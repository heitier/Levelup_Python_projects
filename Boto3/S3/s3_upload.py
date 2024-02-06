import boto3

s3 = boto3.client('s3')

# with open('/home/ec2-user/environment/Levelup_Python_projects/demo.txt', 'rb') as file:
#     s3.put_object(Bucket="kmateta-boto3-02042024", Key="demo_3.txt", Body=file, ContentType="text/plain")
# file.close

with open('/home/ec2-user/environment/Levelup_Python_projects/test_text.txt', 'rb') as file:
    s3.put_object(Bucket="kmateta-boto3-02042024", Key="test_text.txt", Body=file, ContentType="text/plain")
file.close

# s3.upload_file('/Levelup_Python_projects/demo.txt', 'kmateta-boto3-02042024', 'demo.txt', ExtraArgs={'ContentType':'text/plain'})

# s3.put_object(Bucket="kmateta-boto3-02042024", Key="demo_2.txt", Body="/Levelup_Python_projects/demo.txt", ContentType="text/plain")