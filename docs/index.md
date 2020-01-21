# T2D AMP Consortium Genomics Workflows on AWS

The purpose of this document is to demonstrate highly scaleable, cost effective and reproducible genomics workflow 

This documentation contains:

1. Overview to run genomics pipelines on AWS for T2D AMP consortium members

2. Getting started with AWS cloud computing & resources

3. [AWS CloudFormation](https://aws.amazon.com/cloudformation/) templates to create all of the AWS resources required - S3 Bucket, EC2 compute nodes optimized to run genomics pipelines (i.e. elastic storage, elastic load balancing, run container tools and Nextflow orchestrator server), IAM Roles, Batch Compute Environments, Batch Job Queues - specifically designed to run T2D AMP community's genomics workflows

4. Workflow orchestration using Nextflow

Frequently used Nextflow genomics pipelines built by community can be accessed here -  https://nf-co.re/pipelines.

Get in touch with DGA team if you would like to implement your pipeline on AWS cloud. 

