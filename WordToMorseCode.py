# WORD TO MORSE CODE

# Declaring a variable called word_input which takes an input, converts
# it into a string and then saves it in a list
word_input = list(str(input()))

# Defining a function called convert_to_morse_code, which takes the word_input
# variable as the parameter


def convert_to_morse_code(word_input):
    # All letters with their equvilant morse code version saved in a dictionary
    # which we use later to convert.
    morse_code_mappings = {
        'A': ' ·-',
        'B': ' -···',
        'C': ' -·-·',
        'D': ' -··',
        'E': ' ·',
        'F': ' ··-·',
        'G': ' --·',
        'H': ' ····',
        'I': ' ··',
        'J': ' ·---',
        'K': ' -·-',
        'L': ' ··-·',
        'M': ' --',
        'N': ' -·',
        'O': ' ---',
        'P': ' ·--·',
        'Q': ' --·-',
        'R': ' ·-·',
        'S': ' ···',
        'T': ' -',
        'U': ' ··-',
        'V': ' ···-',
        'W': ' ·--',
        'X': ' -··-',
        'Y': ' -·--',
        'Z': ' --·'
    }

    # A list called result which will store all of the morse code letters from the word.
    result = []
    # Looping through each letter in the word from the variable word_input to later on replace the letters with their morse code value.
    for letter in word_input:

        # If the input which is put into the uppercase letter is present in the tuple above (morse_code_mapping):
        if letter.upper() in morse_code_mappings:
            # append the equivilant morse code letter of the letter to the result list.
            result.append(morse_code_mappings[letter.upper()])

        # Else if the letter is a space:
        elif letter == ' ':
            # append a space.
            result.append('   ')

        else:
            # Else print that there is not such a letter.
            raise ValueError("No such letter")

    # Add the result to an empty string and print it.
    print(''.join(result))


# Calling the function
convert_to_morse_code(word_input)


# EXPLANATION AS FULL TEXT
# The code provided is a Python program that converts a given word into Morse code. It takes an input word, converts it
# into a string, and then converts each letter of the word into its corresponding Morse code representation. The Morse
# code mappings are stored in a dictionary, and the program loops through each letter of the word, checks if it exists
# in the dictionary, and appends the corresponding Morse code to a result list. Finally, the program joins the Morse code
# letters in the result list and prints the converted word in Morse code.
