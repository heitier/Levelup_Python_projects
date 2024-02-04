import boto3

# creating a S3 Bucket

s3 = boto3.client('s3')

response = s3.create_bucket(
    Bucket='kmateta-boto3-02042024'
)

print(response)
