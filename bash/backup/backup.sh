#!/bin/bash
set -euo pipefail
# Simple backup script – tars a directory and copies to a backup location
SOURCE_DIR="${1:-.}"
BACKUP_DIR="${2:-./backups}"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
ARCHIVE="${BACKUP_DIR}/backup_${TIMESTAMP}.tar.gz"

mkdir -p "$BACKUP_DIR"
tar -czf "$ARCHIVE" -C "$SOURCE_DIR" .
echo "Backup created: $ARCHIVE"
