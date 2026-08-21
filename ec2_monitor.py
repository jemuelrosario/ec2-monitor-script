import boto3
from datetime import datetime, timezone
from instance import Instance



def obtain_instances():
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()

    instances = []

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances.append(Instance(instance['InstanceId'], instance['State']['Name'], instance['LaunchTime']))

    return instances


def running_time(instance):
    actual_date_UTC = datetime.now(timezone.utc)
    run_time = actual_date_UTC - instance.launch_time  
    return run_time

def check_running_time(instance, threshold):
    run_time = running_time(instance)
    if instance.state == 'running' and run_time  >= threshold:
        return 'This instance has surpassed the maximium running time'
    elif instance.state == 'running' and run_time < threshold:
        return 'Valid running time of the instance'
    else:
        return 'N/A'



