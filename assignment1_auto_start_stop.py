"""
Assignment 1: Automated Instance Management Using AWS Lambda and Boto3

Objective: In this assignment, you will gain hands-on experience with AWS Lambda and Boto3, Amazon's SDK for Python. You will create a Lambda function that will automatically manage EC2 instances based on their tags.

Task: You're tasked to automate the stopping and starting of EC2 instances based on tags. Specifically:

1. Setup:

   - Create two EC2 instances.

   - Tag one of them as `Auto-Stop` and the other as `Auto-Start`.

2. Lambda Function Creation:

   - Set up an AWS Lambda function.

   - Ensure that the Lambda function has the necessary IAM permissions to describe, stop, and start EC2 instances.

3. Coding:

   - Using Boto3 in the Lambda function:

     - Detect all EC2 instances with the `Auto-Stop` tag and stop them.

     - Detect all EC2 instances with the `Auto-Start` tag and start them.

4. Testing:

   - Manually invoke the Lambda function.

   - Confirm that the instance tagged `Auto-Stop` stops and the one tagged `Auto-Start` starts.

Instructions:

1. EC2 Setup:

   - Navigate to the EC2 dashboard and create two new t2.micro instances (or any other available free-tier type).

   - Tag the first instance with a key `Action` and value `Auto-Stop`.

   - Tag the second instance with a key `Action` and value `Auto-Start`.

2. Lambda IAM Role:

   - In the IAM dashboard, create a new role for Lambda.

   - Attach the `AmazonEC2FullAccess` policy to this role. (Note: In a real-world scenario, you would want to limit permissions for better security.)

3. Lambda Function:

   - Navigate to the Lambda dashboard and create a new function.

   - Choose Python 3.x as the runtime.

   - Assign the IAM role created in the previous step.

   - Write the Boto3 Python script to:

     1. Initialize a boto3 EC2 client.
     2. Describe instances with `Auto-Stop` and `Auto-Start` tags.
     3. Stop the `Auto-Stop` instances and start the `Auto-Start` instances.
     4. Print instance IDs that were affected for logging purposes.

4. Manual Invocation:

   - After saving your function, manually trigger it.

   - Go to the EC2 dashboard and confirm that the instances' states have changed according to their tags.
"""

import boto3
import json

region = 'us-east-2'
# Define the tag key and value to identify instances to be stopped
stop_tag_key = 'Auto-Stop'
start_tag_key = 'Auto-Start'
tag_value = 'TRUE'
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    # TODO implement
    #! Creating EC2 client using boto3
    instances = ec2.describe_instances()
    print(f'Instances :: {instances}')
    # Iterate through reservations and instances
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            #! Check if the 'Auto-Stop' tag exists and its value is 'TRUE'
            for tag in instance.get('Tags', []):
                if tag['Key'] == stop_tag_key and tag['Value'] == tag_value:
                    instance_id = instance['InstanceId']
                    
                    # Check the current state of the instance
                    instance_state = instance['State']['Name']
                    print(f'Instance State - STAGE 1 :: {instance_state} <> TAG VALUE {stop_tag_key}')
                    # If the instance is running, stop it
                    if instance_state == 'running':
                        ec2.stop_instances(InstanceIds=[instance_id])
                        print(f"Stopped EC2 instance {instance_id}")
                    else:
                        print(f"EC2 instance {instance_id} is not in a 'running' state, skipping.")
                else:
                    print(f"No matching instances with the {stop_tag_key}:{tag_value} tag found.")
                    
                #! Check if the 'Auto-Stop' tag exists and its value is 'TRUE'
                if tag['Key'] == start_tag_key and tag['Value'] == tag_value:
                    instance_id = instance['InstanceId']
                    
                    # Check the current state of the instance
                    instance_state = instance['State']['Name']
                    print(f'Instance State - STAGE 2 :: {instance_state} <> <> TAG VALUE {start_tag_key}')
                    # If the instance is running, stop it
                    if instance_state == 'stopped':
                        ec2.start_instances(InstanceIds=[instance_id])
                        print(f"Started EC2 instance {instance_id}")
                    else:
                        print(f"EC2 instance {instance_id} is not in a 'stopped' state, skipping.")
                else:
                    print(f"No matching instances with the {start_tag_key}:{tag_value} tag found.")
    
    #! 'body': json.dumps('Hello from Lambda Function! - Kinnar Chowdhury')
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps(response)
    # }
