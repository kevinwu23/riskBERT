import pickle
import pdb
from tqdm import tqdm

def save_pickle(data, path):
    with open(path, 'wb') as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)

def combine_text(dict, filename):
    with open(filename, "wb") as outfile:
        for idx in tqdm(dict):
            outfile.write(dict[idx].encode('utf-8'))
    outfile.close()

def get_raw_text(filepath):
    return ''.join(open(filepath).readlines())