#!/usr/bin/env python3

from aws_cdk import core
from cdk_labs.s3.bucket_stack import S3BucketStack


app = core.App()
S3BucketStack(app, "cdk-labs")

app.synth()
