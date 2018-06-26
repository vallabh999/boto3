#!/usr/bin/env python

import boto3
import time
<<<<<<< HEAD
session = boto3.Session()

ec2 = session.resource('ec2')
instances = ec2.instances.filter(
             Filters =[{'Name': 'instance-state-name', 'Values': ['running','stopped']}])

for i in instances:
    print(i.id, i.instance_type, i.vpc.id, i.subnet.id, i.state[u'Name'], i.tags[0][u'Key'], i.tags[0][u'Value'])
    if (i.state[u'Name'] == "running"): 
       status = ec2.instances.filter(InstanceIds=[i.id]).stop()
       print(i.id,i.state[u'Name'])
=======

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
>>>>>>> e85399455b9c3bab01965d3429390b7dfb992545
