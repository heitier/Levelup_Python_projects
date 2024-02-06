import boto3

ec2 = boto3.client('ec2')


response = ec2.describe_vpcs()

for vpc in response['Vpcs']:
    print(vpc['VpcId'],vpc['CidrBlock'],vpc['State'])


#print(response)