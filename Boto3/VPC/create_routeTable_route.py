import boto3

ec2 = boto3.client('ec2')

gateway = 'igw-09ac4507bbc9d6a2c'
routetableid = 'rtb-03d98b8bb0106e735'


response = ec2.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=gateway,
    RouteTableId=routetableid,
)

print(response)