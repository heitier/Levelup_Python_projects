import boto3

s3 =boto3.client('s3')

# with open('test_text.txt', 'wb') as data:
#     s3.download_fileobj('kmateta-boto3-02042024', 'test_text.txt', data)
    

s3.download_file('kmateta-boto3-02042024', 'test_text.txt', '/home/ec2-user/environment/Levelup_Python_projects/Boto3/test_text_modified2.txt')