#!/usr/bin/env python

"""Extracting Papers from ArXiv"""

import os

import arxiv
import arxiv2bib
import tqdm

client = arxiv.Client()
search = arxiv.Search(query="all:ontolog* AND (all:LLM* OR all:language model*)")
ids = []

try:
    for result in tqdm.tqdm(client.results(search)):
        ids.append(os.path.basename(str(result)))
except:
    with open(
        "/home/upal/Projects/ontology-llm-slr/code/sources/parts/arxiv/id_list.txt", "w"
    ) as f:
        f.writelines(ids)
