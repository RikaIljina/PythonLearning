# Add your file name here

my_file = open(r"counttext.txt", "r", encoding="utf-8")


# Read the file and save it in a string

# remove all periods and commas from string and split the string by space

# Result: a list with words
# make a dictionary 
# read the list word by word
# for each word: if not in dict, add it to dict as a key. Then add +1 to value

# calculate percentage for each word and print
# sort dict!

def make_word_list(file):
    file_contents = file.read()
    file_contents_upd = "".join(c for c in file_contents if c not in "\"\t;{}“”[]()?:!.,-")
    file_contents_upd = file_contents_upd.replace("\n", " ")
    file_contents_upd = file_contents_upd.lower()
    file_contents_list = file_contents_upd.split(" ")

    return file_contents_list


def count_words(word_list):
    word_dict = {}
    for el in word_list:
        if el in word_dict:
            word_dict[el] += 1
        else:
            word_dict[el] = 1
    return word_dict


def show_result(word_list, word_dict):
    sorted_list = [(k, word_dict[k]) for k in sorted(word_dict, key=word_dict.get, reverse=True)]
    # print(sorted_list[0][0])
    for el in range(0, len(sorted_list)):
        prc = 100 * int(sorted_list[el][1]) / len(sorted_list)
        print(f"{sorted_list[el][0]} : {prc:.2f}%")


word_list = make_word_list(my_file)
word_dict = count_words(word_list)

show_result(word_list, word_dict)

input()

my_file.close()
