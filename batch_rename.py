from pathlib import Path
import re


def make_file_list():
    my_path = []
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

    for p in Path('.').iterdir():
        if p.is_file():
            if re.search(match_str, str(p)):
                print(p)
                my_path.append(str(p))

    return my_path


def add_prefix(my_path, new_stems=None):
    choice = ''
    print('\n1. Add unified prefix\n2. Add sequential prefix')
    while choice != '1' and choice != '2':
        choice = input()
    if choice == '1':
        print('\nEnter prefix:\n')
        pref = input()
        print('Renaming...')
        for f in my_path:
            p = Path(f)
            p.rename(Path(p.parent, "{}_{}".format(pref, p.stem) + p.suffix))
    elif choice == '2':
        print('\nEnter prefix (use $ as placeholder for number, e.g. file$$$ for file001, file002 etc):\n')
        pref = input()
        print('\nSequence starts with number:\n')
        count = int(input())
        match = re.search(r'(\$+)', pref)
        print('Renaming...')

        for f in my_path:
            p = Path(f)
            sequence = '0' * (len(match.group(0))-1) + str(count)
            if len(sequence) > len(match.group(0)) and sequence[0] == '0':
                sequence = sequence[1:]
            print(sequence)
            pref = pref[:match.start()] + sequence + pref[match.end():]
            print(pref)
            if new_stems is None:
                new_stem = p.stem
            else:
                new_stem = new_stems[f]
            p.rename(Path(p.parent, "{}_{}".format(pref, new_stem) + p.suffix))
            count += 1
    return


def change_prefix(my_path):
    choice = ''
    new_stems = {}
    print('\nWhich prefix do you want to remove?\n')
    pref = input()
    for f in my_path:
        p = Path(f)
        pref = pref.replace('$','.')
        match = re.search(pref, f)
        print(pref, match)
        print(p)
        print(str(p.stem)[match.end():])
        new_stem = str(p.stem)[match.end():]
        new_stems[f] = new_stem

    print('\nThe remaining part of the filename is ', new_stem)
    print('\nDo you want to replace it with a different prefix?\n')
    print('\n1. Add different prefix\n2. Just remove old prefix')
    while choice != '1' and choice != '2':
        choice = input()
    if choice == '1':
        add_prefix(my_path, new_stems)
    else:
        for f in my_path:
            p = Path(f)
            p.rename(Path(p.parent, new_stems[f] + p.suffix))
        print('\nFinished\n')

    return


def main():
    my_path = make_file_list()
    print('\nThese files will be renamed:\n', my_path)
    print('\nWhat do you want to do?\n1: Add prefix\n2: Change prefix\n')
    choice = 0
    while choice != '1' and choice != '2':
        choice = input()

    if choice == '1':
        add_prefix(my_path)
    else:
        change_prefix(my_path)


if __name__ == "__main__":
    main()