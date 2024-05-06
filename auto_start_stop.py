import boto3
import json

region = 'us-east-2'
# Define the tag key and value to identify instances to be stopped
stop_tag_key = 'Auto-Stop'
start_tag_key = 'Auto-Start'
tag_value = 'TRUE'

def lambda_handler(event, context):
    # TODO implement
    #! Creating EC2 client using boto3
    ec2 = boto3.client('ec2', region_name=region)
    response = ec2.describe_instances()
    print(f'Instances :: {instances}')
    # Iterate through reservations and instances
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            # Check if the 'AutoShutdown' tag exists and its value is 'true'
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
                    print(f"No matching instances with the {tag_key}:{tag_value} tag found.")
                    
                if tag['Key'] == start_tag_key and tag['Value'] == tag_value:
                    instance_id = instance['InstanceId']
                    
                    # Check the current state of the instance
                    instance_state = instance['State']['Name']
                    print(f'Instance State - STAGE 2 :: {instance_state} <> <> TAG VALUE {start_tag_key}')
                    # If the instance is running, stop it
                    if instance_state == 'stopped':
                        ec2.start_instances(InstanceIds=[instance_id])
                        print(f"Stopped EC2 instance {instance_id}")
                    else:
                        print(f"EC2 instance {instance_id} is not in a 'running' state, skipping.")
                else:
                    print(f"No matching instances with the {tag_key}:{tag_value} tag found.")
    
    #! 'body': json.dumps('Hello from Lambda Function! - Kinnar Chowdhury')
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps(response)
    # }
