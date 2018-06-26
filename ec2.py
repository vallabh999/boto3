#!/usr/bin/env python

import boto3
import time
import botocore
import paramiko

ec2 = boto3.resource('ec2')

instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['stopped', 'running','pending']}])
for instance in instances:
    if instance.state[u'Name'] == "stopped":
       print("Stopped Instances", instance.id, instance.instance_type,instance.image_id, instance.key_name)
       if instance.key_name == "boto":
          ec2.instances.filter(InstanceIds=[instance.id]).start()
          print 'Now waiting for 80 seconds to start instance'
          for i in xrange(80,0,-1):
              print i
              time.sleep(1)



after_start = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['stopped', 'running','pending']}])
for i in after_start:
    if i.state[u'Name'] == "running" and i.key_name == "boto":
       print("Instance state for", i.key_name, "is", i.state[u'Name'])
       key = paramiko.RSAKey.from_private_key_file("/home/admins/Downloads/boto.pem")
       client = paramiko.SSHClient()
       client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


       # Connect/ssh to an instance
       try:
           # Here 'ubuntu' is user name and 'instance_ip' is public IP of EC2
          client.connect(hostname="", username="ubuntu", pkey=key)

           # Execute a command(cmd) after connecting/ssh to an instance

          stdin, stdout, stderr = client.exec_command('./mongo.sh')
          print stdout.read()

           # close the client connection once the job is done
          client.close()

       except Exception, e:
          print e

       print("Backup successfully done, Now instance will stop")
       if i.state[u'Name'] == "running" and i.key_name == "boto":
          ec2.instances.filter(InstanceIds=[i.id]).stop()
          print 'Now waiting for 80 seconds to stop instance'
          for wait in xrange(80,0,-1):
              print wait
              time.sleep(1)

after_stop = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['stopped', 'running','pending']}])
for o in after_stop:
   if o.state[u'Name'] == "stopped" and o.key_name == "boto":
      print("Instance state for", o.key_name, "is", o.state[u'Name'])
