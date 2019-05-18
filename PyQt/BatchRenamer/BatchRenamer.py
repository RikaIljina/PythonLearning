import sys
from pathlib import Path
import re
import os


class BatchRenamer:
    def __init__(self):
        self.matchstring = ''
        self.user_paths = []
        self.changed_paths = []
        self.stems = {}
        self.allowed_chars = '^[^\.][a-zA-Z0-9\.\-\_\$\s]+$'
        self.allowed_symbols = '[a-zA-Z0-9\.\-\_\$\s]'

    def add_path(self, path):
        if path not in self.user_paths:
            self.user_paths.append(path)

    def get_paths(self):
        return self.user_paths

    def sort_paths(self):
        self.user_paths.sort(key=lambda n: n.name)      # sort only by filename, not by path!!

    def del_path(self, idx):
        self.user_paths.remove(self.user_paths[idx])

    def move_up(self, idx):
        tmp = self.user_paths[idx]
        self.user_paths[idx] = self.user_paths[idx-1]
        self.user_paths[idx-1] = tmp

    def move_down(self, idx):
        tmp = self.user_paths[idx]
        self.user_paths[idx] = self.user_paths[idx+1]
        self.user_paths[idx+1] = tmp

    def check_prefix(self, prefix):
        reg = re.compile(self.allowed_chars)
        reg_l = re.compile(self.allowed_symbols)
        print(reg.match(prefix))
        if reg.match(prefix) and len(prefix) <= 32:
            return prefix
        else:
            count = 0
            new_pref = ''
            print(prefix, 'Invalid prefix: contains invalid characters or is longer than 32 characters')
            for char in prefix:
                print(char, reg_l.match(char))
                if (new_pref == '' and char == '.') or count >= 32:
                    continue
                if reg_l.match(char):
                    new_pref += char
                    count += 1
            return new_pref


