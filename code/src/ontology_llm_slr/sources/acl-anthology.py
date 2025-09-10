#!/usr/bin/env python

"""Querying ACL Anthology for papers"""

import re

from acl_anthology import Anthology

anthology = Anthology.from_repo()
papers = []
bib = ""
for paper in anthology.papers():
    title = str(paper.title).lower()
    abstract = str(paper.abstract).lower()
    print(paper.year)
    if (
        (
            re.search(r"ontolog*", title)
            and (re.search(r"llm*", title) or re.search(r"language model*", title))
        )
        or (
            re.search(r"ontolog*", abstract)
            and (
                re.search(r"llm*", abstract) or re.search(r"language model*", abstract)
            )
        )
        and (int(paper.year) >= 2018 and int(paper.year) <= 2025)
    ):
        print(paper.year)
        papers.append((paper.full_id, paper.title))
        bib = bib + paper.to_bibtex(with_abstract=True)

with open("/home/upal/Projects/ontology-llm-slr/code/sources/parts/acl.bib", "w") as f:
    f.write(bib)
