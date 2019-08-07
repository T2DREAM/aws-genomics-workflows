# T2D AMP Consortium Genomics Workflows on AWS


## The purpose of this document is to demonstrate highly scaleable, cost effective and reproducible genomics workflow 

This documentation contains:

1. Overview to run genomics pipelines on AWS for T2D AMP consortium members

2. Getting started with AWS cloud computing & resources

3. [AWS CloudFormation](https://aws.amazon.com/cloudformation/) templates to create all of the AWS resources required - S3 Bucket, EC2 compute nodes optimized to run genomics pipelines (i.e. elastic storage, elastic load balancing, run container tools and Nextflow orchestrator server), IAM Roles, Batch Compute Environments, Batch Job Queues - specifically designed to run T2D AMP community's genomics workflows

4. Workflow orchestration using Nextflow

DGA will maintain cloudformation templates to [launch resources](http://www.docs.t2depigenome.org/genomics-workflow/cloudformation/). T2D AMP member will be tasked to convert their pipelines to [Nextflow Workflow that would submit a nextflow Batch job to the appropriate Batch Job Queue via. AWS CLI] (http://www.docs.t2depigenome.org/genomics-workflow/orchestration/nextflow/nextflow-example/) 

Frequently used Nextflow genomics pipelines built by community can be accessed here -  https://nf-co.re/pipelines 

