#!/usr/bin/env python

"""Extracting Papers from ArXiv"""

import os
from time import sleep

import arxiv
import arxiv2bib
import tqdm

client = arxiv.Client(page_size=900, delay_seconds=10.0, num_retries=5)
search = arxiv.Search(
    query="all:ontolog* AND all:LLM* OR all:ontolog* AND all:language model*",
    sort_by=arxiv.SortCriterion.SubmittedDate,
    sort_order=arxiv.SortOrder.Descending,
)
ids = []
fullpaths = []

for result in tqdm.tqdm(client.results(search)):
    try:
        print(fullpaths)k
        fullpaths.append(str(result))
        ids.append(os.path.basename(str(result)))
    except:
        break
with open(
    "/home/upal/Projects/ontology-llm-slr/code/sources/parts/arxiv/id_list.txt", "w"
) as f:
    f.writelines(idx + "\n" for idx in ids)
with open(
    "/home/upal/Projects/ontology-llm-slr/code/sources/parts/arxiv/full_https.txt",
    "w",
) as f:
    f.writelines(idx + "\n" for idx in fullpaths)

with open(
    "/home/upal/Projects/ontology-llm-slr/code/sources/parts/arxiv/id_list.txt", "w"
) as f:
    f.writelines(idx + "\n" for idx in ids)
with open(
    "/home/upal/Projects/ontology-llm-slr/code/sources/parts/arxiv/full_https.txt",
    "w",
) as f:
    f.writelines(idx + "\n" for idx in fullpaths)
