import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_images(Owners = ['self'])


# for images in response['Images']:
#     if images['Architecture'] == 'arm64':

#          print(images['ImageId'],images['CreationDate'],images['Architecture'],images['Name'])
for images in response['Images']:
         
    print(images['ImageId'],images['CreationDate'],images['Architecture'],images['Name'])
