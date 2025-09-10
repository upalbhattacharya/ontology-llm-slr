#!/usr/bin/env python

"""Querying ACL Anthology for papers"""

import re
from acl_anthology import Anthology

anthology = Anthology.from_repo()

for paper in anthology.papers():
    
