import sys
from pathlib import Path
import re
import os


class Menu:
    def __init__(self):
        self.texts_lvl1 = '1: Enter Path\n' \
                          'h: Help\n'\
                          'q: Exit'
        self.choices_lvl1 = {
            '1': enter_path,
            'h': show_help,
            'q': exit_menu
        }
        self.texts_lvl2 = '1: List all files\n' \
                          '2: Select by prefix\n' \
                          '3. Select by content\n' \
                          '4. Select by extension\n' \
                          'b: Back\n' \
                          'h: Help\n'\
                          'q: Exit'
        self.choices_lvl2 = {
            '1': list_all_files,
            '2': select_by_start,
            '3': select_by_content,
            '4': select_by_ext,
            'h': show_help,
            'b': self.run,
            'q': exit_menu
        }
        self.texts_lvl3 = '1: Add prefix\n' \
                          '2: Remove prefix\n' \
                          'b: Back\n' \
                          'h: Help\n'\
                          'q: Exit'
        self.choices_lvl3 = {
            '1': add_prefix,
            '2': remove_prefix,
            'h': show_help,
            'b': self.run_lvl2,
            'q': exit_menu
        }
        self.texts_lvl3_1 = '1: Add unified prefix\n' \
                            '2: Add sequential prefix\n' \
                            'b: Back\n' \
                            'h: Help\n'\
                            'q: Exit'
        self.choices_lvl3_1 = {
            '1': unified_prefix,
            '2': sequential_prefix,
            'h': show_help,
            'b': self.run_lvl3,
            'q': exit_menu
        }                                               # TODO: make help menu for regex

    def run(self, *args):
        while True:
            print(self.texts_lvl1)
            c = input()
            if self.choices_lvl1.get(c):
                self.choices_lvl1[c]()
            else:
                print('wrong input')

    def run_lvl2(self, path_object, *args):
        while True:
            print(self.texts_lvl2)
            c = input()
            if self.choices_lvl2.get(c):
                self.choices_lvl2[c](path_object)
            else:
                print('wrong input')

    def run_lvl3(self, path_object, *args):
        while True:
            print(self.texts_lvl3)
            c = input()
            if self.choices_lvl3.get(c):
                self.choices_lvl3[c](path_object, *args)
            else:
                print('wrong input')

    def run_lvl3_1(self, path_object, *args):
        while True:
            print(self.texts_lvl3_1)
            c = input()
            if self.choices_lvl3_1.get(c):
                self.choices_lvl3_1[c](path_object, *args)
            else:
                print('wrong input')


class PathToRename:
    def __init__(self, path):
        self.path = path
        self.matchstring = ''
        self.user_paths = []
        self.changed_paths = []
        self.stems = {}
        self.allowed_chars = '^[^.][a-zA-Z0-9\.\-\_\$\s]+$'


def show_help():
    print('Use regex for a broader selection of file names:\n'
          '.  -  placeholder for ANY character (My..File means My01File and My__File etc)\n'
          '.? -  placeholder for ANY or NO character (.?1_File means 1_File and 01_File)\n'
          '\. -  finds an actual dot (e.g. old.file)\n'
          '+  -  matches one or several of the previous character (My+ means My and Myyy)\n'
          '*  -  matches none or several of the previous character (My+ means M and Myyy)\n'
          '(_.*?_)  -  matches the first group of characters between _ and _ (matches _My_ in _My_file_1.txt)')


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
    path_object.matchstring = r'^' + start_string
    make_selection(path_object, path_object.matchstring)


def select_by_content(path_object):
    print('Enter content:')
    cont_string = input()
    path_object.matchstring = cont_string
    make_selection(path_object, path_object.matchstring)


def select_by_ext(path_object):
    print('Enter extension without period:')
    ext_string = input()
    path_object.matchstring = '[\.]' + ext_string + '$'
    make_selection(path_object, path_object.matchstring)
###################################################


