import boto3

ec2 = boto3.client('ec2')

igw_id = 'igw-09ac4507bbc9d6a2c'


response = ec2.delete_internet_gateway(
    InternetGatewayId=igw_id,
)

print(response)