#!/usr/bin/env python

"""Extracting Papers from ArXiv"""

import arxiv
import arxiv2bib

client = arxiv.Client()
search = arxiv.Search(query="all:ontolog* AND (all:LLM* OR all:language model*)")
first_result = next(client.results(search))
print(first_result)
print(arxiv2bib.arxiv2bib([first_result]))
