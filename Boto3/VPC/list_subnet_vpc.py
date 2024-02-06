import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_subnets()

for subnet in response['Subnets']:
    print(subnet['AvailabilityZone'] , subnet['SubnetId'], subnet['CidrBlock'])

#print(response)