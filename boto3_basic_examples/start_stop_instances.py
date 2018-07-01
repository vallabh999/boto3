#!/usr/bin/env python

import boto3
import time

client = boto3.client('ec2')
response = client.start_instances(
    InstanceIds=[
        'i-xxxxxxxxx', 'i-xxxxxxxx',
    ],
)

for instance in response['StartingInstances']:
    time.sleep(60)
    print("Instance with {} id is started".format(instance['InstanceId']))
    print("Instance with current state {} is".format(instance['CurrentState']))
    print("Instance with previous state {} is".format(instance['PreviousState']))


response = client.stop_instances(
    InstanceIds=[
        'i-xxxxxxxxxxxxxxxxxx','i-xxxxxxxxxxxxxxxx',
    ],
)

for instance in response['StoppingInstances']:
    time.sleep(60)
    print("Instance with {} id is stopped".format(instance['InstanceId']))
    print("Instance with current state {} is".format(instance['CurrentState']))
    print("Instance with previous state {} is".format(instance['PreviousState']))

response = client.terminate_instances(
    InstanceIds=[
        'i-xxxxxxxxxxxxxxx','i-xxxxxxxxxxxxx',
    ],
)

for instance in response['TerminatingInstances']:
    time.sleep(60)
    print("Instance with {} ids is terminated".format(instance['InstanceId']))
    print("Instance with current state {} is".format(instance['CurrentState']))
    print("Instance with previous state {} is".format(instance['PreviousState']))
