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
            '2': change_prefix,
            'q': self.run_lvl2
        }
        self.choices_lvl3_1 = {
            '1': unified_prefix,
            '2': sequential_prefix,
            'q': self.run_lvl3
        }
        self.choices_lvl3_2 = {
            '1': add_prefix,
            '2': remove_prefix,
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

    def run_lvl2(self, path_object):
        while True:
            print('1: List all files\n2: Select by prefix\n3. Select by content\n4. Select by extension\nq: Back')
            c = input()
            if self.choices_lvl2.get(c):
                self.choices_lvl2[c](path_object)
            else:
                print('wrong input')

    def run_lvl3(self, path_object):
        while True:
            print('1: Add prefix\n2: Change prefix\nq: Back')
            c = input()
            if self.choices_lvl3.get(c):
                self.choices_lvl3[c](path_object)
            else:
                print('wrong input')

    def run_lvl3_1(self, path_object):
        while True:
            print('1: Add unified prefix\n2: Add sequential prefix\nq: Back')
            c = input()
            if self.choices_lvl3_1.get(c):
                self.choices_lvl3_1[c](path_object)
            else:
                print('wrong input')

    def run_lvl3_2(self, path_object):
        while True:
            print('1: Add new prefix\n2: Just remove prefix\nq: Back')
            c = input()
            if self.choices_lvl3_2.get(c):
                self.choices_lvl3_2[c](path_object)
            else:
                print('wrong input')


class PathToRename:
    def __init__(self, path):
        self.path = path
        self.matchstring = ''
        self.user_paths = []
        self.changed_paths = []
        self.stems = {}


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


def list_all_files(path_object):
    print('path entered: ', path_object.path)
    for p in Path(path_object.path).iterdir():
        if p.is_file():
            print(p.name)


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


def make_selection(path_object, match):
    for p in Path(path_object.path).iterdir():
        if p.is_file():
            if re.search(match, str(p.name)):
                print(p.name)
                path_object.user_paths.append(str(p))
    menu_inst.run_lvl3(path_object)                      # open next submenu


def add_prefix(path_object):
    menu_inst.run_lvl3_1(path_object)


def change_prefix(path_object):
    print('changing prefix')
    menu_inst.run_lvl3_2(path_object)


def unified_prefix(path_objects):
    print('unified prefix')
    print('\nEnter prefix:\n')
    pref = input()                          # TODO: check if this is a valid file name
    print('Renaming...')
    path_objects.changed_paths = []
    for file in path_objects.user_paths:
        p = Path(file)
        if path_objects.stems.get(file) is None:
            new_stem = p.stem
        else:
            new_stem = path_objects.stems[file]
        p.rename(Path(p.parent, "{}{}".format(pref, new_stem) + p.suffix))
        path_objects.changed_paths.append(str(Path(p.parent, "{}{}".format(pref, new_stem) + p.suffix)))

    path_objects.user_paths = path_objects.changed_paths[:]
    print(path_objects.user_paths)


def sequential_prefix(path_objects):
    print('seq prefix')


def remove_prefix(path_objects):
    print('removing prefix')


def exit_menu(*args):
    print('Thank you for using this script.')
    sys.exit(0)


if __name__ == '__main__':
    menu_inst = Menu()
    menu_inst.run()
