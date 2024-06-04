# Word To Binary

# Creating a variable which takes user input, converts it into a string and saves it as a list.
word_input = list(str(input()))

# Function with binary mapping to later append the equvilant binary letter.


def converter(word_input):
    # Dictionary containing the binary version of upper- and lowercase letters
    binary_mapping = {
        # uppercase letters
        'A': ' 01000001',
        'B': ' 01000010',
        'C': ' 01000011',
        'D': ' 01000100',
        'E': ' 01000101',
        'F': ' 01000110',
        'G': ' 01000111',
        'H': ' 01001000',
        'I': ' 01001001',
        'J': ' 01001010',
        'K': ' 01001011',
        'L': ' 01001100',
        'M': ' 01001101',
        'N': ' 01001110',
        'O': ' 01001111',
        'P': ' 01010000',
        'Q': ' 01010001',
        'R': ' 01010010',
        'S': ' 01010011',
        'T': ' 01010100',
        'U': ' 01010101',
        'V': ' 01010110',
        'W': ' 01010111',
        'X': ' 01011000',
        'Y': ' 01011001',
        'Z': ' 01011010',
        # lowecase letters
        'a': ' 01100001',
        'b': ' 01100010',
        'c': ' 01100011',
        'd': ' 01100100',
        'e': ' 01100101',
        'f': ' 01100110',
        'g': ' 01100111',
        'h': ' 01101000',
        'i': ' 01101001',
        'j': ' 01101010',
        'k': ' 01101011',
        'l': ' 01101100',
        'm': ' 01101101',
        'n': ' 01101110',
        'o': ' 01101111',
        'p': ' 01110000',
        'q': ' 01110001',
        'r': ' 01110010',
        's': ' 01110011',
        't': ' 01110100',
        'u': ' 01110101',
        'v': ' 01110110',
        'w': ' 01110111',
        'x': ' 01111000',
        'y': ' 01111001',
        'z': ' 01111010'
    }

    # Result list to save the binary version in.
    result = []

    # Loop to get each letter in the word.
    for letter in word_input:
        # If the letter is in the mapping:
        if letter in binary_mapping:
            # append the binary version of that letter.
            result.append(binary_mapping[letter])
        # Else if the letter is a space:
        elif letter == ' ':
            # append a space.
            result.append('   ')
        # Else if nothing is true:
        else:
            # raise an Error telling the user that the word contains an unsupported letter
            raise ValueError('Word contains invalid letter...' +
                             '\nLetter raising Error: ' + '"' + letter + '"' + '\n')

    # Printing the result variable.
    print(''.join(result))


# Calling the function.
converter(word_input)
