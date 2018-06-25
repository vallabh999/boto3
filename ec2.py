#!/usr/bin/env python

import boto3
import time

ec2 = boto3.resource('ec2')

instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['stopped', 'running','pending']}])
for instance in instances:
    if instance.state[u'Name'] == "stopped":
       print("Stopped Instances", instance.id, instance.instance_type,instance.image_id, instance.key_name)
       if instance.key_name == "boto3":
          ec2.instances.filter(InstanceIds=[instance.id]).start()
          print 'Now waiting for 180 seconds to start instance'
          for i in xrange(120,0,-1):
              print i
              time.sleep(1)



after_start = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['stopped', 'running','pending']}])
for i in after_start:
    if i.state[u'Name'] == "running" and i.key_name == "boto3":
       print("Instance state for", i.key_name, "is", i.state[u'Name'])
