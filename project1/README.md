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



Configure your credentials using a [aws profile](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html)
your profile should be named `sandbox`

# Deploying the current stack

1. Run the resources stack, this will create the user with necessary permissions and the repository where the Docker image is going to be uploaded

```sh

cd project1/resources
terraform init
terraform plan
terraform apply

```

You will get the repository and the role you will use for the infrastructure deployment



2. Upload the docker image

You will need to run the following action: `publish-app` and you can get the tag in order to use it in the next step

you will need the export the TAG that will be used in the next step
`export TAG=20210820-1732.6a0bb2054ap`


3. Run the Infrastructure Stack

Export the following variables (Use the info obtained in the step 2)

```sh
export TF_VAR_app_image=ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/ops-hire-app:${TAG}
export TF_VAR_ecs_role=arn:aws:iam::ACCOUNT_ID:role/EcsTasksRole
cd project1/infrastructure
terraform init
terraform plan
terraform apply
```


At the end, the main alb dns will be printed to access to that easily


## Providers

| Name | Version |
|------|---------|
| <a name="provider_aws"></a> [aws](#provider\_aws) | 3.55.0 |
| <a name="provider_template"></a> [template](#provider\_template) | 2.2.0 |

## Modules

No modules.

## Resources

| Name | Type |
|------|------|
| [aws_alb.main_alb](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/alb) | resource |
| [aws_alb_listener.front_end](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/alb_listener) | resource |
| [aws_alb_target_group.app](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/alb_target_group) | resource |
| [aws_cloudwatch_dashboard.cloudwatch_dashboard](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudwatch_dashboard) | resource |
| [aws_cloudwatch_metric_alarm.ecs-alert_High-CPUReservation](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudwatch_metric_alarm) | resource |
| [aws_cloudwatch_metric_alarm.ecs-alert_High-MemReservation](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudwatch_metric_alarm) | resource |
| [aws_ecs_cluster.main](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ecs_cluster) | resource |
| [aws_ecs_service.main](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ecs_service) | resource |
| [aws_ecs_task_definition.app](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ecs_task_definition) | resource |
| [aws_eip.gw](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/eip) | resource |
| [aws_iam_access_key.iam_s3_access](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_access_key) | resource |
| [aws_iam_user.app_user](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_user) | resource |
| [aws_iam_user_policy.app_policy](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_user_policy) | resource |
| [aws_internet_gateway.public_gw](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/internet_gateway) | resource |
| [aws_nat_gateway.gw](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/nat_gateway) | resource |
| [aws_route_table.private_rt](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/route_table) | resource |
| [aws_route_table.public_rt](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/route_table) | resource |
| [aws_route_table_association.private_rta](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/route_table_association) | resource |
| [aws_route_table_association.public_rta](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/route_table_association) | resource |
| [aws_s3_bucket.ops_hire_app_bucket](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket) | resource |
| [aws_security_group.ecs_tasks](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/security_group) | resource |
| [aws_security_group.lb_sg](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/security_group) | resource |
| [aws_subnet.private_subnets](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/subnet) | resource |
| [aws_subnet.public_subnets](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/subnet) | resource |
| [aws_vpc.main_vpc](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/vpc) | resource |
| [aws_availability_zones.available_zones](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/availability_zones) | data source |
| [template_file.app](https://registry.terraform.io/providers/hashicorp/template/latest/docs/data-sources/file) | data source |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_app_count"></a> [app\_count](#input\_app\_count) | Number of docker containers to run | `number` | `2` | no |
| <a name="input_app_image"></a> [app\_image](#input\_app\_image) | Docker image to run in the ECS cluster | `any` | n/a | yes |
| <a name="input_app_port"></a> [app\_port](#input\_app\_port) | Port exposed by the docker image to redirect traffic to | `number` | `8080` | no |
| <a name="input_aws_az_count"></a> [aws\_az\_count](#input\_aws\_az\_count) | Number of availability\_zones to cover in the region | `number` | `2` | no |
| <a name="input_aws_region"></a> [aws\_region](#input\_aws\_region) | The AWS region to create things in. | `string` | `"us-east-1"` | no |
| <a name="input_aws_zone"></a> [aws\_zone](#input\_aws\_zone) | The AWS zone to create things in. | `string` | `"us-east-1b"` | no |
| <a name="input_ecs_role"></a> [ecs\_role](#input\_ecs\_role) | ECS role to allow access to the ECR repository | `any` | n/a | yes |
| <a name="input_fargate_cpu"></a> [fargate\_cpu](#input\_fargate\_cpu) | Fargate instance CPU units to provision (1 vCPU = 1024 CPU units) | `string` | `"256"` | no |
| <a name="input_fargate_memory"></a> [fargate\_memory](#input\_fargate\_memory) | Fargate instance memory to provision (in MiB) | `string` | `"256"` | no |
| <a name="input_project_name_prefix"></a> [project\_name\_prefix](#input\_project\_name\_prefix) | Name of the project | `string` | `"ops-hire-project"` | no |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_access_key_id"></a> [access\_key\_id](#output\_access\_key\_id) | The access key ID |
| <a name="output_alb_hostname"></a> [alb\_hostname](#output\_alb\_hostname) | The dns to access to the application |
| <a name="output_bucket_id"></a> [bucket\_id](#output\_bucket\_id) | Bucket Name (aka ID) |
| <a name="output_private_subnet_arn"></a> [private\_subnet\_arn](#output\_private\_subnet\_arn) | Private subnet ARN |
| <a name="output_public_subnet_arn"></a> [public\_subnet\_arn](#output\_public\_subnet\_arn) | Public subnet ARN |
| <a name="output_secret_access_key"></a> [secret\_access\_key](#output\_secret\_access\_key) | The secret access key. This will be written to the state file in plain-text |





# Improvements for this version 


* Improve the CI/CD process to deploy/destroy the stack easily
* Make sure that policies for User and ECS task are correct or you need to be more restricitve
    * For S3 bucket use a role for the ecs service instead passing environment variables
* Integrate all infra in one Stack to avoid get data manually
* Don't print the aws credentials (use Parameter store, 1 Password or other tool that manage secrets)
* Use MFA for running these tasks
* Update all resouces in separated files where necessary 
* Improve the monitoring part
* Add linter + testing

# Tasks

- Update the infrastructure to run the container in Fargate []
    - If you want to use Terraform instead, please do! We use both at Contrast and enjoy discussions comparing the two.
- Add monitoring for your service []
- Add an endpoint to `app.py` to return a file from an S3 bucket []

## Things to keep in mind

- Treat this like a production service - think about concepts such as reliability, principle of least privilege, availability, security, etc.
- Break down the work into sizeable chunks (PR per task, commit per task, etc). Show us how you would approach this work.

# Bonus points!

Add what you feel could be missing from this project. Show us how you think about running a service in AWS and what you are passionate about.

# Feedback

We love feedback. PR or create issues on this repository with feedback on what we could do better!