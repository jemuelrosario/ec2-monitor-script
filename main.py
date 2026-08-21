from ec2_monitor import obtain_instances, running_time, check_running_time
from datetime import timedelta

threshold = timedelta(hours=1)

instances = obtain_instances()

for instance in instances:
    print(f"Instance ID: {instance.instance_id}\nInstance State: {instance.state}")

    if instance.state == 'running':
        print (f'Instance Running Time: {running_time(instance)}')
    else:
        print ('Instance Running Time: N/A')
    message = check_running_time(instance, threshold) 
    print(message + '\n')