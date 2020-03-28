#!/usr/bin/env python3

from aws_cdk import core

from cdk_labs.cdk_labs_stack import CdkLabsStack


app = core.App()
CdkLabsStack(app, "cdk-labs")

app.synth()
