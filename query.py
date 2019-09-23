from Bio import Entrez
from tqdm import tqdm

class Downloader:
    def __init__(self, email='kewu93@gmail.com'):

        Entrez.email = email
        self.abstracts = {}

    def search_abstracts(self, search_term, retmax):

        record = Entrez.read(Entrez.esearch(db='pubmed', retmax=retmax, term=search_term))

        for id in tqdm(record['IdList']):
            d = Entrez.read(Entrez.efetch(db='pubmed', id=id, retmax=1, retmode='xml'))
            try:
                content = d['PubmedArticle'][0]['MedlineCitation']['Article']['Abstract']['AbstractText'][0]
                self.abstracts[id] = content
            except:
                continue

    def get_abstracts(self):

        return self.abstracts

if __name__ == '__main__':

    dl = Downloader()
    search_term = '"0000/01/01"[PDAT] : "3000/12/31"[PDAT]'
    dl.search_abstracts( search_term, retmax=100)

    print(len(dl.abstracts))






