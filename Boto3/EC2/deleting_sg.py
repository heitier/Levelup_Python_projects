import boto3

ec2 = boto3.client('ec2')

response = ec2.delete_security_group(
    GroupId='sg-0f758bbdf8e1bc7ab',
)

print(response)