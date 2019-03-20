import os
from os import walk
import hashlib
from zipfile import ZipFile
import zipfile

# file with all folders that need backup
file_with_backup_folders = (r'backup_folders.txt')

all_files_in_backup = []  # TODO: save all files in backup in a list to check if any have been deleted


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
            bf.write('######')
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
                print(f"file changed! {new_hash} {old_hash}")
                return True, new_hash
            else:
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
    with open(h_file, 'w+') as this_hash:  # TODO: call function update_hash
        this_hash.write(f_hash)

    compression = zipfile.ZIP_DEFLATED
    with ZipFile((f_target + '.zip'), 'w') as current_zip:
        current_zip.write(f_source, os.path.basename(f_target), compress_type=compression)
        print(f'Created new backup of {f_source}')


# TODO: prompt user if she wants to add a new file location to the backup_list

# Compare the previous backup to the current one and check if files have been deleted
# from the source location. Ask if the respective backup files should be deleted, too.
def compare_backups(new_backup_list):
    print(new_backup_list)
    files_in_backup = 'files_in_backup.txt'
    ghost_files = []
    if os.path.exists(files_in_backup):
        with open(files_in_backup, 'r', encoding='utf-8') as fib:
            old_files = fib.read().split('\n')
            old_files.remove('')
        for i in range(0, len(old_files), 2):
            file = old_files[i]
            print(file)
            if file not in new_backup_list:
                print(
                    f'{file} is not in the original location anymore. Delete {old_files[i + 1]}.zip and hash?? y/n \n')
                inp = input()
                if inp == 'y' or inp == 'Y':
                    os.remove(old_files[i + 1] + '.zip')
                    os.remove(old_files[i + 1] + '.hash.txt')
                else:
                    ghost_files.append(file)
                    ghost_files.append(old_files[i + 1])

    with open(files_in_backup, 'w+', encoding='utf-8') as fib:
        if ghost_files:
            new_backup_list.extend(ghost_files)
        for el in new_backup_list:
            fib.write(el + '\n')


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
    backup_list.pop(0)
    print(f'\nBackup list: {backup_list}\n')

    for backup_location in backup_list:

        current_files = []
        current_dirs = []
        current_path = ''
        paths = []

        for (dirpath, dirnames, filenames) in walk(backup_location):
            current_files = filenames  # all files in this directory
            current_dirs = dirnames  # all folders in this directory
            paths.append(dirpath)  # path we're currently in

            for file in current_files:
                file_for_backup = os.path.join(dirpath, file)
                backup_dir = os.path.join(backup_path, dirpath.replace(':', '', 1))
                file_target = os.path.join(backup_path, dirpath.replace(':', '', 1), file)
                hashfile_name = os.path.join(backup_path, dirpath.replace(':', '', 1),
                                             (file + '.hash.txt'))

                #   print(
                #       f'Backup of {file} from {file_for_backup} \n to {backup_dir} as {file_target} \n hash file {hashfile_name}')

                current_backup_list.append(file_for_backup)
                current_backup_list.append(file_target)

                filehash = calculate_hash(file_for_backup)

                hasChanged, new_hash = compare_hash(file_for_backup, hashfile_name)

                #    print(f'{file} has changed: {hasChanged}  {new_hash}')

                if hasChanged:
                    # input('backup? ')
                    update_backup(backup_dir, hashfile_name, filehash, file_target, file_for_backup)

    print(current_backup_list)
    compare_backups(current_backup_list)


if __name__ == "__main__":
    main()
