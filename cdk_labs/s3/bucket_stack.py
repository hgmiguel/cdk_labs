from aws_cdk import (
    aws_s3 as s3,
    aws_ssm as ssm,
    core
)

import uuid
import boto3
import json

class S3BucketStack(core.Stack):

    def get_hash(self, bucket_name):
        client = boto3.client('ssm')
        s3_hash_parameter = self.node.try_get_context("s3_hash_parameter")
        try:
            response = client.get_parameter(
                Name=s3_hash_parameter,
                WithDecryption=True
            )

            s3_hashes = json.loads(response['Parameter']['Value'])
            if bucket_name in s3_hashes:
                return s3_hashes[bucket_name]
            else:
                s3_hashes[bucket_name] = uuid.uuid4().hex[:6]
        except  Exception as e:
            print(e)
            s3_hashes = {bucket_name: uuid.uuid4().hex[:6]}

        response = client.put_parameter(
            Name=s3_hash_parameter,
            Value=json.dumps(s3_hashes),
            Type='SecureString',
            Overwrite=True,
            Tier='Intelligent-Tiering'
        )

        return s3_hashes[bucket_name]

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        #get inmutable hash
        bucket_name = self.node.try_get_context("bucket_name")
        hash_value = self.get_hash(bucket_name)
        #if 'dummy' in hash_value:
        #    hash_value = uuid.uuid4().hex[:6]

        print(hash_value)



        #create an S3 bucket
        s3Bucket = s3.Bucket(self, 'Bucket', bucket_name=f'{bucket_name}-{hash_value}')
        core.Tag.add(s3Bucket, "key", "value")

