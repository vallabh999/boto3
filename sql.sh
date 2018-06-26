#!/bin/sh

#backup folder within the server where backup files are stored
BAK_DEST=~/backup

#database credentials
DB_USERNAME=[username]
DB_PASSWORD=[password]
DB_SCHEMA=[schema]

#folders for backup, can be comma separated for multiple folders
BAK_SOURCES=[folder_A, folder_B]

#s3 bucket name that contains backup
S3_BUCKET=[s3_bucket]

#number of days to keep archives
KEEP_DAYS=7

#script variables
BAK_DATE=`date +%F`
BAK_DATETIME=`date +%F-%H%M`
BAK_FOLDER=${BAK_DEST}/${BAK_DATE}
BAK_DB=${BAK_FOLDER}/db-${BAK_DATETIME}

#CREATE folder where backup database is to be place
echo 'Creating database back up ' ${BAK_FOLDER}
mkdir ${BAK_FOLDER}

#PERFORM mySQL Database DUMP
echo 'Creating archive file ' ${BAK_DB}'.tar.gz Pls wait...'
mysqldump -u ${DB_USERNAME} -p${DB_PASSWORD} ${DB_SCHEMA} > ${BAK_DB}.sql
tar czPf ${BAK_DB}.tar.gz ${BAK_DB}.sql

echo 'Copying database backup to S3 ...'
s3cmd put ${BAK_DB}.tar.gz s3://${S3_BUCKET}/backup/db/db-${BAK_DATETIME}.tar.gz

#ARCHIVING FILES / FOLDER
echo 'Archiving files and folders...'

FOLDERS=$(echo $BAK_SOURCES | tr "," "\n")
i=0
for F in $FOLDERS
do
  echo 'Archiving ' ${F} '...'
  i=`expr ${i} + 1`
  tar czPf ${BAK_FOLDER}/FILE_${i}_${BAK_DATETIME}.tar.gz ${F}
  s3cmd put ${BAK_FOLDER}/FILE_${i}_${BAK_DATETIME}.tar.gz s3://${S3_BUCKET}/backup/files/FILE_${i}_${BAK_DATETIME}.tar.gz
done

#DELETE FILES OLDER THAN 7 days
echo 'Deleting backup older than '${KEEP_DAYS}' days'
find ${BAK_FOLDER} -type f -mtime +${KEEP_DAYS} -name '*.gz' -execdir rm -- {} \;
