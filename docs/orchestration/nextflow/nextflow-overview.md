# Nextflow on AWS Batch

![Nextflow on AWS](./images/nextflow-on-aws-infrastructure.png)

[Nextflow](https://www.nextflow.io) is a reactive workflow framework and domain specific language (DSL) developed by the [Comparative Bioinformatics group](https://www.crg.eu/en/programmes-groups/notredame-lab) at the Barcelona [Centre for Genomic Regulation (CRG)](http://www.crg.eu/) that enables scalable and reproducible scientific workflows using software containers.

Nextflow can be run either locally or on a dedicated EC2 instance.  The latter is preferred if you have long running workflows - with the caveat that you are responsible for stopping the instance when your workflow is complete.  The architecture presented in this guide demonstrates how you can run Nextflow using AWS Batch in a managed and cost effective fashion.


## Running a workflow

### Configuration

The entrypoint script for the `nextflow` container above generates a default config file automatically that looks like the following:

```groovy
// where workflow logs are written
workDir = 's3://<s3-nextflow-bucket>/<s3-prefix>/runs'

process.executor = 'awsbatch'
process.queue = '<batch-job-queue>'

// AWS CLI tool is installed via the instance launch template
executor.awscli = '/home/ec2-user/miniconda/bin/aws'
```

The script will replace `<s3-nextflow-bucket>`, `<s3-prefix>`, and `<batch-job-queue>` with values appropriate for your environment.


### Running the workflow (RNAseq pipeline)

To run a workflow you submit a `nextflow` Batch job to the appropriate Batch Job Queue via the command line with the AWS CLI

```
git clone https://github.com/nf-core/rnaseq.git
aws s3 sync rnaseq s3://path/to/workflow/folder

aws batch submit-job \
    --job-name run-workflow-nf \
    --job-queue <queue-name> \
    --job-definition nextflow \
    --container-overrides command=s3://path/to/workflow/folder,\
"--reads","'s3://1000genomes/phase3/data/HG00243/sequence_read/SRR*_{1,2}.filt.fastq.gz'",\
"--genome","GRCh37",\
"--skip_qc"
```

After submitting a workflow, you can monitor the progress of tasks via the AWS Batch console.

For the nf-core example "rnaseq" workflow you will see 11 jobs run in Batch over the course of a couple hours - the head node will last the whole duration of the pipeline while the others will stop once their step is complete. You can look at the CloudWatch logs for the head node job to monitor workflow progress. Note the additional single quotes wrapping the 1000genomes path.
