import boto3

s3 = boto3.client('s3')

bucket = 'kmateta-boto3-02042024'

response = s3.delete_object(
    Bucket = bucket,
    Key='demo_3.txt',
   
)

print(response)