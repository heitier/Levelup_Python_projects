import boto3

ec2 = boto3.client('ec2')

subnet_id = 'subnet-0bcb9df9dc8f445a2'

response = ec2.delete_subnet(
    SubnetId=subnet_id,)

