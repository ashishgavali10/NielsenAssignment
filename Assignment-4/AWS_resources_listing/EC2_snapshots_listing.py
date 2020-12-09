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

count=1

if sys.argv[1] == "us-east-1":
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("Processing snapshots for region : " + sys.argv[1])
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
elif sys.argv[1] == "us-west-2":
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("Processing snapshots for region : " + sys.argv[1])
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

for each_snap in client.describe_snapshots(OwnerIds=['030845907404'])['Snapshots']:

   print(count)
   print("Snapshot Id : "+each_snap['SnapshotId'] +" ,Attached volume ID : "+each_snap['VolumeId'])
   print("Description : "+each_snap['Description'])
   print("Creation Date :")
   print(each_snap['StartTime'])
   count=count+1
   print("-------------------------------------------------------------------------------------------------")
