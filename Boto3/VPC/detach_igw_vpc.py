import boto3

ec2 = boto3.client('ec2')

igw_id = 'igw-09ac4507bbc9d6a2c'
vpcid = 'vpc-0fd371ecdf3c0a292'

response = ec2.detach_internet_gateway(
    InternetGatewayId=igw_id,
    VpcId=vpcid,
)

print(response)