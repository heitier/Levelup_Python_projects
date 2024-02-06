import boto3

ec2 = boto3.client('ec2')

igw = ec2.create_internet_gateway()

print(igw['InternetGateway']['InternetGatewayId'])