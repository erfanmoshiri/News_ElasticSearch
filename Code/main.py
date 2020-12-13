#!/usr/bin/env python
 
# -*- coding: utf-8 -*-

from SearchQuery import weightedSearchQuery as ws
from elasticsearch import Elasticsearch

# es = Elasticsearch()

# es.indices.delete("asr_iran")


p1 = "فرهنگی"
p2 = "سیاسی"
p3 = "اقتصادی"

res = ws(p1, p2, p3, "asr_iran")

print(" ")