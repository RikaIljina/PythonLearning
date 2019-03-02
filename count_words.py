import os
import sys
from pathlib import Path

# Add your file name here
file_path = r"counttext.txt"
result_path = r"result.csv"

# Remember names of source and target files
f_name = Path(file_path)
r_name = Path(result_path)

print("#" * 86)
print(f"This script will read the file {f_name} that must be placed in the same folder\n"
      f"and analyse the amount and distribution of words used in it. The result is saved\n"
      f"in a csv file in the same directory and can be opened in Excel or a text editor.\n"
      f"The file encoding is iso-8859-1, suitable for German language.")
print("#" * 86)

try:
    my_file = open(file_path, "r", encoding="iso-8859-1")
except:
    print("\nCouldn't open source file counttext.txt. Place it in the same directory as this script.\n")
    input()
    sys.exit("Aborting script...")

# Deleting old result file if it exists
if os.path.isfile(result_path):
    print(f"\nThe existing file {r_name} will be deleted and recreated. Proceed? y/n ")
    user_input = input()
    if user_input == "y" or user_input == "Y":
        os.remove(result_path)
    else:
        sys.exit("Aborting script...")

result_file = open(r"result.csv", "a+", encoding="iso-8859-1")


# This function reads the file, removes all unwanted characters, replaces line breaks with whitespace,
# converts all characters to lowercase and splits the string into a list containing all words.
def make_word_list(file):
    file_contents = file.read()
    file_contents_upd = "".join(c for c in file_contents if c not in "\"\t\\/'_;{}“”‘’“”«»[]()?:!.,—-–=<>*123y4567890§$%&#+|")
    file_contents_upd = file_contents_upd.replace("\n", " ")
    # print(file_contents_upd)
    file_contents_upd = file_contents_upd.lower()
    file_contents_list = file_contents_upd.split()
    # print(file_contents_list)

    return file_contents_list, len(file_contents_list)


# This function creates a dictionary and reads the list word by word.
# Each word will be used as a unique key in the dict, and its value is a counter
# indicating how many times it was used throughout the text.
def count_words(w_list):
    w_dict = {}
    for el in w_list:
        if el in w_dict:
            w_dict[el] += 1
        else:
            w_dict[el] = 1
    return w_dict


# This function sorts the dict by most used word and alphabetically, calculates the percentage for each word
# and appends an f-string formatted line to a comma separated csv file.
def show_result(w_dict, w_count):
    sorted_list_by_usage = [(k, w_dict[k]) for k in sorted(w_dict, key=w_dict.get, reverse=True)]
    sorted_list_alphab = [(k, w_dict[k]) for k in sorted(w_dict.keys())]
    result_file.write(f"sep=,\n")
    result_file.write(f"Analysed file: {f_name}\n")
    result_file.write(f"Unique words: {len(sorted_list_alphab)}, Total words: {w_count}\n\n")
    result_file.write(f"Words by usage,Percentage,Amount,Words alphabetically,Percentage,Amount\n")
    plural_s = "s"
    for el in range(0, len(sorted_list_by_usage)):
        prc_1 = 100 * int(sorted_list_by_usage[el][1]) / w_count
        prc_2 = 100 * int(sorted_list_alphab[el][1]) / w_count
        # print(f"{sorted_list_by_usage[el][0]} : {prc_1:.2f}%")
        result_file.write(f"{sorted_list_by_usage[el][0]},{prc_1:.3f}%,{sorted_list_by_usage[el][1]} "
                          f"usage{plural_s if sorted_list_by_usage[el][1] > 1 else ''},"
                          f"{sorted_list_alphab[el][0]},{prc_2:.3f}%,{sorted_list_alphab[el][1]} "
                          f"usage{plural_s if sorted_list_alphab[el][1] > 1 else ''}\n")


word_list, words_total = make_word_list(my_file)
# word_dict = count_words(make_word_list(my_file))

print(f"...Creating the result file {r_name} from {f_name}")
show_result(count_words(word_list), words_total)
print("...File created. Press enter to finish.")

input()

print("...Closing files...")

result_file.close()
my_file.close()
