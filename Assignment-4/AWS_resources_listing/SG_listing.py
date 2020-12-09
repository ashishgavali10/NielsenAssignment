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

SG_Details = client.describe_security_groups()

count=1
#pprint(SG_Details)

if sys.argv[1] == "us-east-1":
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("Security groups of region : " + sys.argv[1])
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
elif sys.argv[1] == "us-west-2":
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("Security groups of region : " + sys.argv[1])
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
 

if SG_Details['ResponseMetadata']['HTTPStatusCode'] == 200:
 for each_SG in SG_Details['SecurityGroups']:
  print(count, ", Id : ", each_SG['GroupId'], ", Name : ", each_SG['GroupName']) 
  count=count+1
  
