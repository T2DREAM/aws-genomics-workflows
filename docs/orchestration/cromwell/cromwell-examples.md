# Cromwell Examples

The following are some example workflows you can use to test Cromwell on AWS.
The `curl` commands assume that you have access to a Cromwell server via `localhost:8000`.

## Simple Hello World

This is a single file workflow.  It simply echos "Hello AWS!" to `stdout` and exits.

**Workflow Definition**

`simple-hello.wdl`

```java
task echoHello{
    command {
        echo "Hello AWS!"
    }
    runtime {
        docker: "ubuntu:latest"
    }

}

workflow printHelloAndGoodbye {
    call echoHello
}

```

**Running the workflow**

To submit this workflow via `curl` use the following command:

```bash
$ curl -X POST "http://localhost:8000/api/workflows/v1" \
    -H  "accept: application/json" \
    -F "workflowSource=@/path/to/simple-hello.wdl"
```

You should receive a response like the following:

```json
{"id":"104d9ade-6461-40e7-bc4e-227c3a49e98b","status":"Submitted"}
```

If the workflow completes successfully, the server will log the following:

```
2018-09-21 04:07:42,928 cromwell-system-akka.dispatchers.engine-dispatcher-25 INFO  - WorkflowExecutionActor-7eefeeed-157e-4307-9267-9b4d716874e5 [UUID(7eefeeed)]: Workflow w complete. Final Outputs:
{
  "w.echo.f": "s3://aws-cromwell-test-us-east-1/cromwell-execution/w/7eefeeed-157e-4307-9267-9b4d716874e5/call-echo/echo-stdout.log"
}
2018-09-21 04:07:42,931 cromwell-system-akka.dispatchers.engine-dispatcher-25 INFO  - WorkflowManagerActor WorkflowActor-7eefeeed-157e-4307-9267-9b4d716874e5 is in a terminal state: WorkflowSucceededState
```

## Hello World with inputs

This workflow is virtually the same as the single file workflow above, but
uses an input file to define parameters in the workflow.

**Workflow Definition**

`hello-aws.wdl`

```java
task hello {
  String addressee
  command {
    echo "Hello ${addressee}! Welcome to Cromwell . . . on AWS!"
  }
  output {
    String message = read_string(stdout())
  }
  runtime {
    docker: "ubuntu:latest"
  }
}

workflow wf_hello {
  call hello

  output {
     hello.message
  }
}
```

**Inputs**

`hello-aws.json`

```json
{
    "wf_hello.hello.addressee": "World!"
}
```

**Running the workflow**

Submit this workflow using:

```bash
$ curl -X POST "http://localhost:8000/api/workflows/v1" \
    -H  "accept: application/json" \
    -F "workflowSource=@hello-aws.wdl" \
    -F "workflowInputs=@hello-aws.json"
```

## Using data on S3

This workflow demonstrates how to use data from S3.

First, create some data:

```bash
$ curl "https://baconipsum.com/api/?type=all-meat&paras=1&format=text" > meats.txt
```

and upload it to your S3 bucket:


```bash
$ aws s3 cp meats.txt s3://<your-bucket-name>/
```

Create the following `wdl` and input `json` files.

**Workflow Definition**

`s3inputs.wdl`

```java
task read_file {
  File file

  command {
    cat ${file}
  }

  output {
    String contents = read_string(stdout())
  }

  runtime {
    docker: "ubuntu:latest"
  }
}

workflow ReadFile {
  call read_file

  output {
    read_file.contents
  }
}
```

**Inputs**

`s3inputs.json`

```json
{
  "ReadFile.read_file.file": "s3://aws-cromwell-test-us-east-1/meats.txt"
}
```

**Running the workflow**

Submit the workflow via `curl`:

```bash
$ curl -X POST "http://localhost:8000/api/workflows/v1" \
    -H  "accept: application/json" \
    -F "workflowSource=@s3inputs.wdl" \
    -F "workflowInputs=@s3inputs.json"
```

If successful the server should log the following:

```
2018-09-21 05:04:15,478 cromwell-system-akka.dispatchers.engine-dispatcher-25 INFO  - WorkflowExecutionActor-1774c9a2-12bf-42ea-902d-3dbe2a70a116 [UUID(1774c9a2)]: Workflow ReadFile complete. Final Outputs:
{
  "ReadFile.read_file.contents": "Strip steak venison leberkas sausage fatback pork belly short ribs.  Tail fatback prosciutto meatball sausage filet mignon tri-tip porchetta cupim doner boudin.  Meatloaf jerky short loin turkey beef kielbasa kevin cupim burgdoggen short ribs spare ribs flank doner chuck.  Cupim prosciutto jerky leberkas pork loin pastrami.  Chuck ham pork loin, prosciutto filet mignon kevin brisket corned beef short loin shoulder jowl porchetta venison.  Hamburger ham hock tail swine andouille beef ribs t-bone turducken tenderloin burgdoggen capicola frankfurter sirloin ham."
}
2018-09-21 05:04:15,481 cromwell-system-akka.dispatchers.engine-dispatcher-28 INFO  - WorkflowManagerActor WorkflowActor-1774c9a2-12bf-42ea-902d-3dbe2a70a116 is in a terminal state: WorkflowSucceededState
```

## Genomics pipeline example ATACseq
