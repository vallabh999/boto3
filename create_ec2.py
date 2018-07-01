#!/usr/bin/env python

import boto3

ec2 = boto3.resource('ec2', region_name='ap-south-1')
instances = ec2.create_instances(
	ImageId='ami-41e9c52e', 
	MinCount=1, 
	MaxCount=1,
	KeyName="boto",
	InstanceType="t2.micro",
        TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'boto'
                },
            ]
        },
    ]
)

for instance in instances:
    print(instance.id, instance.instance_type)
    print(instance.vpc_id)
