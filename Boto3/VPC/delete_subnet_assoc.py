import boto3

ec2 = boto3.client('ec2')

route_table_id = 'rtb-03d98b8bb0106e735'

response = ec2.describe_route_tables(RouteTableIds =[route_table_id])


for association in response['RouteTables'][0]['Associations']:
    if not association['Main']:
        associate_id = association['RouteTableAssociationId']
        print(associate_id)
        ec2.disassociate_route_table(
            AssociationId=associate_id,)