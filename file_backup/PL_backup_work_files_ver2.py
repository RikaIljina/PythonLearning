import os
from os import walk
import hashlib
from zipfile import ZipFile
import zipfile
import datetime
import re

# file with all folders that need backup
file_with_backup_folders = r'backup_folders.txt'
log_file = r'backup_log.txt'
log_list = []


# TODO: make sure there's enough space on the disk before backup
# open the file with all folders that need backup and save them in a list
def create_dir_lists():
    backup_list = []
    if os.path.exists(file_with_backup_folders):
        with open(file_with_backup_folders, 'r') as bf:
            for file in bf:
                # print(file, ' file')
                if file.startswith('#'):
                    continue
                backup_list.append(file.strip('\n'))
            return True, backup_list
    else:
        with open(file_with_backup_folders, 'w+') as bf:
            bf.write(
                '###### Put the folder where the backup should be saved below. It must be empty!\nZ:\\MyBackupFolder\n'
                '###### Put all the folders to be backed up below, one folder per line. Subfolders will also be'
                ' included in the backup.\nZ:\\MyWorkFiles')
        return False, []


def calculate_hash(filename):
    # make a hash object
    h = hashlib.sha1()

    # open file for reading in binary mode
    with open(filename, 'rb') as file:
        # loop till the end of the file
        chunk = 0
        while chunk != b'':
            # read only 1024 bytes at a time
            chunk = file.read(1024)
            h.update(chunk)

    # return the hex representation of digest
    return h.hexdigest()


def compare_hash(filename, hashfile):
    # save hash of current file in variable
    new_hash = calculate_hash(filename)
    # compare new hash to old hash from hash file
    if os.path.exists(hashfile):
        with open(hashfile, 'r') as hm:
            old_hash = hm.read()
            if old_hash != new_hash:
                log_list.append(f'+++ CHANGED: {filename} has changed: old hash: {old_hash} '
                                f'new hash: {new_hash} +++\n\n')
                return True, new_hash
            else:
                log_list.append(f'--- NOT changed: {filename} has not changed: old hash: {old_hash} '
                                f'new hash: {new_hash} ---\n\n')
                return False, new_hash
    else:
        return True, new_hash


def update_backup(b_dir, h_file, f_hash, f_target, f_source):
    if not os.path.exists(b_dir):
        try:
            os.makedirs(b_dir)
        except FileExistsError:
            # directory already exists
            pass
    with open(h_file, 'w+') as this_hash:
        this_hash.write(f_hash)

    compression = zipfile.ZIP_DEFLATED
    with ZipFile((f_target + '.zip'), 'w') as current_zip:
        current_zip.write(f_source, os.path.basename(f_target), compress_type=compression)
        print(f'\nCreated new backup of {f_source}\n')
        log_list.append(f'Created new backup of {f_source} at {f_target}.zip\n\n\n')


# TODO: prompt user if she wants to add a new file location to the backup_list

# Compare the previous backup to the current one and check if files have been deleted
# from the source location. Ask if the respective backup files should be deleted, too.
def compare_backups(new_backup_list):
    # print(new_backup_list)
    files_in_backup = 'files_in_backup.txt'
    ghost_files = []
    if os.path.exists(files_in_backup):
        with open(files_in_backup, 'r', encoding='utf-8') as fib:
            old_files = fib.read().split('\n')
            old_files.remove('')
        for i in range(0, len(old_files), 2):
            file = old_files[i]
            if file not in new_backup_list:
                print(
                    f'{file} is not in the original location anymore. Delete {old_files[i + 1]}.zip and hash? y/n \n')
                inp = input()
                if inp == 'y' or inp == 'Y':
                    os.remove(old_files[i + 1] + '.zip')
                    os.remove(old_files[i + 1] + '.hash.txt')
                    log_list.append(f'\n### Deleted: {old_files[i + 1]}.zip and hash because source file has been '
                                    f'deleted. ###\n')
                else:
                    ghost_files.append(file)
                    ghost_files.append(old_files[i + 1])
                    log_list.append(f'\n### Still in backup: {old_files[i + 1]}.zip and hash, but source file does not '
                                    f'exist. ###\n')

    with open(files_in_backup, 'w+', encoding='utf-8') as fib:
        if ghost_files:
            new_backup_list.extend(ghost_files)
        for el in new_backup_list:
            fib.write(el + '\n')
        log_list.append(f'\n### A list of all files currently in backup is here: {files_in_backup} ###\n')


def create_log():

    if os.path.exists(log_file):
        with open(log_file, 'r+', encoding='utf-8') as log:
            old_log = log.read()
            temp_log = ''
            st = re.compile('#######')
            en = re.compile('END #######')
            m_st = st.search(old_log)
            m_en = en.search(old_log)
            start_i = m_st.start()
            end_i = m_en.end()
            for i in range(start_i, end_i):
                temp_log += old_log[i]

    with open(log_file, 'w+', encoding='utf-8') as log:
        now = datetime.datetime.now()
        log.write(f'####### {now} #######\n\n')
        for el in log_list:
            log.write(el)
        log.write(f'\n\n####### END #######\n\n')
        log.write(temp_log)

    print(f'Log created\n')
    print(f'{(int(os.path.getsize(log_file)) / 1024):.2f} KB ')


def main():
    fileExists, backup_list = create_dir_lists()
    if not fileExists or len(backup_list) == 0:
        print(
            f'The file {file_with_backup_folders} was just created in the same folder as this script.'
            f'\nPlease fill it with the backup location and the folders that you want to backup.'
            f'\nMake sure the backup location is an empty folder.')
        input()
        return

    backup_path = backup_list[0]
    current_backup_list = []
    print(f'\nBackup location: {backup_path}\n')
    log_list.append(f'\nBackup location: {backup_path}\n')
    backup_list.pop(0)
    print(f'\nBackup list: {backup_list}\n')
    log_list.append(f'\nBackup list: \n')
    for el in backup_list:
        log_list.append(f' {el}\n')
    log_list.append('\n\n')

    for backup_location in backup_list:

        paths = []

        for (dirpath, dirnames, filenames) in walk(backup_location):
            current_files = filenames  # all files in this directory
            paths.append(dirpath)  # path we're currently in

            for file in current_files:
                file_for_backup = os.path.join(dirpath, file)
                backup_dir = os.path.join(backup_path, dirpath.replace(':', '', 1))
                file_target = os.path.join(backup_path, dirpath.replace(':', '', 1), file)
                hashfile_name = os.path.join(backup_path, dirpath.replace(':', '', 1),
                                             (file + '.hash.txt'))

                log_list.append(f'Backup of {file} \n from {file_for_backup} \n to {backup_dir} \n as {file_target}.zip'
                                f'\n\n hash file {hashfile_name}\n\n')

                current_backup_list.append(file_for_backup)
                current_backup_list.append(file_target)

                hasChanged, new_hash = compare_hash(file_for_backup, hashfile_name)

                if hasChanged:
                    update_backup(backup_dir, hashfile_name, new_hash, file_target, file_for_backup)

    compare_backups(current_backup_list)
    print(f'Creating log at {log_file}...\n')
    create_log()


if __name__ == "__main__":
    main()
