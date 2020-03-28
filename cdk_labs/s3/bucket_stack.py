from aws_cdk import (
    aws_s3 as s3,
    core
)

class S3BucketStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        #create an S3 bucket
        s3Bucket = s3.Bucket(self, 'Bucket', bucket_name=self.node.try_get_context("bucket_name"))
        core.Tag.add(s3Bucket, "key", "value")

