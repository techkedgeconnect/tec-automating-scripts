# This Python script is meant to automatically back up any specify directory every day and remove backups older than 7 days
import os
import tarfile
import time
from datetime import datetime, timedelta

# Variables
SOURCE_DIR = "/path/to/source_directory"      # Directory to backup
BACKUP_DIR = "/path/to/backup_directory"      # Directory where backups will be stored
RETENTION_DAYS = 7                            # Number of days to retain old backups

# Create backup directory if it doesn't exist
if not os.path.exists(BACKUP_DIR):
    os.makedirs(BACKUP_DIR)

# Generate the backup filename with current date
current_date = datetime.now().strftime('%Y-%m-%d')
backup_name = f"backup-{current_date}.tar.gz"
backup_path = os.path.join(BACKUP_DIR, backup_name)

# Create a tar.gz backup of the source directory
with tarfile.open(backup_path, "w:gz") as tar:
    tar.add(SOURCE_DIR, arcname=os.path.basename(SOURCE_DIR))

print(f"Backup of {SOURCE_DIR} completed successfully. Saved as {backup_name}")

# Optional: Delete backups older than retention period
now = time.time()
for filename in os.listdir(BACKUP_DIR):
    file_path = os.path.join(BACKUP_DIR, filename)
    if os.path.isfile(file_path):
        file_age = now - os.path.getmtime(file_path)
        if file_age > RETENTION_DAYS * 86400:  # 86400 seconds in a day
            os.remove(file_path)
            print(f"Deleted old backup: {filename}")
