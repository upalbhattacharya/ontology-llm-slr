#!/usr/bin/env python

"""Extracting Papers from ArXiv"""

import os
import arxiv
import arxiv2bib

client = arxiv.Client()
search = arxiv.Search(query="all:ontolog* AND (all:LLM* OR all:language model*)")
first_result = next(client.results(search))
idx = 
print(arxiv2bib.arxiv2bib([str(first_result)]))
