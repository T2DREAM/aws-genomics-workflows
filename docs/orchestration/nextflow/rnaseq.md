# RNAseq pipeline

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
For the nf-core example "rnaseq" workflow you will see 11 jobs run in Batch over the course of a couple hours - the head node will last the whole duration of the pipeline while the others will stop once their step is complete. You can look at the CloudWatch logs for the head node job to monitor workflow progress. Note the additional single quotes wrapping the 1000genomes path.