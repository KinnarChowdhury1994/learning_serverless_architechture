"""
Assignment 4: Monitor Unencrypted S3 Buckets Using AWS Lambda and Boto3

Objective: To enhance your AWS security posture by setting up a Lambda function that detects any S3 bucket without server-side encryption.

Task: Automate the detection of S3 buckets that don't have server-side encryption enabled.

Instructions:

1. S3 Setup:

   - Navigate to the S3 dashboard and create a few buckets. Ensure that a couple of them don't have server-side encryption enabled.

2. Lambda IAM Role:

   - In the IAM dashboard, create a new role for Lambda.

   - Attach the `AmazonS3ReadOnlyAccess` policy to this role.

3. Lambda Function:

   - Navigate to the Lambda dashboard and create a new function.

   - Choose Python 3.x as the runtime.

   - Assign the IAM role created in the previous step.

   - Write the Boto3 Python script to:

     1. Initialize a boto3 S3 client.
     2. List all S3 buckets.
     3. Detect buckets without server-side encryption.
     4. Print the names of unencrypted buckets for logging purposes.

4. Manual Invocation:

   - After saving your function, manually trigger it.

   - Review the Lambda logs to identify the buckets without server-side encryption.
"""
import boto3
import json

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # TODO implement
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps('Hello from Lambda!')
    # }
    
    # response = s3.list_buckets()
    s3List = s3.list_buckets()
    print(f"All S3 Buckets :: {s3List}")
    
    # Get a list of all bucket names from the response
    buckets = [bucket['Name'] for bucket in s3List['Buckets']]
    # Print out the bucket list
    print(f"Bucket List: {buckets}")
    
    for i in range(len(buckets)):
        enc = s3.get_bucket_encryption(Bucket=str(buckets[i]))
        rules = enc['ServerSideEncryptionConfiguration']['Rules']
        print(f"Bucket: {buckets[i]} =============== Encryption: {rules}\n")
