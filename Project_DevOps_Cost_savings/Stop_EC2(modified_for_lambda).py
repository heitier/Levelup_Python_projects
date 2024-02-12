import boto3

def lambda_handler(event, context):
    
     # Creating an EC2 client using boto3.
    ec2 = boto3.client('ec2')
    
     # List of instance IDs to be stopped
    instance_ids = ['i-079a22354687ef95a', 'i-0a5fc454fc9ab81b1', 'i-05d8308e6f4d090e5', 'i-09c38979862ce0844']
    
     # Sending a request to stop instances using the provided ec2 and instance IDs
    response = ec2.stop_instances(InstanceIds=instance_ids)
    instances_info = []
   
     # Iterating through the response to print the current and previous states of each instance
    for state in response['StoppingInstances']:
        instance = state['InstanceId']
        current_state = state['CurrentState']['Name']
        previous_state = state['PreviousState']['Name']
        instances_info.append(instance)

    print('The following Instances', ', '.join(instances_info), 'are', current_state,
              '. Their Previous state was', previous_state)

    return {
        'statusCode': 200,
        'body':"Instances stopped successfully."
    }
