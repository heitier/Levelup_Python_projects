import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_route_tables()

for rtid in response['RouteTables']:
    print(rtid['RouteTableId'])
    
    for route in rtid['Routes']:
        print(route['DestinationCidrBlock'], route['GatewayId'],route['Origin'])
        
    

#print(response)