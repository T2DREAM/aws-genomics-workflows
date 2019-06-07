#!/bin/bash

set -e

echo "publishing templates:"
aws s3 sync \
    --acl public-read \
    --delete \
    --metadata commit=$(git rev-parse HEAD) \
    ./src/templates \
    s3://aws-genomics-workflow/templates


echo "publishing site"
aws s3 sync \
    --acl public-read \
    --delete \
    ./site \
    s3://www.docs.t2depigenome.org/genomics-workflow

