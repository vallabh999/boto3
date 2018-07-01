#!/usr/bin/env python

import boto3

client = boto3.client('ec2')

resp = client.describe_instances()

for reservation in resp['Reservations']:
    for instance in reservation['Instances']:
        print("Instance id is {} ".format(instance['InstanceId']),
              "Instance Type is {}".format(instance['InstanceType']),
              "Instance Keyname is {}".format(instance['KeyName']))
