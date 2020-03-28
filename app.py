#!/usr/bin/env python3

from aws_cdk import core
from cdk_labs.s3.bucket_stack import S3BucketStack
import os


app = core.App()
S3BucketStack(app, "cdk-labs", env=core.Environment(
    account=os.environ.get("CDK_DEPLOY_ACCOUNT", os.environ["CDK_DEFAULT_ACCOUNT"]),
    region=os.environ.get("CDK_DEPLOY_REGION", os.environ["CDK_DEFAULT_REGION"])))

app.synth()
