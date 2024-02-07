import boto3

ec2 = boto3.client('ec2')

response = ec2.create_image(InstanceId='i-08fb2eb3cc650135a' ,Name='test_server' )

print(response['ImageId'])