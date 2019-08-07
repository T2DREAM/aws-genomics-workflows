# Permissions

## Create IAM Roles

IAM roles that your job execution environment in AWS Batch will use include:

* **Batch Service Role (required)**:
    
    Role used by AWS Batch to call other AWS services on its behalf.
    AWS Batch makes calls to other AWS services on your behalf to manage the resources that you use with the service. Before you can use the service, you must have an IAM policy and role that provides the necessary permissions to AWS Batch.
    [(Learn More)](https://docs.aws.amazon.com/batch/latest/userguide/service_IAM_role.html)

* **Batch Instance Profile (required)**:
    
    Role that defines service permissions for EC2 instances launched by AWS Batch.
    For example, this is used to specify policies that allow access to specific S3 buckets and modify storage on the instance (shown below).
    [(Learn More)](https://docs.aws.amazon.com/batch/latest/userguide/instance_IAM_role.html)

```yaml

# this inline policy specifies access to a single S3 bucket
- PolicyName: DGA-S3Bucket-Access-us-west-2
    PolicyDocument:
        Version: 2012-10-17
        Statement:
            Effect: Allow
            Resource:
                - "arn:aws:s3:::<bucket_name>"
                - "arn:aws:s3:::<bucket_name>/*"
            Action:
                - "s3:*"

# this inline policy allows the job instance to attach EBS volumes to create
# extra scratch space for genomic data
- PolicyName: DGA-Autoscale-EBS-us-west-2
    PolicyDocument:
        Version: 2012-10-17
        Statement:
            Effect: Allow
            Action:
            - "ec2:createVolume"
            - "ec2:attachVolume"
            - "ec2:deleteVolume"
            - "ec2:modifyInstanceAttribute"
            - "ec2:describeVolumes"
            Resource: "*"
```

* **Batch SpotFleet Role (depends)**:
    
    This role is needed if you intend to launch spot instances from AWS Batch.
    If you create a managed compute environment that uses Amazon EC2 Spot Fleet Instances, you must create a role that grants the Spot Fleet permission to bid on, launch, tag, and terminate instances on your behalf.
    [(Learn More)](https://docs.aws.amazon.com/batch/latest/userguide/spot_fleet_IAM_role.html)

* **Note - At this time we do not plan to use spot instances for our genomics work flow

* **Batch Job Role (optional)**:

    Role used to provide service permissions to individual jobs.
    Jobs can run without an IAM role. In that case, they inherit the
    permissions of the instance they run on.
