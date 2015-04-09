from string import ascii_lowercase
key = dict(zip(ascii_lowercase, ascii_lowercase[::-1]))


def five(word):
    """This function takes a string (word) and splits it into sections of five, with a space between each grouping."""
    if len(word) <= 5:
        return word
    return word[:5]+" "+five(word[5:])


def encode(word):
    """ This function takes a word and encodes it using an atbash cipher """
    word = [c for c in word.lower() if c.isalnum()]
    encoded_string = ''
    for c in word:
        if c in ascii_lowercase:
            encoded_string += key[c]
        else:
            encoded_string += c
    encoded_string = five(encoded_string)
    return encoded_string


def decode(word):
    """ This function takes a word in the cipher and returns it decoded, without spaces if necessary """
    word = [c for c in word.lower() if c.isalnum()]
    decoded = ''
    for c in word:
        decoded += key[c]
    return decoded
