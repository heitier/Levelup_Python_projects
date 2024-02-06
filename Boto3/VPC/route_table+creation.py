import boto3

cidr_blk = '12.0.2.0/24'
vpc_id = 'vpc-0fd371ecdf3c0a292'

ec2 = boto3.client('ec2')

rt = ec2.create_route_table(VpcId=vpc_id)

print(rt['RouteTable']['RouteTableId'])
    
    