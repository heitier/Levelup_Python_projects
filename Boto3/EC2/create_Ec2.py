import boto3

ec2 = boto3.client('ec2')

response = ec2.run_instances(
    ImageId='ami-0cbf60eab3a02b214',
    InstanceType='t2.micro',
    KeyName='my-boto3-key-pair',
    MaxCount=1,
    MinCount=1,
    SecurityGroupIds=[
        'sg-0f758bbdf8e1bc7ab',
    ],
    
)

print(response['Instances'][0]['InstanceId'])