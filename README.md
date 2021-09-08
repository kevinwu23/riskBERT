# riskBERT

This repository contains files used to pull abstracts related to genes from PubMed.

The full list of 92 genes are located in `files/genes.csv`, and a union of lists from the following sites:
  - https://www.invitae.com/en/physician/tests/01101/
  - https://www.ambrygen.com/clinician/genetic-testing/1/oncology/cancernext
  - https://myriad.com/products-services/hereditary-cancers/myrisk-hereditary-cancer/

The file `query.py` contains a script to pull abstracts from PubMed given a date range and query term.

Once the abstracts are downloaded, `process_abstracts.py` can be used to convert them for the task of masked language modeling (MLM).

Finally, `run_mlm.py` can be used to train a BERT model using HuggingFace.
