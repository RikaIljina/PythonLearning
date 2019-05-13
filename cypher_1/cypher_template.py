##############################################
# This code is a template for encoding and
# decoding a string using a custom key that is
# layered on top of the string with ord() and
# chr(). The key can be any sequence of symbols,
# e.g. "This is my $uper-$ecret k3y!!"
# Optimally, this code would ask users to
# choose between encoding and decoding a
# string, read in a file with the secret
# content, take the key as input and overwrite
# the secret file with the encoded string.
# When decoding, it would take a key, apply
# it to the encoded file and show the result.
##############################################

# this import is just needed for a test
import random


# This function takes the string secret_content and
# the key. It turns every letter into its Unicode
# code point, adds the Unicode value of the key on top
# and returns the encoded string containing int values
# separated with '.'

def encode_string(secret_content, incr_key):
    # this will count how many symbols from the key have been used
    counter = 0
    # this will be added to each letter to encode it
    incr = 0
    # this will be the Unicode code point of the letter
    int_letter = 0
    # this is the resulting string
    safe_string = ''

    # It is possible that the key is longer than the secret text.
    # In that case, I want to encode the encoded string again with
    # the remainder of the key by running additional encryption loops.
    # If the key is shorter than the text, encryption_loops is 1.

    encryption_loops = int(0 if incr_key == "" else (len(incr_key) / len(secret_content))) + 1

    # Now let's go through each letter of our secret content
    # and convert it:

    for letter in secret_content:
        int_letter = ord(letter)

        # Let's find the value from the key that
        # will be added to our secret letter:
        incr = get_next_increment(incr_key, counter)

        # If we have more than 1 encryption loop, this loop
        # checks if there are characters in the key left that
        # have not been used yet and adds them to the increment.
        for loop in range(1, encryption_loops):
            if counter + len(secret_content) * loop < len(incr_key):
                incr += get_next_increment(incr_key, (counter + len(secret_content) * loop))

        # Let's check if we used up the entire key and reset
        # or set the counter to the next symbol in the key:
        if (incr_key is not None or incr_key != "") and len(incr_key) - counter != 1:
            counter += 1
        else:
            counter = 0

        # Here, the letter is finally encoded and added to the safe string:
        safe_string = safe_string + "." + str(int_letter + incr)

    return safe_string


# This function is the same as encode_string,
# only backwards. It takes the safe string and
# a key and returns the decoded string.
def decode_string(safe_string, incr_key):
    counter = 0
    incr = 0
    chr_letter = ''
    int_letter = 0
    decr_string = ''

    # Let's parse the encoded string, create a list
    # with all Unicode values and remove the first
    # empty value:
    encoded_list = safe_string.split('.')
    del (encoded_list[0])

    decryption_loops = int(0 if incr_key == "" else (len(incr_key) / len(encoded_list))) + 1

    for el in encoded_list:
        incr = get_next_increment(incr_key, counter)

        for loop in range(1, decryption_loops):
            if counter + len(encoded_list) * loop < len(incr_key):
                incr = incr + get_next_increment(incr_key, (counter + len(encoded_list) * loop))

        if (incr_key is not None or incr_key != "") and len(incr_key) - counter != 1:
            counter += 1
        else:
            counter = 0

        # Here, we decode the letter by subtracting the
        # calculated increment value and turning it back
        # into a character.
        int_letter = int(el) - incr
        chr_letter = chr(int_letter if 0 <= int_letter <= 1114111 else 0)

        decr_string += chr_letter

    return decr_string


# This function takes the increment key
# and the current counter as arguments and returns
# the Unicode value of the key at position [counter].

def get_next_increment(incr_key, counter):
    return 0 if incr_key is None or incr_key == "" else int(ord(incr_key[counter]))


def main():
    # This is your secret text. It should be replaced with
    # a string read from a file.
    secret_content = "This is the text I will encode. It is highly classified, of course.\nNo one is allowed to see it. Ever."
    print(secret_content + "\n")

    print("##########\nEnter your secret key (any characters, the longer, the better)\n##########:")
    incr_key = input()

    safe_string = encode_string(secret_content, incr_key)
    print("\n##########\nThis is the encoded string. It should be stored in a file for future decoding:\n##########\n",
          safe_string)

    decoded_string = decode_string(safe_string, "")
    print("\n##########\nThis is what you get if you decode the string without a key:\n##########\n", decoded_string)

    # The following logic constructs a random key with 1-35 characters
    # and tries to decode the string with it:
    random.seed()
    rnd_key = ''
    for i in range(random.randrange(1, 35)):
        random.seed()
        rnd_key = rnd_key + chr(random.randint(33, 127))
    decoded_string = decode_string(safe_string, str(rnd_key))
    print("\n##########\nThis is what you get if you decode the string with the random key ", rnd_key,
          ":\n##########\n", decoded_string)

    # Obviously, incr_key shouldn't be saved anywhere. Rather, the user
    # should be prompted to enter the correct key now.
    decoded_string = decode_string(safe_string, incr_key)
    print("\n##########\nThis is what you get if you decode the string with the correct key:\n##########\n")
    print(decoded_string)
    print("\n##########\nI hope you enjoyed my first attempt at encryption! :)\n##########\n")


if __name__ == "__main__":
    main()
