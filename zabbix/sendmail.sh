#!/bin/bash
 
to=$1
subject=$2
body=$3
FILE=/tmp/mailtmp.txt

echo "$body">/tmp/mailtmp.txt
dos2unix -k $FILE

cat <<EOF | mail -s "$subject" "$to"
`cat $FILE`
EOF
