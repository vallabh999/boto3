#!/bin/bash

# Initialization of variables

HOST=""
PORT="27017"
USERNAME=""
PASSWORD=""
Bk_PATH=/tmp/mongodump
TODAYS_DATE=`date +%Y%m%d`
FILE_NAME="mongodump.$TODAYS_DATE"
Final_Path=$Bk_PATH/$TODAYS_DATE
MONGO_DUMP_BIN_PATH=`which mongodump`
TAR_BIN_PATH=`which tar`
s3_bucket="vallabh9886304569000"
s3_check_bucket=`aws s3 ls | grep $s3_bucket`

# Check the backup folder exists, if not create it
if [[ -d $Bk_PATH ]] && [[ -d $Final_Path ]]
	then
	echo "$Bk_PATH and $Final_Path Already Exists"
        echo "Backup in process........!"
	else
        cd $Bk_PATH
	mkdir $TODAYS_DATE && echo "$Bk_PATH created"
        mkdir $Final_Path && echo "$Final_Path is created"

fi

# Check username and password and take backup of mongo database

if [ "$USERNAME" != "" -a "$PASSWORD" != "" ]; then 
	$MONGO_DUMP_BIN_PATH --host $HOST:$PORT -u $USERNAME -p $PASSWORD --out $Final_Path >> /dev/null
else 
	$MONGO_DUMP_BIN_PATH --host $HOST:$PORT --out $Final_Path >> /dev/null
fi

# Check for directory created, save file name with present date and tar 
if [[ -d $Final_Path ]]; then
		cd $Bk_PATH	
		#then make it todays date
		if [[ "$FILE_NAME" == "" ]]; then
			FILE_NAME="$TODAYS_DATE"
		fi
		$TAR_BIN_PATH -czf $FILE_NAME.tar.gz $Final_Path >> /dev/null

		if [[ -f "$FILE_NAME.tar.gz" ]]; then
			echo "=> Success: `du -sh $FILE_NAME.tar.gz` in "; echo
                        find $Bk_PATH -type f -mtime +7 -exec rm -r {} \;

         		if [[ -d "$Final_Path" ]]; then
				rm -rf "$Final_Path"
				echo "$Final_Path deleted" 
         		fi
		else
			 echo -en "!!!=> Failed to create backup file: $BACKUP_PATH/$FILE_NAME.tar.gz \n";
		fi

fi

if [[ $s3_check_bucket ]]; then
   echo "Bucket Already Exist"
else
   echo "Bucket not Exist, Creating $s3_bucket"
   aws s3 mb s3://$s3_bucket
fi

#Upload backup file to s3 bucket
if [[ $s3_bucket ]]; then
   echo "Transfering Backup to $s3_bucket" 
   aws s3 cp /tmp/mongodump/* s3://$s3_bucket/
   echo "Succes:!!!"
else
   echo "Transfer Failed"
fi




