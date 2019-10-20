from tqdm import tqdm
import pdb
import nltk
import pandas as pd
import re

'''
Convert dictionary of abstracts into a .txt:
    - One sentence per line
    - Empty sentence for new abstract.
'''

def dictionary_to_lines(abstracts_path, output_path):

    regex_tokenizer = nltk.RegexpTokenizer("\w+")

    df = pd.read_pickle(abstracts_path)
    f = open(output_path, 'w')

    for abstract_id in tqdm(df):

        text = df[abstract_id]
        sentences = re.split(r'[.!?]\s', text)

        for sentence in sentences:

            sentence = sentence.encode('utf-8', 'ignore')
            sentence = " ".join(regex_tokenizer.tokenize(sentence))
            f.write(sentence + '\n')

        f.write('\n')

    f.close()

if __name__ == '__main__':

    abstracts_path = '../data/abstracts.pkl'
    output_path = '../data/processed.txt'

    dictionary_to_lines(abstracts_path, output_path)