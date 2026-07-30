#!/usr/bin/env python3
"""
AWS Cleanup Utility
Deletes unattached EBS volumes and old snapshots older than a specified number of days.
"""
import boto3
import argparse
from datetime import datetime, timezone, timedelta

def delete_unattached_volumes(ec2_client, dry_run=True):
    volumes = ec2_client.describe_volumes(Filters=[{'Name': 'status', 'Values': ['available']}])
    for vol in volumes['Volumes']:
        vol_id = vol['VolumeId']
        if not dry_run:
            ec2_client.delete_volume(VolumeId=vol_id)
            print(f"Deleted unattached volume: {vol_id}")
        else:
            print(f"Would delete unattached volume: {vol_id}")

def delete_old_snapshots(ec2_client, days=30, dry_run=True):
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    snapshots = ec2_client.describe_snapshots(OwnerIds=['self'])
    for snap in snapshots['Snapshots']:
        snap_id = snap['SnapshotId']
        start_time = snap['StartTime']
        if start_time < cutoff:
            if not dry_run:
                ec2_client.delete_snapshot(SnapshotId=snap_id)
                print(f"Deleted snapshot: {snap_id}")
            else:
                print(f"Would delete snapshot: {snap_id}")

def main():
    parser = argparse.ArgumentParser(description="AWS Cleanup Tool")
    parser.add_argument('--dry-run', action='store_true', default=True, help='Perform a dry run (default)')
    parser.add_argument('--execute', dest='dry_run', action='store_false', help='Actually delete resources')
    parser.add_argument('--days', type=int, default=30, help='Age in days for snapshot deletion')
    args = parser.parse_args()

    ec2 = boto3.client('ec2')
    delete_unattached_volumes(ec2, args.dry_run)
    delete_old_snapshots(ec2, args.days, args.dry_run)

if __name__ == '__main__':
    main()
