"""
Assignment 2: Automated S3 Bucket Cleanup Using AWS Lambda and Boto3

Objective: To gain experience with AWS Lambda and Boto3 by creating a Lambda function that will automatically clean up old files in an S3 bucket.

Task: Automate the deletion of files older than 30 days in a specific S3 bucket.

Instructions:

1. S3 Setup:

   - Navigate to the S3 dashboard and create a new bucket.

   - Upload multiple files to this bucket, ensuring that some files are older than 30 days (you may need to adjust your system's date temporarily for this or use old files).

2. Lambda IAM Role:

   - In the IAM dashboard, create a new role for Lambda.

   - Attach the `AmazonS3FullAccess` policy to this role. (Note: For enhanced security in real-world scenarios, use more restrictive permissions.)

3. Lambda Function:

   - Navigate to the Lambda dashboard and create a new function.

   - Choose Python 3.x as the runtime.

   - Assign the IAM role created in the previous step.

   - Write the Boto3 Python script to:

     1. Initialize a boto3 S3 client.
     2. List objects in the specified bucket.
     3. Delete objects older than 30 days.
     4. Print the names of deleted objects for logging purposes.

4. Manual Invocation:

   - After saving your function, manually trigger it.

   - Go to the S3 dashboard and confirm that only files newer than 30 days remain.
"""
import json
import boto3
from datetime import datetime,timedelta

bucket_name = "kinnar-chowdhury-b4"
cleanup_schedule = 30

S3 = boto3.client('s3')

def lambda_handler(event, context):
    # # TODO implement
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps('Hello from Lambda!')
    # }
    objects = S3.list_objects(Bucket=str(bucket_name))
    print(f"Objects in {bucket_name} Bucket :: {objects}")
    
    contents = objects.get('Contents',[])
    if len(contents) > 0:
        for i in range(len(contents)):
            file = contents[i]['Key']
            print(f'Object inside bucket :: {file}')
            
            LastModified = contents[i]['LastModified'].replace(tzinfo=None)
            print(f'Object Last Modified :: {LastModified}')
            
            currentDateTime = datetime.utcnow().replace(tzinfo=None)
            print(f'Current DateTime :: {currentDateTime}')
            
            delta = currentDateTime.toordinal() - LastModified.toordinal()
            print(f"Delta Days :: {delta}")
            
            if int(delta) > int(cleanup_schedule):
                print(f'Object {file} is Older than {cleanup_schedule} Days')
                
                print("Initiating Auto Cleanup Process.")
                resp = S3.delete_object(Bucket=str(bucket_name),Key=str(file))
                print(f"Response after delete object operation :: {file}")
                print(f"Object Older than {cleanup_schedule} days Deleted Successfully.")
            else:
                print("Nothing to do here.")
            
    else:
        print("No Objects Available in the Bucket")
