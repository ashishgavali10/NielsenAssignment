import sys
import boto3
from pprint import pprint
import dotenv
import os
from datetime import datetime, timedelta, timezone

# load the environment variables
dotenv.load_dotenv()

# create boto3 client for ec2
client = boto3.client('ec2')

# call describe_volumes() method of client to get the details of all ebs volumes in given region
# if you have large number of volumes then get the volume detail in batch by using nextToken and process accordingly
volume_detail = client.describe_volumes()

count=1

if sys.argv[1] == "us-east-1":
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("Processing volumes for region : " + sys.argv[1])
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
elif sys.argv[1] == "us-west-2":
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("Processing volumes for region : " + sys.argv[1])
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

# process each volume in volume_detail
if volume_detail['ResponseMetadata']['HTTPStatusCode'] == 200:
    for each_volume in volume_detail['Volumes']:
        # some logging to make things clear about the volumes in your existing system
      
        print(count,", Working for volume with volume_id: ", each_volume['VolumeId'])
        print("Volume creation date: ", each_volume['CreateTime'])
        print("State of volume: ", each_volume['State'])
        print("Attachment state length: ", len(each_volume['Attachments']))
        print(each_volume['Attachments'])
        print("-----------------------------------------------------------------------------")
        count=count+1
   
