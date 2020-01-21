#!/bin/bash

set -e

echo "publishing site"
aws s3 sync \
    --delete \
    ./site \
    s3://www.docs.diabetesepigenome.org/genomics-workflow/

