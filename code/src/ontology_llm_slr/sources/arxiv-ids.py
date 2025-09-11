#!/usr/bin/env python

"""Extracting Papers from ArXiv"""

import os
from time import sleep

import arxiv
import arxiv2bib
import tqdm

client = arxiv.Client()
search = arxiv.Search(query="all:ontolog* AND (all:LLM* OR all:language model*)")
ids = []
fullpaths = []

try:
    for i, result in tqdm.tqdm(enumerate(client.results(search))):
        fullpaths.append(str(result))
        ids.append(os.path.basename(str(result)))
        if i % 100 == 0:
            sleep(3)
except:
    with open(
        "/home/upal/Projects/ontology-llm-slr/code/sources/parts/arxiv/id_list.txt", "w"
    ) as f:
        f.writelines(idx + "\n" for idx in ids)
    with open(
        "/home/upal/Projects/ontology-llm-slr/code/sources/parts/arxiv/full_https.txt",
        "w",
    ) as f:
        f.writelines(idx + "\n" for idx in fullpaths)
