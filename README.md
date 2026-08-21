# EC2-Monitor-Script
A python script that helps monitoring the running time and state of AWS EC2 instances, and alerts when an instance exceeds a specified running time threshold.

## How it works
This script collects information of existing resources in your AWS account, what it does is ensure that your resources don't exceed a limit time of utilization so you don't waste money, it is like ensuring your sons don't leave the lights on when leaving the house, this script does the same!

## Installation and Configuration

### Requirements
- AWS Account
- IAM user with permissions (AmazonEC2ReadOnlyAccess)
- Python installed in your computer
- boto3 installed 

### Steps
1. Clone repository
```
git clone https://github.com/jemuelrosario/ec2-monitor-script.git
```
2. Install boto3
```
pip install boto3
``` 
3. Configure credentials with aws configure
```
aws configure
```

## How to run it
```
python main.py
```
When you run it will show you details of your EC2 instance like, ID, state, running time and alerts if any of your instances exceed the threshold.

## Project Structure

```
ec2-monitor-script/
├── instance.py        # Has the structure of the instance class that stores important information of these.
├── ec2_monitor.py     # Has all the functions to validate, display and manage logic to obtain the information.
└── main.py            # This file obtains your instances and initializes important variables like the threshold which you can edit to your choice, also displays all the instances information.
```

## Possible extensions
1. An upgrade that permits the script to send you an email if any of the instances exceed the limit running time.
2. 
