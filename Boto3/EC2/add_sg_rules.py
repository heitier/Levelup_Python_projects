import boto3

ec2 = boto3.client('ec2')

response = ec2.authorize_security_group_ingress(
    GroupId='sg-0f758bbdf8e1bc7ab',
    IpPermissions=[
        {
            'FromPort': 22,
            'IpProtocol': 'tcp',
            'IpRanges': [
                {
                    'CidrIp': '0.0.0.0/0',
                    'Description': 'SSH access from anywhere',
                },
            ],
            'ToPort': 22,
        },
        {
            'FromPort': 80,
            'IpProtocol': 'tcp',
            'IpRanges': [
                {
                    'CidrIp': '0.0.0.0/0',
                    'Description': 'Http access from anywhere',
                },
            ],
            'ToPort': 80,
        }
        
    ],
)

print(response)