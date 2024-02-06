import boto3

ec2 = boto3.client('ec2')

vpc_id = 'vpc-0fd371ecdf3c0a292'

response = ec2.delete_vpc(
    VpcId=vpc_id,
)

print(response)