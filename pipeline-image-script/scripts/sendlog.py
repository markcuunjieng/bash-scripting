#!/usr/bin/env python3

import boto3
import sys
import os
import json2table
import json
import time
import glob

from botocore.exceptions import ClientError
from os.path import abspath
from json2html import *
from json2table import *
from os import path

# ========= #
# VARIABLES #
# ========= #

ALLOWED_EXTENSTIONS = {".json", ".log"}
project_name = os.environ.get('CI_PROJECT_NAME')
pipeline_url = os.environ.get('CI_PIPELINE_URL')
release = os.environ.get('APPLICATION')
SENDER = "marccuunjieng@gmail.com"
RECIPIENTS =  sys.argv[1]
AWS_REGION = "us-east-1"
SUBJECT = project_name + "-" + release        
CHARSET = "UTF-8"
client = boto3.client('ses',region_name=AWS_REGION)

# ========= #
# LOAD FILE #
# ========= #

def load_files():
    json_files = []
    for json_file in glob.glob("*.json"):
        f_path = abspath(json_file)
        print("Loading file..",json_file),
        time.sleep(3),
        try:
            with open(f_path) as data_file:
                data = json.load(data_file)
            if 'unapproved' in data: 
                del data['unapproved']
            with open(f_path, 'w') as data_file:
                data = json.dump(data, data_file)
            with open(f_path) as json_data:
                json_obj = json.load(json_data)
            json_obj_in_html = json2html.convert(json_obj)
        except IOError:
            print("Unknown file",json_file,"or file doesn't exist.")
            sys.exit()
        try:
            response = client.send_email(
                Destination={
                    'ToAddresses': [
                        RECIPIENTS,
                        "marccuunjieng@gmail.com",
                        "marccuunjieng@gmail.com"",
                    ],
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': CHARSET,
                            'Data': "<b>Pipeline: </b>" + SUBJECT + "<br><b>Security: </b>" + json_file + json_obj_in_html,
                        },
                        'Text': {
                            'Charset': CHARSET,
                            'Data': json_obj_in_html,
                        },
                    },
                    'Subject': {
                        'Charset': CHARSET,
                        'Data': SUBJECT,
                    },
                },
                Source=SENDER,
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            print("Email sent! Message ID:"),
            print(response['MessageId'])

# ============= #
# CALL FUNCTION #
# ============= #

load_files()
