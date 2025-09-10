#!/usr/bin/env python

"""Extracting Papers from ArXiv"""

import arxiv

client = arxiv.Client()
search = arxiv.Search(query="all:ontolog* AND (all:LLM* OR all:language model*)")
first_result = next(client.results(search))
print(first_result)
