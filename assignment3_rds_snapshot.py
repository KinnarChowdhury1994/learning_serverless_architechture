"""
Assignment 3: Automated RDS Snapshot Using AWS Lambda and Boto3

Objective: To become familiar with automating RDS tasks using AWS Lambda and Boto3. You will create a Lambda function that takes a snapshot of an RDS instance.

Task: Automate the creation of a snapshot for a specific RDS instance at regular intervals.

Instructions:

1. RDS Setup:

   - Navigate to the RDS dashboard and create a new RDS instance (use the free tier, if available).

   - Note the name of the instance.

2. Lambda IAM Role:

   - In the IAM dashboard, create a new role for Lambda.

   - Attach the `AmazonRDSFullAccess` policy to this role. (Note: Always practice the principle of least privilege in real-world scenarios.)

3. Lambda Function:

   - Navigate to the Lambda dashboard and create a new function.

   - Choose Python 3.x as the runtime.

   - Assign the IAM role created in the previous step.

   - Write the Boto3 Python script to:

     1. Initialize a boto3 RDS client.
     2. Take a snapshot of the specified RDS instance.
     3. Print the snapshot ID for logging purposes.

4. Event Source (Bonus):

   - Attach an event source, like Amazon CloudWatch Events, to trigger the Lambda function every day (or as per your preferred frequency).

5. Manual Invocation:

   - After saving your function, manually trigger it (or wait for the scheduled trigger).

   - Go to the RDS dashboard and confirm that a snapshot has been taken.
"""
