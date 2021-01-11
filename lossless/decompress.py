# Needed for struct.unpack

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

# Open the input and output files. 'rb' is needed on some platforms
# to indicate that 'compressed' is a binary file.

fin = open('compressed','rb')
fout = open('out.txt','w')

# Read in the entire compressed file

data = fin.read();
indices = list()
nextChars = list()
separationPoint = data.find('\n\n\n\n\n\n\n\n\n\n');
indData = data[0:separationPoint]
nextData = data[separationPoint+10:]

print(len(nextData))

# nextChars parsing loop
while nextData != '':
    fourphrases = struct.unpack("<I", nextData[0:3]+'\0')[0]
    nextData = nextData[3:]
    for j in range(0,4):
        nextChars.append((fourphrases >> 6*j) & 63)
#while(len(nextChars)<separationPoint/4):
#    nextChars.append(0)
print(len(nextChars))

# Decoding loop
for i in range(0,separationPoint/4):
    indices.append(struct.unpack("<I",indData[0:4])[0])
    indData = indData[4:]
    phrase = dictionary[indices[i]][1]
    #print(i)
    next = alphabet[nextChars[i]][1]
    fout.write(phrase+next)
    dictionary.append((len(dictionary),phrase+next))
    


# Close input and output files

fin.close()
fout.close()
