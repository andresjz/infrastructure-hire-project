# Infrastructure Hire Project 1

# Overview

At Contrast we like to play hard, work hard, and automate our SaaS environment end to end. We made this project so you can showcase your skills and give us a better idea of your individual talents!

# Setup

You will need the following:

* A fork of this repository (If you have concerns about this, let us know!)
* An AWS account (Contrast will provide a temporary one)
* Docker
* Python
* [AWS CLI](https://aws.amazon.com/cli/)
* Terraform 

# Deploying the current stack

1. Run the resources stack, this will create the user with necessary permissions and the repository where the Docker image is going to be uploaded

```sh

cd resources
terraform init
terraform plan
terraform apply

```

You will get the repository and the user you will use for the infrastructure deployment


2. Upload the docker image

You will need to run the following action: `publish-app`
3. Run the Infrastructure Stack

TBD

################################
# Deploying the current stack

```
aws cloudformation deploy --template-file infrastructure/infrastructure.yml --stack-name ops-hire-project --tags Name=ops-hire-project Environment=dev
```

# Tasks

- Update the infrastructure to run the container in Fargate
    - If you want to use Terraform instead, please do! We use both at Contrast and enjoy discussions comparing the two.
- Add monitoring for your service
- Add an endpoint to `app.py` to return a file from an S3 bucket

## Things to keep in mind

- Treat this like a production service - think about concepts such as reliability, principle of least privilege, availability, security, etc.
- Break down the work into sizeable chunks (PR per task, commit per task, etc). Show us how you would approach this work.

# Bonus points!

Add what you feel could be missing from this project. Show us how you think about running a service in AWS and what you are passionate about.

# Feedback

We love feedback. PR or create issues on this repository with feedback on what we could do better!