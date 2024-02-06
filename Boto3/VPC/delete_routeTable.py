import boto3

ec2 = boto3.client('ec2')

routeTable_Id = 'rtb-03d98b8bb0106e735'

response = ec2.delete_route_table(
    RouteTableId=routeTable_Id,
)

print(response)
