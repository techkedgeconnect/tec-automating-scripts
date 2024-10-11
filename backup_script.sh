# This script will ensure daily backups with the last 7 days of backups retained.

#!/bin/bash

# Variables
SOURCE_DIR="/path/to/source_directory"   # Directory to backup
BACKUP_DIR="/path/to/backup_directory"   # Directory where backups will be stored
DATE=$(date +%Y-%m-%d)                   # Current date (e.g., 2024-10-07)
BACKUP_NAME="backup-$DATE.tar.gz"        # Backup file name

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Perform the backup using tar
tar -czf "$BACKUP_DIR/$BACKUP_NAME" "$SOURCE_DIR"

# Optional: Keep backups for the last 7 days (delete older backups)
find "$BACKUP_DIR" -type f -name "*.tar.gz" -mtime +7 -exec rm {} \;

# Log the backup operation
echo "Backup of $SOURCE_DIR completed on $DATE. Saved as $BACKUP_NAME." >> "$BACKUP_DIR/backup-log.txt"
