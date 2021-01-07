# lambda-containers
POC project for running lambda functions based on containers.

* We will create an API Gateway with one endpoint (GET /hello). 
* This endpoint will proxy the request to a lambda function.
* The lambda function is deployed as container image.
* We're using an AWS provided base image (see /lambda-image/Dockerfile)
* Lambda function code is in /lambda-image/hello.py (this is what is copied to the container image)

## Instructions ##

We'll be using [CDK](https://docs.aws.amazon.com/cdk/latest/guide/home.html) for creating our infrastructure.

First, make sure you clone this project

```
$git clone https://github.com/gmansilla/lambda-container-images.git && cd lambda-container-images
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