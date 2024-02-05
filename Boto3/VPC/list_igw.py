import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_internet_gateways()

for igw in response['InternetGateways']:
    print(igw['InternetGatewayId'], igw['OwnerId'])
    
    for attachements in igw['Attachments']:
        print(attachements['State'], attachements['VpcId'])
        

# print(response)