###################################################
# A list with all files to be renamed is created
def make_selection(path_object, match):
    path_object.user_paths = []
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
# Option from submenu "Add prefix": add same prefix
# to all file names
def unified_prefix(path_object, index=0):
    pref = get_user_prefix(path_object)
    if pref is None:
        menu_inst.run_lvl3_1(path_object)
    print('Renaming...')
    print(path_object.user_paths)
    path_object.changed_paths = []
    for file in path_object.user_paths:
        p = Path(file)
        if path_object.stems.get(file) is None:
            new_stem = str(p.stem)[:index] + pref + str(p.stem)[index:]
        else:
            new_stem = path_object.stems[file]

        rename_file(path_object, Path(p.parent, new_stem + p.suffix), p)   # "{}{}".format(pref, new_stem)

    path_object.user_paths = path_object.changed_paths[:]
    print(path_object.user_paths)
    return
###################################################


###################################################
# Option from submenu "Add prefix": add a prefix
# with a running sequence
def sequential_prefix(path_object, index=0):
    print('\nEnter prefix (use $ as placeholder for number, e.g. file$$$ for file001, file002 etc):')
    pref = get_user_prefix(path_object)
    print('\nSequence starts with number:')
    sequence_incr = int(input())
    match = re.search(r'(\$+)', pref)
    path_object.changed_paths = []

    print('Renaming...')

    for f in path_object.user_paths:
        p = Path(f)
        sequence = '0' * (len(match.group(0)) - len(str(sequence_incr))) + str(sequence_incr)
        if len(sequence) > len(match.group(0)) and sequence[0] == '0':
            sequence = sequence[1:]
        print(sequence)
        pref = pref[:match.start()] + sequence + pref[match.end():]
        print(pref)
        new_stem = str(p.stem)[:index] + pref + str(p.stem)[index:]

        rename_file(path_object, Path(p.parent, new_stem + p.suffix), p)  # "{}{}".format(pref, p.stem)
        #p.rename(Path(p.parent, "{}{}".format(pref, p.stem) + p.suffix))
        #path_object.changed_paths.append(str(Path(p.parent, "{}{}".format(pref, p.stem) + p.suffix)))

        sequence_incr += 1

    path_object.user_paths = path_object.changed_paths[:]
###################################################


###################################################
# Removes prefix from file name
def remove_prefix(path_object, *args):
    print('\nEnter prefix to remove from file name (use $ or . as wildcard for one character):\n')
    pref = input()
    print('before removal: ', path_object.user_paths)
    path_object.changed_paths = []

    for f in path_object.user_paths:
        p = Path(f)
        pref = pref.replace('$', '.')
        match = re.search(pref, str(p.name))
        print(match)
        if not match:
            print('not found')
            path_object.changed_paths.append(str(p))
            continue
        new_stem = str(p.stem)[:match.start()] + str(p.stem)[match.end():]
        print('New file name: ', new_stem)

        rename_file(path_object, Path(p.parent, new_stem + p.suffix), p)
        #p.rename(Path(p.parent, new_stem + p.suffix))
        #path_object.changed_paths.append(str(Path(p.parent, new_stem + p.suffix)))

    path_object.user_paths = path_object.changed_paths[:]
    print('after removal: ', path_object.user_paths)

    print(f'\nThe prefix {pref} was removed.\nDo you want to replace the removed prefix with a different prefix?')
    menu_inst.run_lvl3(path_object, match.start())

    return
###################################################


def rename_file(path_object, new_path, p):
    if new_path.is_file():
        print(f'Cannot rename file to {new_path}: it already exists')
        path_object.changed_paths.append(str(p))
    else:
        p.rename(new_path)
        path_object.changed_paths.append(str(new_path))




###################################################
# Ends script execution
def exit_menu(*args):
    print('Thank you for using this script.')
    sys.exit(0)
###################################################


if __name__ == '__main__':
    menu_inst = Menu()
    menu_inst.run()
