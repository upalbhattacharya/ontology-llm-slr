#!/usr/bin/env python

"""Extracting Papers from ArXiv"""

import os

import arxiv
import arxiv2bib

client = arxiv.Client()
search = arxiv.Search(query="all:ontolog* AND (all:LLM* OR all:language model*)")
first_result = next(client.results(search))
idx = os.path.basename(str(first_result))

cli = arxiv2bib.Cli(id=idx)
cli.run()
cli.print_output()
print(cli.args.id)
