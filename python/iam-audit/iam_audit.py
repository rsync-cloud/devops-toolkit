#!/usr/bin/env python3
"""IAM Audit – lists users with access keys and their last used date."""
import boto3
from datetime import datetime

def audit():
    iam = boto3.client('iam')
    users = iam.list_users()['Users']
    for user in users:
        username = user['UserName']
        keys = iam.list_access_keys(UserName=username)['AccessKeyMetadata']
        for key in keys:
            key_id = key['AccessKeyId']
            last_used = iam.get_access_key_last_used(AccessKeyId=key_id)['AccessKeyLastUsed']
            last_date = last_used.get('LastUsedDate', 'Never')
            if last_date != 'Never':
                last_date = last_date.strftime('%Y-%m-%d')
            print(f"User: {username}, Key: {key_id}, Last Used: {last_date}")

if __name__ == '__main__':
    audit()
