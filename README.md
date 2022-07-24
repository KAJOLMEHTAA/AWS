# Send Email A Month Before the Reserved Instance Expires
## Introduction:
In this Article, we will go through how we can receive email notifications a month before the Reserved Instance expires.

Instances are never shut down or terminated because an Amazon EC2 Reserved Instance (RI) expires.

However, when an RI expires, you might notice a change in the pricing of one or more of your instances. This is because any instances that were covered by the RI pricing benefit are now billed at the on-demand price.

You can set reservation expiration alerts to remind you when your RIs are about to expire.

The following are the steps to follow to set email notifications:
1. Create a Lambda function, where you will check for all the instances and send mail before a month
2. Create an SNS Topic which will be called by the Lambda function.

## Step-by-Step Explanation:
1. Create a Lambda function:
      * Open Lambda Console, Create Function
      * Enter the function Name, Select Python 3.9, create a IAM role with following policies and attach the same to the Lambda function. EC@FullAccess and SNSFullAccess.
      * Click on Create Function, will redirect to the Function page with Basic Lambda Code, copy the below Lambda code and paste it in the console
      * This is the Lambda function which will call the SNS.
      * [Refer This File](https://github.com/KAJOLMEHTAA/Reserved_Instance/blob/main/RI.py)

2. SNS Topic:
      * Open SNS Topic Console, Create Topic
      * Under the Topic Create Subscription, Protocol as AWS Lambda and Specify the Lambda Function to invoke in Endpoint.
