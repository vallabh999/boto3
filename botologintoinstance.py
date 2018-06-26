#!/usr/bin/env python

import boto3
import botocore
import paramiko

key = paramiko.RSAKey.from_private_key_file("/home/admins/Downloads/boto.pem")
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect/ssh to an instance
try:
    # Here 'ubuntu' is user name and 'instance_ip' is public IP of EC2
    client.connect(hostname="13.127.161.71", username="ubuntu", pkey=key)

    # Execute a command(cmd) after connecting/ssh to an instance

    stdin, stdout, stderr = client.exec_command('./mongo.sh')
    print stdout.read()

    # close the client connection once the job is done
    client.close()
    
except Exception, e:
    print e
