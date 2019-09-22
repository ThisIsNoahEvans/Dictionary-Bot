###This is used to test that you can read and select random words from the words.txt file###

import random

with open('words.txt') as word:
        #Scans The File
        lines = word.readlines()
        #Prints Random Word
        print(random.choice(lines))
