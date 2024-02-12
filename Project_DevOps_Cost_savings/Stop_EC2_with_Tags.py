import boto3

def lambda_handler(event, context):
    
     # Creating an EC2 client using boto3.
    ec2 = boto3.client('ec2')
    
    instances_info = []
    instance_ids = []
    
    response_list = ec2.describe_instances()
    
    for reservations in response_list['Reservations']:
        for instances in reservations['Instances']:
            for Tag in instances['Tags']:
                if Tag['Key'] == 'Environment':
                    if Tag['Value'] == 'DEV':
                        instance_ids.append(instances['InstanceId'])

    response = ec2.stop_instances(InstanceIds=instance_ids)
     # Iterating through the response to print the current and previous states of each instance
    for state in response['StoppingInstances']:
        instance = state['InstanceId']
        current_state = state['CurrentState']['Name']
        previous_state = state['PreviousState']['Name']
        instances_info.append(instance)

    print('The following Instances', ', '.join(instances_info), 'are', current_state,
              '.Their Previous state was', previous_state)

    return {
        'statusCode': 200,
        'body':"Instances stopped successfully."
        }