# SERVICE CHECKER 

## Requirements
- Linux
- MailUtils/Postfix

## Functionalities
- Check Multiple Services (User Define)
- Check Status 
- Create Log output file
- Dated logs
- Send Email Notification using Postfix
- Cleanup Logs

## **Getting Started**
### **STEP 1:** Download the file
- Download service-check

### **STEP 2:** Set file permission 
`Run Command:`
```
chmod 755 service-check
```
### **STEP 3:** Run the script 

`Run Command:`
```
./service-check
```
:exclamation: **Important:** You must edit the script to specify each services you want to check<br />
**_Things you need to do:_**
> - Specify services to check 
> - Set email_to

### **STEP 4:** Schedule with Crontab (Optional)
**Note:** You need to convert your localtime to UTC time to set the desire schedule <br />
<br />

**Cron job**
Everyday 1am
```
crontab -e
0 1 * * * /home/ubuntu/service-stat
```
