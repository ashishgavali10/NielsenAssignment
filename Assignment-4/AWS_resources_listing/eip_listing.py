import sys
import boto3
from pprint import pprint
import dotenv
import os
from datetime import datetime, timedelta, timezone

client = boto3.client('ec2')

count=1

addresses_not_associated = list()
addresses_to_release = list()
addresses_to_exclude = list()
#Processing different reserved Elastic IPs as per region
if sys.argv[1] == "us-east-1":
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("Processing addresses for region : " + sys.argv[1])
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    reserved_eips_file = open("../../input_files/reserved-eips-nv.txt")
elif sys.argv[1] == "us-west-2":
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("Processing addresses for region : " + sys.argv[1])
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    reserved_eips_file = open("../../input_files/reserved-eips-or.txt")

for reserved_eip in reserved_eips_file:
    addresses_to_exclude.append(reserved_eip.replace("\n", ""))
# call describe_addresses() method of client to get the details of all addresses used in the given region
address_detail = client.describe_addresses()

# process each address scanned in address_detail
if address_detail['ResponseMetadata']['HTTPStatusCode'] == 200:
    for each_address in address_detail['Addresses']:
        # some logging to make things clear about the addresses in your existing system
       
        print(count, ", Working for address : ", each_address['PublicIp'])
        count=count+1
          
        # figuring out the unassociated ips
        # the volumes which do not have 'AssociationIdA' are considered to be available for release
        if ((each_address.get('AssociationId',"None")) == 'None') :
            addresses_not_associated.append([each_address['PublicIp'],each_address.get('AllocationId',"None"),each_address.get('Domain',"None")])
print("--------------------------------------------")
print("---------------------Addresses not associated-----------------------")
pprint(addresses_not_associated)
# separating processing for different domain (scope) of EIPs. Ec2-classic Eips need publicIp to be releases. VPC scoped EIPs need allocation id to be released

for row in range(len(addresses_not_associated)):
     if (addresses_not_associated[row][0]) in addresses_to_exclude: 
        print("Excluding address " + addresses_not_associated[row][0])
     else:
        if (addresses_not_associated[row][2] == 'standard'):
           print("===================================In standard if block==========================================") 
           print("Releasing address " + addresses_not_associated[row][0] + " of domain " + addresses_not_associated[row][2])
        elif (addresses_not_associated[row][2] == 'vpc'):
           print("==================================In vpc if block================================================")
           print("Releasing address " + addresses_not_associated[row][0] + " of domain " + addresses_not_associated[row][2])
        else:
          print("Different Domain, Please check address " + addresses_not_associated[row][0] + " for releasing")

