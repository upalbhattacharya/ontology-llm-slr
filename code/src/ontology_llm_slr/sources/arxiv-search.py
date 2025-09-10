#!/usr/bin/env python

"""Extracting Papers from ArXiv"""

import os

import arxiv
import arxiv2bib

client = arxiv.Client()
search = arxiv.Search(query="all:ontolog* AND (all:LLM* OR all:language model*)")
first_result = next(client.results(search))
idx = os.path.basename(str(first_result))
print(arxiv2bib.arxiv2bib([idx]))
