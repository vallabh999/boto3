# boto3
Following are the tasks done by the code - 

1. This code starts the ec2 instance/backupserver where backup to be carried out.
2. Creates a dir in /tmp if not available and takes the backup(mongo/sql) from the DB instance.
3. Once the backup is done in instance it uploads the created tar.gz file to s3 bucket.
4. On succesful upload the instance is stopped.

Note :
- AWSCLI to be configured and mongo-clinets/mongod to be installed in backup server/instance.
- Security groups to be updates as per requirements for port bindings.
