
# message file
enigma_code_file = "enigma_message"  # "coding_qual_input"


# dictionary for coded words
enigma_code = {}


# decode message
# receives the encoded message file as its input
def decode(message_file):

    global enigma_code

    # read the message file and get the number of code lines
    code_lines = read_message_file(message_file)

    display_file(code_lines)

    # extract the codes
    enigma_codes = get_code(code_lines)

    # display the code numbers in pyramid form
    build_pyramid(code_lines)

    display_message(enigma_codes)


# read encoded massage file
def read_message_file(message_file):

    # read the message file 
    input_file = open(message_file + '.txt', 'r')

    # get the number of lines in the file
    number_of_codes = input_file.readlines()

    return number_of_codes


def display_file(code_lines):

    for i in code_lines:

        print(i)


def get_code(code_lines):

    global enigma_code

    # loop through all the lines in the file
    for code_line in code_lines:

        # the code number
        code_number = ''

        # for each code line, loop through all the characters
        for code_number_digit in code_line:

            # if the character is a number
            if code_number_digit.isdigit():

                # store the number
                code_number += code_number_digit

        # get the index position of the space in the code line
        code_delimeter = code_line.index(' ')

        # get the code word by reading all the character to the right of the space
        code_word = code_line[code_delimeter + 1:len(code_line)]

        # populate the code dictionary
        enigma_code[int(code_number)] = code_word

    # get the key values from the code dictionary
    enigma_code_keys = list(enigma_code.keys())

    # sort them into ascending numerical order 
    enigma_code_keys.sort()

    # create a new dictionary
    # loop through the sorted key values and match them with their key value pair   
    sorted_dictionary = {i: enigma_code[i] for i in enigma_code_keys}

    # re-assign the code dictionary with the sorted dictionary
    enigma_code = sorted_dictionary

    return enigma_code_keys


# display the code numbers in the form of a pyramid
def build_pyramid(code_lines):

    # get the number of rows of the pyramid by dividing
    # the number of code lines by 2
    pyramid_height = int(len(code_lines) / 2)  # 12

    # initialise the code number
    code_number = 1

    # loop through the number of rows of the pyramid
    for i in range(0, pyramid_height):

        # display the required amount of left padding for each row
        print(' ' * (pyramid_height - i), end=' ')

        # then loop through the required code numbers for each row
        if code_number < int(len(code_lines)):

            for j in range(0, i + 1):

                # display the code number
                print(code_number, end=' ')

                # increment code number
                code_number += 1

            print(' ')

    print()


def display_message(enigma_codes):

    code_numbers_to_read = 1

    # code number list
    enigma_code_numbers = []

    message = []

    # number of code lines to read
    x = int(len(enigma_codes) / 2)  # 12

    # create subsets of the code numbers
    for y in range(x, 0, -1):

        # get the number of code numbers from 0 to code numbers to read
        enigma_code_numbers.append(enigma_codes[0:code_numbers_to_read])

        # move to the next position
        enigma_codes = enigma_codes[code_numbers_to_read:]

        # increase the number of code numbers to read
        code_numbers_to_read += 1

    # match the code word with the code
    for i in range(0, x):  # - 1

        # get the correct code number from the subset
        code_number = enigma_code_numbers[i][i]

        # get the code words
        message.append(enigma_code[enigma_code_numbers[i][i]])

        code_word = str(message[i])

        # display the code number with its corresponding code word
        print(str(code_number) + ': ' + code_word)

    # convert message list to a string and remove newline characters
    string_message = ''.join(message).splitlines()

    # convert the message to lowercase
    enigma_message = ' '.join(string_message).lower()

    # display the message
    print(enigma_message)


# call the decoder function
decode(enigma_code_file)
