import boto3

ec2 = boto3.client('ec2')
file_name = 'my-boto3-key-pair'
response = ec2.create_key_pair(
    KeyName='my-boto3-key-pair',
)

with open(file_name, 'w') as f:
    f.write(response['KeyMaterial'])
