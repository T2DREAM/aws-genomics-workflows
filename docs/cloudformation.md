# CloudFormation Templates & launching infrastructure

For architectural details, best practices, step-by-step instructions, and customization options, see the [deployment guide](https://fwd.aws/9VdxN).

## Step 1: Compute Environment

### Option A: Full stack

The "Full Stack" CloudFormation template below will create all of the AWS resources required - S3 Bucket, EC2 Launch Templates, IAM Roles, Batch Compute Environments, Batch Job Queues - for your genomics workflow environment.

| Name | Description | Source | Launch Stack |
| -- | -- | :--: | :--: |
{{ cfn_stack_row("Full Stack", "GenomicsEnv-Full", "aws-genomics-root-novpc.template.yaml", "Create EC2 Launch Templates, AWS Batch Job Queues and Compute Environments, a secure Amazon S3 bucket, and IAM policies and roles within an **existing** ") }}

Prior to the final create button, be sure to acknowledge "IAM CAPABILITIES".

![CloudFormation web console wizard IAM capabilities](./images/root-vpc-4.png)

The template will take about 15-20 minutes to finish creating resources.

Once completed, click on the `Outputs` tab and copy down the AWS Batch Job Queue ARN for the default and high-priority queues. You will need these when configuring your workflow orchestration system (e.g. AWS Step Functions, Cromwell, or Nextflow) to use AWS Batch as a backend for task distribution.

![CloudFormation web console wizard output job queue ARN](./images/root-vpc-5.png)

### Option B: Individual components

The `Full Stack` CloudFormation template above is a [nested stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html), a hierarchy of templates that pass values from a parent template to dependent templates.

Below are the stand-alone CloudFormation templates for each of the sub-stacks. These are handy in case you need to modify the individual components, or need to have another individual with elevated privileges to execute one of them (e.g. the IAM template). They are in order of dependency, and you will need to provide output values from one template to the dependent templates.

| Name | Description | Source | Launch Stack |
| -- | -- | :--: | :--: |
{{ cfn_stack_row("Amazon IAM Roles", "GenomicsWorkflow-IAM", "aws-genomics-iam.template.yaml", "Create the necessary IAM Roles. This is useful to hand to someone with the right permissions to create these on your behalf. _You will need to provide an Amazon S3 bucket name_.") }}
{{ cfn_stack_row("EC2 Launch Template", "GenomicsWorkflow-LT", "aws-genomics-launch-template.template.yaml", "Creates an EC2 Launch Template that provisions instances on first boot for processing genomics workflow tasks.") }}
{{ cfn_stack_row("Amazon S3 Bucket", "GenomicsWorkflow-S3", "aws-genomics-s3.template.yaml", "Creates a secure Amazon S3 bucket to read inputs and write results.") }}
{{ cfn_stack_row("AWS Batch", "GenomicsWorkflow-Batch", "aws-genomics-batch.template.yaml", "Creates AWS Batch Job Queues and Compute Environments. You will need to provide the details on IAM roles and instance profiles") }}

## Step 2: Worklow Orchestrators

| Name | Description | Source | Launch Stack |
| -- | -- | :--: | :--: |
{{ cfn_stack_row("Cromwell Server", "CromwellServer", "cromwell/cromwell-server.template.yaml", "Create an EC2 instance and an IAM instance profile to run Cromwell") }}

