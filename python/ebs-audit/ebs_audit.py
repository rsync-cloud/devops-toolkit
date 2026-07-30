#!/usr/bin/env python3
"""EBS Volume Audit – lists volumes with size, type, and attachment status."""
import boto3

def audit():
    ec2 = boto3.client('ec2')
    volumes = ec2.describe_volumes()
    print(f"{'VolumeId':<20}{'Size(GB)':<10}{'Type':<15}{'State':<15}{'Attachment'}")
    for vol in volumes['Volumes']:
        attach_info = ', '.join([att['InstanceId'] for att in vol['Attachments']]) if vol['Attachments'] else 'None'
        print(f"{vol['VolumeId']:<20}{vol['Size']:<10}{vol['VolumeType']:<15}{vol['State']:<15}{attach_info}")

if __name__ == '__main__':
    audit()
