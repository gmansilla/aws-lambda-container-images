# AWS Lambda containers
POC project for running AWS Lambda functions based on containers.

* We will create an API Gateway with one endpoint (GET /hello). 
* This endpoint will proxy the request to a lambda function.
* The lambda function is deployed as container image.
* We're using an AWS provided base image (see /lambda-image/Dockerfile)
* Lambda function code is in /lambda-image/hello.py (this is what is copied to the container image)

## Instructions ##

We'll be using [CDK](https://docs.aws.amazon.com/cdk/latest/guide/home.html) for creating our infrastructure.

First, make sure you clone this project

```
$git clone https://github.com/gmansilla/aws-lambda-container-images.git && cd aws-lambda-container-images
```

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

Prior to deploying, we need to bootstrap CDK

```
$cdk bootstrap
```

And we're ready to deploy!

```
$cdk deploy
```

Pay attention to the Output of this command as this will tell you the URL we're going to use to test our API.


## Testing ##

Now that the infrastructure has been deployed, you can start sending GET requests to the URL printed in the previous step

## Testing Locally ##

Since your lambda function is using a container image, and this image comes with the Lambda Runtime Interface Emulator,
you can test your function locally!

Let's use the Docker CLI to build our image locally:
```
$cd lambda-image
$docker build -t demo .
```

Now, let's start the container image locally using the Lambda Runtime Interface Emulator
```
$docker run -p 9000:8080 demo:latest
```

Finally, we can start testing function invocation with cURL by opening a new terminal and sending a request.
```
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
```

You'll see in your logs something like
<pre>
START RequestId: aa505f95-1bed-4fd2-adb2-2405effee01b Version: $LATEST
END RequestId: aa505f95-1bed-4fd2-adb2-2405effee01b
REPORT RequestId: aa505f95-1bed-4fd2-adb2-2405effee01b  Init Duration: 1.61 ms  Duration: 80.78 ms      Billed Duration: 100 ms Memory Size: 3008 MB     Max Memory Used: 3008 MB
</pre>
Just like you would see in AWS Lambda Console!


## Pushing changes ##
Since we're using CDK, we can just run ```$cdk deploy``` and the new image will be uploaded to ECR. As mentioned before, look at the output
as it will print the URL you're going to use to make api calls.

## Destroying the stack ##
After you experiment with this project you should run ```$cdk destroy``` to destroy all the infrastructure we created and avoid incurring in extra charges


Enjoy!

## Further Reading ##
* [New for AWS Lambda – Container Image Support Blog Post](https://aws.amazon.com/blogs/aws/new-for-aws-lambda-container-image-support/)
* [Testing AWS Lambda container images locally](https://docs.aws.amazon.com/lambda/latest/dg/images-test.html)
* [Create an image from an AWS base image for Lambda](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-create-1)
* [Create an image from an alternative base image](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-create-2)