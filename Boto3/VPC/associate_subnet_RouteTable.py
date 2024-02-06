import boto3

ec2 = boto3.client('ec2')

routeTable = 'rtb-03d98b8bb0106e735'#, 'rtb-0eebffa67ce149509']
subnetid = 'subnet-0bcb9df9dc8f445a2'

for route in routeTable:
    
    associate = ec2.associate_route_table(RouteTableId=routeTable,SubnetId=subnetid)

print(associate['AssociationId'])