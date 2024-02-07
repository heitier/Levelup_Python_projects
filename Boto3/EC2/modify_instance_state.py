import boto3

def stop_instance (client,instance_ids):
    response = client.stop_instances(
    InstanceIds=instance_ids
    )
    for state in response['StoppingInstances']:
        print(state['CurrentState']['Name'], state['InstanceId'], state['PreviousState']['Name'])

def start_instance (client,instance_ids):
    response = client.start_instances(
    InstanceIds=instance_ids
    )
    for state in response['StartingInstances']:
        print(state['CurrentState']['Name'], state['InstanceId'], state['PreviousState']['Name'])


def reboot_instance (client,instance_ids):
    response = client.reboot_instances(
    InstanceIds=instance_ids
)


def terminate_instance (client,instance_ids):
    response = client.terminate_instances(
    InstanceIds=instance_ids
)
    for state in response['TerminatingInstances']:
     print(state['CurrentState']['Name'], state['InstanceId'], state['PreviousState']['Name'])




ec2 = boto3.client('ec2')
instance_ids = ['i-01a44dc1e8e5b5b3a','i-02800a5fc8306a1cb','i-0e815fc10db0a3d02']
terminate_instance(ec2,instance_ids)

