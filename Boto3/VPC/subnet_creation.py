import boto3

cidr_blk = '12.0.1.0/24'
vpc_id = 'vpc-0fd371ecdf3c0a292'

ec2 = boto3.client('ec2')

subnet = ec2.create_subnet(CidrBlock= cidr_blk, VpcId=vpc_id)

print(subnet['Subnet']['SubnetId'])