import sys
from pathlib import Path
import re
import os


class Menu:
    def __init__(self):
        self.choices_lvl1 = {
            '1': enter_path,
            'q': exit_menu
        }
        self.choices_lvl2 = {
            '1': list_all_files,
            '2': select_by_start,
            '3': select_by_content,
            '4': select_by_ext,
            'q': self.run
        }
        self.choices_lvl3 = {
            '1': add_prefix,
            '2': remove_prefix,
            'q': self.run_lvl2
        }
        self.choices_lvl3_1 = {
            '1': unified_prefix,
            '2': sequential_prefix,
            'q': self.run_lvl3
        }

    def run(self, *args):
        while True:
            print('1: Enter Path\nq: Exit')
            c = input()
            if self.choices_lvl1.get(c):
                self.choices_lvl1[c]()
            else:
                print('wrong input')

    def run_lvl2(self, path_object, *args):
        while True:
            print('1: List all files\n2: Select by prefix\n3. Select by content\n4. Select by extension\nq: Back')
            c = input()
            if self.choices_lvl2.get(c):
                self.choices_lvl2[c](path_object)
            else:
                print('wrong input')

    def run_lvl3(self, path_object, *args):
        while True:
            print('1: Add prefix\n2: Remove prefix\nq: Back')
            c = input()
            if self.choices_lvl3.get(c):
                self.choices_lvl3[c](path_object, *args)
            else:
                print('wrong input')

    def run_lvl3_1(self, path_object, *args):
        while True:
            print('1: Add unified prefix\n2: Add sequential prefix\nq: Back')
            c = input()
            if self.choices_lvl3_1.get(c):
                self.choices_lvl3_1[c](path_object)
            else:
                print('wrong input')


class PathToRename:
    def __init__(self, path):
        self.path = path
        self.matchstring = ''
        self.user_paths = []
        self.changed_paths = []
        self.stems = {}
        self.allowed_chars = '^[a-zA-Z0-9\.\-_\$\s]+$'


###################################################
# Lets user enter a path
def enter_path():
    # Asks user for path input
    # checks if path is valid
    # saves path in object and enters submenu
    print('Enter path:')
    while True:
        user_path = input()
        if os.path.isdir(user_path):
            print('Path ok')
            break
        else:
            print('Bad path, try again')
    new_path_object = PathToRename(Path(user_path))      # remember path in object PathToRename
    menu_inst.run_lvl2(new_path_object)                  # open next submenu
###################################################


###################################################
# Shows all files at the path chosen by user
def list_all_files(path_object):
    print('path entered: ', path_object.path)
    for p in Path(path_object.path).iterdir():
        if p.is_file():
            print(p.name)
###################################################


###################################################
# User chooses which files to rename in the directory
def select_by_start(path_object):
    print('Enter start string:')
    start_string = input()
    match_str = r'^' + start_string
    path_object.matchstring = match_str
    make_selection(path_object, path_object.matchstring)


def select_by_content(path_object):
    print('Enter content:')
    cont_string = input()
    match_str = cont_string
    path_object.matchstring = match_str
    make_selection(path_object, path_object.matchstring)


def select_by_ext(path_object):
    print('Enter extension without period:')
    ext_string = input()
    match_str = '[\.]' + ext_string + '$'
    path_object.matchstring = match_str
    make_selection(path_object, path_object.matchstring)
###################################################


###################################################
# A list with all files to be renamed is created
def make_selection(path_object, match):
    for p in Path(path_object.path).iterdir():
        if p.is_file():
            if re.search(match, str(p.name)):
                print(p.name)
                path_object.user_paths.append(str(p))       # full path to file is saved
    menu_inst.run_lvl3(path_object)                         # open next submenu
###################################################


###################################################
# Asks user for new prefix
def get_user_prefix(path_object):
    print('\nEnter prefix:\n')
    pref = input()
    reg = re.compile(path_object.allowed_chars)
    print(reg.match(pref))
    if reg.match(pref) and len(pref) <= 32:
        return pref
    else:
        print('Invalid prefix: contains invalid characters or is longer than 32 characters')
        return None
###################################################


###################################################
# Calls submenu for adding a prefix
def add_prefix(path_object, *args):
    menu_inst.run_lvl3_1(path_object, *args)
###################################################


###################################################
# Allows to select a prefix to change or remove
# then call submenu
def change_prefix(path_object):
    print('\nEnter prefix to remove from file name (use $ or . as wildcard for one character):\n')
    pref = input()

    print(f'\nthe prefix {pref} will be removed.\nDo you want to replace the removed prefix with a different prefix?')
    menu_inst.run_lvl3_2(path_object, pref)
###################################################


###################################################
# Option from submenu "Add prefix": add same prefix
# to all file names
def unified_prefix(path_object):
    pref = get_user_prefix(path_object)
    if pref is None:
        menu_inst.run_lvl3_1(path_object)
    print('Renaming...')
    path_object.changed_paths = []
    for file in path_object.user_paths:
        p = Path(file)
        if path_object.stems.get(file) is None:
            new_stem = p.stem
        else:
            new_stem = path_object.stems[file]
        p.rename(Path(p.parent, "{}{}".format(pref, new_stem) + p.suffix))
        path_object.changed_paths.append(str(Path(p.parent, "{}{}".format(pref, new_stem) + p.suffix)))

    path_object.user_paths = path_object.changed_paths[:]
    print(path_object.user_paths)
    return
###################################################


###################################################
# Option from submenu "Add prefix": add a prefix
# with a running sequence
def sequential_prefix(path_object):
    print('\nEnter prefix (use $ as placeholder for number, e.g. file$$$ for file001, file002 etc):')
    pref = get_user_prefix(path_object)
    print('\nSequence starts with number:')
    sequence_incr = int(input())
    match = re.search(r'(\$+)', pref)
    print('Renaming...')

    for f in path_object.user_paths:
        p = Path(f)
        sequence = '0' * (len(match.group(0)) - len(str(sequence_incr))) + str(sequence_incr)
        if len(sequence) > len(match.group(0)) and sequence[0] == '0':
            sequence = sequence[1:]
        print(sequence)
        pref = pref[:match.start()] + sequence + pref[match.end():]
        print(pref)
        p.rename(Path(p.parent, "{}{}".format(pref, p.stem) + p.suffix))
        sequence_incr += 1
        path_object.changed_paths.append(str(Path(p.parent, "{}{}".format(pref, p.stem) + p.suffix)))

    path_object.user_paths = path_object.changed_paths[:]
###################################################


###################################################
# Removes prefix from file name
def remove_prefix(path_object):
    print('\nEnter prefix to remove from file name (use $ or . as wildcard for one character):\n')
    pref = input()

    for f in path_object.user_paths:
        p = Path(f)
        pref = pref.replace('$', '.')
        match = re.search(pref, str(p.name))
        if not match:
            path_object.changed_paths.append(str(p))
            continue
        new_stem = str(p.stem)[match.end():]
        print('New file name: ', new_stem)
        p.rename(Path(p.parent, new_stem + p.suffix))
        path_object.changed_paths.append(str(Path(p.parent, new_stem + p.suffix)))

    path_object.user_paths = path_object.changed_paths[:]

    print(f'\nThe prefix {pref} was removed.\nDo you want to replace the removed prefix with a different prefix?')
    menu_inst.run_lvl3(path_object)

    return
###################################################


###################################################
# Ends script execution
def exit_menu(*args):
    print('Thank you for using this script.')
    sys.exit(0)
###################################################


if __name__ == '__main__':
    menu_inst = Menu()
    menu_inst.run()
