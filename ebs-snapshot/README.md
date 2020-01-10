# EBS AUTOSNAPSHOT AND DELETION

## Requirements
- Linux Host with Bash Shell.
- AWS CLI configured (AWS Access ID/Key/Region)
- MailUtils/Postfix

## Features
- Passing Argument (IntanceID/Days/EmailTo/Sender)
- Display Input Details
- Check AWS Installation
- Check Mailutils Installation
- Load AWS Configuration
- Check Instance ID if Exist
- Create Snapshot
- Retrieve All Snapshot
- Auto delete old snapshot (Age in Days)
- Create Log output file
- Dated logs
- Send Email Notification
- Cleanup Logs

:exclamation: **IMPORTANT NOTE:** This will only delete the snapshot/s created by this script with/based-on Tags "CreatedBy:AutomatedBackup". Other backups on the instance are not going to delete.

## **Getting Started**
### **STEP 1:** Download files
- Download the both file ebs_auto & express or pull file from from script_tool repository

`Run Command:`
```
git clone
```
- Change directory to script_tool/ebs_snapshot_script

`Run Command:`
```
cd script_tool/ebs_snapshot_script
```

### _Run the script depending on your needs:_ 
- **Basic Mode (ebs-auto)**
> Manage EBS of a single instance per AWS account.

- **Advance Mode (ebs_auto & express)**
> Manage EBS of multiple instance from different AWS account.

### **STEP 2:** Set file permission 
`Run Command:`
```
chmod 755 ebs_auto
chmod 755 express
```
### **STEP 3:** Choose your preference
### _Two Option to run the script_

:one: **Option 1: Basic Mode (ebs-auto alone)**
> Snapshot and backup volume of a single instance

`Run Command:`
```
./ebs_auto <instance_id> <days> <email> <from-sender>
```
**_For each arguments_**
> - Instance ID 	- 	Specify AWS EC2 Instance ID
> - Days 		- 	Age of the Snapshot in Days to be deleted
> - Email 	- 	Send an Email notification (For multiple emails separated by comma)
> - From		-	Sender name will appear on email (Any name e.g EBS@testaccount.aws)

:two: **Option 2: Express Mode (ebs_auto & express combination)**
> Description: Snapshot and backup volume of multiple instance at the same time from different and multiple AWS account

`Run Command:`
```
./express
```
:exclamation: **Important:** You must edit the file "express" and specify each instance ID before running the script<br />
**_Things you need to do:_**
> - Specify each instance ID
> - Set retention days
> - Set email_to
> - Set AWS profile (for multiple account)

### **STEP 4:** Schedule with Crontab (Optional)
**Note:** You need to convert your localtime to UTC time to set the desire schedule <br />
<br />
**Basic mode**
```
crontab -e
0 6,12 * * * /home/ubuntu/ebs_auto <instance_id> <days> <email-to> <from-sender>
```

**Advance Mode**
```
crontab -e
0 6,12 * * * /home/ubuntu/express
```
