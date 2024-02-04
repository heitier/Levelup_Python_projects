import boto3

s3 = boto3.client('s3')

response = s3.generate_presigned_url('get_object', Params={'Bucket': 'kmateta-boto3-02042024', 'Key': 'demo_3.txt'},ExpiresIn=300)

print(response)