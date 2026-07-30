import pytest
from unittest.mock import MagicMock, patch
from aws_cleanup import delete_unattached_volumes, delete_old_snapshots

def test_delete_unattached_volumes_dry_run():
    mock_ec2 = MagicMock()
    mock_ec2.describe_volumes.return_value = {'Volumes': [{'VolumeId': 'vol-123'}]}
    delete_unattached_volumes(mock_ec2, dry_run=True)
    mock_ec2.delete_volume.assert_not_called()

def test_delete_unattached_volumes_execute():
    mock_ec2 = MagicMock()
    mock_ec2.describe_volumes.return_value = {'Volumes': [{'VolumeId': 'vol-456'}]}
    delete_unattached_volumes(mock_ec2, dry_run=False)
    mock_ec2.delete_volume.assert_called_once_with(VolumeId='vol-456')
