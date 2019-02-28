# Add your file name here

my_file = open(r"counttext.txt", "r", encoding="utf-8")

# This function reads the file, removes all unwanted characters, replaces line breaks with whitespace,
# converts all characters to lowercase and splits the string into a list containing all words.
def make_word_list(file):
    file_contents = file.read()
    file_contents_upd = "".join(c for c in file_contents if c not in "\"\t;{}“”[]()?:!.,-")
    file_contents_upd = file_contents_upd.replace("\n", " ")
    file_contents_upd = file_contents_upd.lower()
    file_contents_list = file_contents_upd.split(" ")

    return file_contents_list


# This function creates a dictionary and reads the list word by word.
# Each word will be used as a unique key in the dict, and its value is a counter
# indicating how many times it was used throughout the text.
def count_words(word_list):
    word_dict = {}
    for el in word_list:
        if el in word_dict:
            word_dict[el] += 1
        else:
            word_dict[el] = 1
    return word_dict


# This function sorts the dict by most used word, calculates the percentage for each word
# and prints out an f-string formatted line with the info.
def show_result(word_list, word_dict):
    sorted_list = [(k, word_dict[k]) for k in sorted(word_dict, key=word_dict.get, reverse=True)]
    for el in range(0, len(sorted_list)):
        prc = 100 * int(sorted_list[el][1]) / len(sorted_list)
        print(f"{sorted_list[el][0]} : {prc:.2f}%")



word_list = make_word_list(my_file)
word_dict = count_words(word_list)

# TODO: Save result to file
show_result(word_list, word_dict)

input()

my_file.close()
