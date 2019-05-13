from pathlib import Path
import re

# abs_path = r'C:\Users\wasil\OneDrive\Desktop\Python\GitReps\PythonLearning\word_count_script'


def make_file_list():
    print('Enter the path to your files:')
    abs_path = input()
    my_paths = []
    choice = ''
    print('What files should be renamed?')
    print('1. Starts with...')
    print('2. Contains...')
    print('3. Extension...')
    while choice != '1' and choice != '2' and choice != '3':
        choice = input()
    if choice == '1':
        print('Enter start string:')
        start_string = input()
        match_str = r'^' + start_string
    elif choice == '2':
        print('Enter contained string:')
        cont_string = input()
        match_str = cont_string
    elif choice == '3':
        print('Enter extension without period:')
        ext_string = input()
        match_str = '.' + ext_string + '$'

    for p in Path(abs_path).iterdir():
        print(p)
        if p.is_file():
            if re.search(match_str, str(p.name)):
                print(p)
                my_paths.append(str(p))

    return my_paths


def add_prefix(my_paths, new_stems=None):
    choice = ''
    print('\n1. Add unified prefix\n2. Add sequential prefix')
    while choice != '1' and choice != '2':
        choice = input()
    if choice == '1':
        print('\nEnter prefix:\n')
        pref = input()
        print('Renaming...')
        for f in my_paths:
            p = Path(f)
            p.rename(Path(p.parent, "{}{}".format(pref, p.stem) + p.suffix))
    elif choice == '2':
        print('\nEnter prefix (use $ as placeholder for number, e.g. file$$$ for file001, file002 etc):\n')
        pref = input()
        print('\nSequence starts with number:\n')
        sequence_incr = int(input())
        match = re.search(r'(\$+)', pref)
        print('Renaming...')

        for f in my_paths:
            p = Path(f)
            sequence = '0' * (len(match.group(0))-1) + str(sequence_incr)
            if len(sequence) > len(match.group(0)) and sequence[0] == '0':
                sequence = sequence[1:]
            print(sequence)
            pref = pref[:match.start()] + sequence + pref[match.end():]
            print(pref)
            if new_stems is None:
                new_stem = p.stem
            else:
                new_stem = new_stems[f]
            p.rename(Path(p.parent, "{}{}".format(pref, new_stem) + p.suffix))
            sequence_incr += 1
    return


def change_prefix(my_paths):
    choice = ''
    new_stems = {}
    print('\nWhich prefix do you want to remove? (Use $ as wildcard)\n')
    pref = input()
    for f in my_paths:
        p = Path(f)
        pref = pref.replace('$', '.')
        match = re.search(pref, str(p.name))
        print(pref, match)
        print(p.name)
        print(str(p.stem)[match.end():])
        new_stem = str(p.stem)[match.end():]
        new_stems[f] = new_stem

    print('\nThe remaining part of the filename is ', new_stem)
    print('\nDo you want to replace it with a different prefix?')
    print('\n1. Add different prefix\n2. Just remove old prefix')
    while choice != '1' and choice != '2':
        choice = input()
    if choice == '1':
        new_paths = []
        for f in my_paths:
            p = Path(f)
            p.rename(Path(p.parent, new_stems[f] + p.suffix))
            new_paths.append(str(Path(p.parent, new_stems[f] + p.suffix)))
            print(str(Path(p.parent, new_stems[f] + p.suffix)))
        add_prefix(new_paths, new_stems)
    else:
        for f in my_paths:
            p = Path(f)
            p.rename(Path(p.parent, new_stems[f] + p.suffix))
        print('\nFinished\n')

    return


def main():
    my_paths = make_file_list()
    print('\nThese files will be renamed:\n', my_paths)
    print('\nWhat do you want to do?\n1: Add prefix\n2: Change prefix\n')
    choice = 0
    while choice != '1' and choice != '2':
        choice = input()

    if choice == '1':
        add_prefix(my_paths)
    else:
        change_prefix(my_paths)


if __name__ == "__main__":
    main()
