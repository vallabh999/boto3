#!/usr/bin/env python

import boto3
import time
session = boto3.Session()

ec2 = session.resource('ec2')
instances = ec2.instances.filter(
             Filters =[{'Name': 'instance-state-name', 'Values': ['running','stopped']}])

#for i in instances:
  #  print("Instance ID:", i.id, "Type", i.instance_type, "VPC",i.vpc.id, "Subnet-id",i.subnet.id) 
#    print(i.id, i.instance_type, i.vpc.id, i.subnet.id, i.state[u'Name'], i.tags[0][u'Key'], i.tags[0][u'Value'])
    #print(i.state[u'Name'], i.tags[0][u'Value'])
 #   if (i.state[u'Name'] == "running"): 
  #    status = ec2.instances.filter(InstanceIds=[i.id]).stop()
   #    print(i.id,i.state[u'Name'])

for i in instances:
#   print("Instance ID:", i.id, "Type", i.instance_type, i.private_ip_address, i.private_dns_name, i.image_id, i.key_pair.name)
   if (i.image_id == "ami-41e9c52e"):
      status = ec2.instances.filter(InstanceIds=[i.id]).stop()
      time.sleep(60)
     # status = ec2.instances.filter(InstanceIds=[i.id]).stop()
      if(i.state[u'Name'] == "running"):
        print("Running")
      elif (i.state[u'Name'] == "stopped"):
       print("Stopped") 
      else:
       print("Went Wrong")
      


  
