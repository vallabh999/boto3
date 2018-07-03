#!/usr/bin/env python

import boto3
import time

ec2 = boto3.resource('ec2')
instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['stopped', 'running','pending']}])

for instance in instances:
    print "All instances in mumbai region are {}".format(instance.id), "With Instance state {}".format(instance.state[u'Name'])
    if(instance.key_name == "boto"):
        ec2.instances.filter(InstanceIds=[instance.id]).start()
        print("Starting instance {}".format(instance.tags[0][u'Value']))
        time.sleep(200)
        print "Instance started with keyname {}".format(instance.key_name), "and Instance ID {}".format(instance.id)
        print("Public Ip for the started instance {} is {}".format(instance.tags[0][u'Value'], instance.public_ip_address))
        print("Now stopping instance {}".format(instance.tags[0][u'Value']))
        ec2.instances.filter(InstanceIds=[instance.id]).stop()
        time.sleep(120)
        print("The state of {} is {}".format(instance.tags[0][u'Value'], instance.state[u'Name']))
