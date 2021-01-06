#!/usr/bin/env python3

from aws_cdk import core
from stacks.lambda_container_stack import LambdaContainerStack

app = core.App()
env = {'region': 'us-east-1'}
lambda_container_stack = LambdaContainerStack(app, "lambda-container-stack", env=env)
app.synth()
