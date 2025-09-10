#!/usr/bin/env python

"""Querying ACL Anthology for papers"""

import re

from acl_anthology import Anthology

anthology = Anthology.from_repo()

for paper in anthology.papers():
    title = str(paper.title).lower()
    abstract = str(paper.abstract).lower()
    if re.search(r"ontolog*", title) and (
        re.search(r"llm*", title) or re.search(r"language model*", title)
    ):
        pass
