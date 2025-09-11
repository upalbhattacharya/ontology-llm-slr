#!/usr/bin/env python

"""Extracting Papers from ArXiv"""

import os

import arxiv
import arxiv2bib
import tqdm

client = arxiv.Client(page_size=100, delay_seconds=5, num_retries=5)
search = arxiv.Search(
    query="all:ontolog* AND (all:LLM* OR all:language model*)", max_results=None
)
ids = []
fullpaths = []

try:
    for result in tqdm.tqdm(client.results(search)):
        print(str(result))
        fullpaths.append(str(result))
        ids.append(os.path.basename(str(result)))
except:
    print(fullpaths)
    with open(
        "/home/upal/Projects/ontology-llm-slr/code/sources/parts/arxiv/id_list.txt", "w"
    ) as f:
        f.writelines(idx + "\n" for idx in ids)
    with open(
        "/home/upal/Projects/ontology-llm-slr/code/sources/parts/arxiv/full_paths.txt",
        "w",
    ) as f:
        f.writelines(idx + "\n" for idx in fullpaths)
