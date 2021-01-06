import os
from aws_cdk import (
    core,
    aws_lambda,
    aws_ecr,
    aws_apigatewayv2 as api_gw,
    aws_apigatewayv2_integrations
)


class LambdaContainerStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ecr_image = aws_lambda.EcrImageCode.from_asset_image(
            directory = os.path.join(os.getcwd(), "lambda-image")
        )
        lambda_function = aws_lambda.Function(self, 
          id            = "lambdaContainerFunction",
          description   = "Sample Lambda Container Function",
          code          = ecr_image,
          ##
          ## Handler and Runtime must be *FROM_IMAGE*
          ## when provisioning Lambda from Container.
          ##
          handler       = aws_lambda.Handler.FROM_IMAGE,
          runtime       = aws_lambda.Runtime.FROM_IMAGE,
          environment   = {"hello":"world"},
          function_name = "sampleContainerFunction",
          memory_size   = 128,
          reserved_concurrent_executions = 10,
          timeout       = core.Duration.seconds(10),
        ) ## aws_lambda.Function
        
        api = api_gw.HttpApi(self, "API")
        
        api.add_routes(path="/hello", 
            methods=[api_gw.HttpMethod.GET],
            integration=aws_apigatewayv2_integrations.LambdaProxyIntegration(handler=lambda_function))
        
        core.CfnOutput(self, "Output", value=api.url)