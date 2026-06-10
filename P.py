# task1_file_handling_exception_safe.py

import os
import shutil
from datetime import datetime

BASE_DIR = "files"
ARCHIVE_DIR = "archive"

os.makedirs(BASE_DIR, exist_ok=True)
os.makedirs(ARCHIVE_DIR, exist_ok=True)

file_path = os.path.join(BASE_DIR, "log.txt")
backup_path = os.path.join(ARCHIVE_DIR, "log_backup.txt")

try:
    # 1. Write file
    with open(file_path, "a") as file:
        file.write(f"Log entry at {datetime.now()}\n")
    print(" File written successfully")

    # 2. Read file
    with open(file_path, "r") as file:
        print("\n File content:")
        print(file.read())

    # 3. If backup already exists, remove it
    if os.path.exists(backup_path):
        os.remove(backup_path)
        print(" Old backup removed")

    # 4. Move & rename in one step
    shutil.move(file_path, backup_path)
    print(" File moved to archive as log_backup.txt")

    print("\n  completed successfully")

except Exception as e:
    print(" Exception occurred:", e)
