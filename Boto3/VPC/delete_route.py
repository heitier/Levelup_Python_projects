import boto3

ec2 = boto3.client('ec2')


routetableid = 'rtb-03d98b8bb0106e735'

response = ec2.delete_route(
    DestinationCidrBlock='0.0.0.0/0',
    RouteTableId=routetableid,
)

print(response)