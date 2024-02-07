import boto3

ec2 = boto3.client('ec2')

description = 'Security group made in boto3 to experiment'
groupName = 'Boto3 Security group'
vpcId = 'vpc-0b33c08c1de906dbf'

response = ec2.create_security_group(
    Description= description,
    GroupName= groupName ,
    VpcId= vpcId
)

print(response['GroupId'])