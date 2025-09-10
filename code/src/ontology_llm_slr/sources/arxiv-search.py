#!/usr/bin/env python

"""Extracting Papers from ArXiv"""

import os

import arxiv
import arxiv2bib

client = arxiv.Client()
search = arxiv.Search(query="all:ontolog* AND (all:LLM* OR all:language model*)")
ids = []

for result in client.results(search):
    ids.append(os.path.basename(str(result)))

with open(
    "/home/upal/Projects/ontology-llm-slr/code/sources/parts/arxiv/id_list.txt", "w"
) as f:
    f.writelines(ids)
