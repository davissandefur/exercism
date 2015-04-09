key = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}

reverse = 'zyxwvutsrqponmlkjihgfedcba'


def five(word):
    """This function takes a string (word) and splits it into sections of five, with a space between each grouping."""
    if len(word) <= 5:
        return word
    return word[:5]+" "+five(word[5:])


def encode(word):
    """ This function takes a word and encodes it using an atbash cipher """
    word = word.lower()
    word = word.strip()
    word = word.replace(',', '')
    word = word.replace('.', '')
    word = word.replace(' ', '')
    encoded_string = ''
    for c in word:
        if c in reverse:
            encoded_string += str(reverse[key[c]])
        else:
            encoded_string += str(c)
    encoded_string = five(encoded_string)
    return encoded_string


def decode(word):
    """ This function takes a word in the cipher and returns it decoded, without spaces if necessary """
    word = word.lower()
    word = word.replace(" ",'')
    decoded = ''
    for c in word:
        decoded += str(reverse[key[c]])
    return decoded
