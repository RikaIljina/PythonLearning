## Basic backup script in Python

This script can be executed from a Python IDE or as a .py file.

It will create the following files in the same folder it is in:

```
backup_folders.txt
files_in_backup.txt
backup_log.txt
```
The file **backup_folders.txt** should contain:
- the full path to the location where the backup will be stored
- all paths that have to be stored in backup, each in a new line

The script will read the file, ignore all lines that start with **#**, save line 0 as the
backup path and all other lines as folders to store in backup.

Subfolders will be included in the backup.

Each file will be zipped (with compression). Its folder structure will be recreated in the
backup folder. A hash file will be saved for each file, containing its hash value at the
moment of the backup.

When the script is run, it creates the hash value of each original file and compares it to
the value in the corresponding hash file. If they don't match, a new backup of this file is created.

All files currently in backup are saved in the file **files_in_backup.txt** (source and target path).
Each new backup run matches the files in backup with the original files and checks if
a source file has been deleted. If yes, **the user is prompted to decide whether to keep the
file in backup or to delete it**.

The file **backup_log** summarizes all actions that the script has executed, stating which
files have been updated and where they are saved. The log file only contains the two most recent
backup runs.

## This script is a work in progress.
Use it at our own risk. The script does not check for available free disk space yet, so
exceeding that might cause some issues. The log might also consume too much space.

It is also supposed to be a desktop application with a neat GUI and a drag&drop functionality,
and it will be once I've learned how to work with PyQt :smile:

###TODO:
- [ ] Check for free disk space
- [ ] Check for all possible errors, such as wrong file formatting
- [ ] Consider saving the hash in *files_in_backup* instead of creating individual files
- [ ] Figure out ways to make the code faster
- [ ] Create a GUI