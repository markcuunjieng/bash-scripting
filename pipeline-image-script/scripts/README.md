# CICD Script Command

## Enable SSH Key

`Usage:`

```
source cicd key enable

```

## Load Credentials

`Usage:`

```
cicd cred DEV | QA | STG | PROD

Option:
    DEV     =   For AWS DEV Credentials
    QA      =   For AWS QA Credentials
    STG     =   For AWS STG Credentials
    PROD    =   For AWS Production Credentials
```

`e.g.`
```
source cicd PROD

```

## Pipeline Trigger

`Usage:`

```
cicd pipeline <pipeline_id> <token>

Option:
    PIPELINE ID     =   Gitlab Pipeline ID
    TOKEN           =   Gitlab Pipeline Token
```

`e.g`
```
cicd pipeline 101 xxxxxxxx

```

## Ansible Tower Deployment

`Usage:`

```
Usage: cicd deploy <environment> <job_template>

Option:
    QA | PROD       =   For AWS QA/PROD Environment
    JOB TEMPLATE    =   Ansible Job Template ID
```

`e.g`
```
cicd deploy QA 123
```

## Merge Request

`Usage:`

```
Usage: cicd mr <project_id> <token>

Option:
    PROJECT ID      =   Gitlab Project ID
    TOKEN           =   Gitlab Token

```

`e.g.`
```
e.g cicd mr 101 xxxxxxxx
```

## MS Teams Notification

`Usage:`

```
Usage: cicd notif <webhook_url>

Option:
    WEBHOOK URL     =   MS Teams Webhook
```

`e.g.`
```
cicd notif https://outlook.office.com/webhook/fe1c489e-9ad5
```

## Mail Log

`Usage:`

```
Usage: cicd sendlog <email_address>

Option:
    MAIL TO    =   Email of Recipient
```

`e.g.`
```
cicd sendlog sample@mail.com
```

## Enable Configuration

`Usage:`

```
Usage: config enable

```

## Snyk Scanning

`Usage:`

```
Usage: snyk-scan run

```

## Tenable Scanning

`Usage:`

```
Usage: tenable-scan run

```