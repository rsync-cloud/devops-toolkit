#!/usr/bin/env python3
"""Log Rotator – rotates log files based on size or age."""
import os
import gzip
import shutil
import argparse

def rotate(log_path, max_size_mb=10):
    if os.path.getsize(log_path) > max_size_mb * 1024 * 1024:
        backup = log_path + ".1.gz"
        with open(log_path, 'rb') as f_in:
            with gzip.open(backup, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        open(log_path, 'w').close()
        print(f"Rotated: {log_path} -> {backup}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('logfile', help='Path to log file')
    parser.add_argument('--max-size-mb', type=int, default=10)
    args = parser.parse_args()
    rotate(args.logfile, args.max_size_mb)
