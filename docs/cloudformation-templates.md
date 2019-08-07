# Quick Start - For rapid deployment

## Step 1: Compute Environment

The "Full Stack" CloudFormation template below will create all of the AWS resources required - S3 Bucket, EC2 Launch Templates, IAM Roles, Batch Compute Environments, Batch Job Queues - for your genomics workflow environment into an existing VPC.

| Name | Description | Source | Launch Stack |
| -- | -- | :--: | :--: |
{{ cfn_stack_row("Full Stack (Existing VPC)", "GenomicsEnv-Full", "aws-genomics-root-novpc.template.yaml", "Create EC2 Launch Templates, AWS Batch Job Queues and Compute Environments, a secure Amazon S3 bucket, and IAM policies and roles within an **existing** VPC. _NOTE: You must provide VPC ID, and subnet IDs_.") }}

Prior to the final create button, be sure to acknowledge "IAM CAPABILITIES".

![CloudFormation web console wizard IAM capabilities](./images/root-vpc-4.png)

The template will take about 15-20 minutes to finish creating resources.

Once completed, click on the `Outputs` tab and copy down the AWS Batch Job Queue ARN for the default and high-priority queues. You will need these when configuring your workflow orchestration system (e.g. AWS Step Functions, Cromwell, or Nextflow) to use AWS Batch as a backend for task distribution.

![CloudFormation web console wizard output job queue ARN](./images/root-vpc-5.png)


## Step 2: Workflow Orchestrator - Nextflow

| Name | Description | Source | Launch Stack |
| -- | -- | :--: | :--: |
{{ cfn_stack_row("Nextflow Resources", "NextflowResources", "nextflow/nextflow-resources.template.yaml", "Create Nextflow specific resources needed to run on AWS: an S3 Bucket for nextflow config and workflows, AWS Batch Job Definition for a Nextflow head node, and an IAM role for the nextflow head node job") }}

