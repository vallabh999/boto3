#!/bin/bash

echo "Logging in DB instance";
ssh -i /home/admins/Downloads/boto.pem ubuntu@13.127.161.71 <<EOF
echo "Proceeding mongo backup";
./mongo.sh
#mongodump -h 13.232.123.63:27017
echo "Done"
EOF
