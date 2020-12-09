#!/bin/bash -e

declare -a regions=("us-east-1" "us-west-2")

for r in "${regions[@]}"
do 
	aws configure set region $r

	python eip_listing.py $r >> resources_output/eip_listing.txt
	python SG_listing.py $r >> resources_output/SG_listing.txt
        python ebs_volumes_listing.py $r >> resources_output/ebs_volumes_listing.txt  
        python EC2_instances_listing.py $r >> resources_output/EC2_instances_listing.txt
        python EC2_snapshots_listing.py $r >> resources_output/EC2_snapshots_listing.txt      
done



