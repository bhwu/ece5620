# Needed for struct.pack

import struct

# Initialize our list of phrases

prefices_tuple = (
        '',
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z',
       '\n',
        ' ',
        '!',
        '"',
        '&',
        '\'',
        '(',
        ')',
        ',',
        '-',
        '.',
        '0',
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        ':',
        ';',
        '?',
)

alphabet = list(enumerate(prefices_tuple));
dictionary = list(enumerate(prefices_tuple));

# Function that returns the longest phrase, and its index, that is a 
# prefix of the given string

def find_encoding(en, string):

    for k, w in reversed(en):
        if string.startswith(w):
            return k,w
    return -1,''


# Open the input and output files. Compressed will be a text file

fin = open('austen.txt','r')
fout = open('compressed','wb')

# Read in the entire text file

data = fin.read();

indices = list()
nextChars = list()

# Data-parsing loop
while (data != ''):
    # find the longest phrase that is a prefix in data -> add it to list of indices
    [index, phrase] = find_encoding(dictionary, data)
    data = data[len(phrase):]
    indices.append(index)
    # check the next letter -> add its index in alphabet to list of nextChars
    if(data !=''):
        [alph_ind, char] = find_encoding(alphabet, data)
        nextChars.append(alph_ind)
        data = data[1:]
    else:
        nextChars.append(0)
    # Use the aforementioned phrase and char to construct a new dictionary entry
    dictionary.append((len(dictionary),phrase+char))

# Encoding indices loop
for i in range(0, len(indices)):
    fout.write(struct.pack("<I",indices[i]))

# Encoding nextChars loop
fout.write('\n\n\n\n\n\n\n\n\n\n')
sextuple = 0
encoding = 0
outbytes = bytearray(4)
for i in range(0,len(nextChars)):
    encoding += nextChars[i] << (6*sextuple)
    if(sextuple<3):
        sextuple +=1
    else:
        outbytes = struct.pack("<I", encoding)
        fout.write(outbytes[0:3])
        sextuple = 0
        encoding = 0
if sextuple !=0:
    outbytes = struct.pack("<I", encoding)
    fout.write(outbytes[0:3])
    sextuple = 0
    encoding = 0
# Close the input and output files

fin.close()
fout.close()
