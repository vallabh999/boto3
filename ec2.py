#!/usr/bin/env python

import boto3
import time
import paramiko
import json

def start_backup(instance_ip):
    key = paramiko.RSAKey.from_private_key_file(private_key_file)
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=instance_ip, username=user_name, pkey=key)
        print "Connected successfully to MongoBackup instance! Starting backup now...\n"
        stdin, stdout,stderr = client.exec_command('bash mongo.sh')
        if stderr is None:
            print "Backup completed successfully...\n"
        else:
            print "Backup completed with error...\n Errors are below:\n %s" %(stderr)
        client.close()
            
    except:
        print "Could not connect to client, Please check the firewall policy properly and retry again...\n"
        client.close()
            
def stop_instance(instance_id):
    print "Shutting down instance post backup!!!\n This marks the end of script"
    ec2.stop_instances(InstanceIds=instance_id)
    

with open('parameters.json') as json_data:
    stream = json.load(json_data)
    
private_key_file = stream.get('private_key')
user_name        = stream.get('username')


ec2 = boto3.resource('ec2')

instances = ec2.instances.filter(
    #Filters=[{'Name': 'instance-state-name', 'Values': ['stopped', 'running','pending']}])
    Filters = [{'Name': 'instance-state-name', 'Values': ['stopped']},
               {'Name': 'tag:Name', 'Values': ['MongoBackup']}])
for instance in instances:
    #if instance.state[u'Name'] == "stopped":
    #   print("Stopped Instances", instance.id, instance.instance_type,instance.image_id, instance.key_name)
   if (instance.key_name == "boto"):
      ec2.instances.filter(InstanceIds=[instance.id]).start()
      #print 'Now waiting for 80 seconds to start instance'
      #for i in xrange(80,0,-1):
      #    print i
      #    time.sleep(1)
      while true:
        if (instance.state['Name'] == "started":
            print "Instance %s is now started!!! Starting the backup procedure...\n"
            break;
        else:
            print "Instance is still not yet started, waiting for 5 more seconds...\n"
            time.sleep(5)
      start_backup(instance.instance_public_ip_address)
      instance_id = []
      instance_id.append(instance.id)
      stop_instance(instance_id)


            
#after_start = ec2.instances.filter(
#    Filters=[{'Name': 'instance-state-name', 'Values': ['stopped', 'running','pending']}])
#for i in after_start:
#    if i.state[u'Name'] == "running" and i.key_name == "boto":
#       print("Instance state for", i.key_name, "is", i.state[u'Name'])
#       key = paramiko.RSAKey.from_private_key_file("/home/admins/Downloads/boto.pem")
#       client = paramiko.SSHClient()
#       client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


       # Connect/ssh to an instance
#       try:
#           # Here 'ubuntu' is user name and 'instance_ip' is public IP of EC2
#          client.connect(hostname="", username="ubuntu", pkey=key)
#
#           # Execute a command(cmd) after connecting/ssh to an instance
#
#         stdin, stdout, stderr = client.exec_command('./mongo.sh')
#          print stdout.read()

#           # close the client connection once the job is done
#          client.close()

#       except Exception, e:
#          print e

#       print("Backup successfully done, Now instance will stop")
#       if i.state[u'Name'] == "running" and i.key_name == "boto":
#          ec2.instances.filter(InstanceIds=[i.id]).stop()
#          print 'Now waiting for 80 seconds to stop instance'
#          for wait in xrange(80,0,-1):
#              print wait
#              time.sleep(1)

#after_stop = ec2.instances.filter(
#    Filters=[{'Name': 'instance-state-name', 'Values': ['stopped', 'running','pending']}])
#for o in after_stop:
#   if o.state[u'Name'] == "stopped" and o.key_name == "boto":
#      print("Instance state for", o.key_name, "is", o.state[u'Name'])
