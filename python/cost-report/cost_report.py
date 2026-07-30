#!/usr/bin/env python3
"""AWS Cost Report – retrieves current month's unblended cost per service."""
import boto3
from datetime import datetime

def report():
    ce = boto3.client('ce')
    today = datetime.now().strftime('%Y-%m-%d')
    start = datetime.now().strftime('%Y-%m-01')
    resp = ce.get_cost_and_usage(
        TimePeriod={'Start': start, 'End': today},
        Granularity='MONTHLY',
        Metrics=['UnblendedCost'],
        GroupBy=[{'Type': 'DIMENSION', 'Key': 'SERVICE'}]
    )
    for group in resp['ResultsByTime'][0]['Groups']:
        service = group['Keys'][0]
        amount = group['Metrics']['UnblendedCost']['Amount']
        print(f"{service}: ${amount}")

if __name__ == '__main__':
    report()
