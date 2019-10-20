import numpy as np
import pdb
import nltk
import re


path = '../../data/raw_text.txt'

with open(path) as f:
    lines = f.readlines()

text = ''

for line_chunk in lines:
    lines = line_chunk.split(' ')
    text += ' '.join(lines)

sentences = re.split(r'[.!?]\s*', text)

with open('lines.txt', 'w') as f:
    for sentence in sentences:
        f.write(sentence+'\n')
pdb.set_trace()