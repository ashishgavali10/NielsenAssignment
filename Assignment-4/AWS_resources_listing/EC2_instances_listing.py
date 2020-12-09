import sys
import boto3
from pprint import pprint
import dotenv
import os
from datetime import datetime, timedelta, timezone

# load the environment variables
dotenv.load_dotenv()

count=1

ec2 = boto3.resource('ec2')

if sys.argv[1] == "us-east-1":
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("Processing instances for region : " + sys.argv[1])
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
elif sys.argv[1] == "us-west-2":
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("Processing instances for region : " + sys.argv[1])
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

instance_iterator=ec2.instances.all()

for instance in ec2.instances.all():
    print (count)
    print("Instance ID : "+instance.id+" , State: "+instance.state['Name'])
    print("------------------------------------------------------------------------------------------------------")
    count=count+1
