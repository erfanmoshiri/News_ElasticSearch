
#!/usr/bin/env python
 
# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch


def weightedSearchQuery(part1, part2, part3, index):

    # sample input
    #query = 'hi'
    #turn_num= "1_1"

    es = Elasticsearch()

    print(es.indices.exists("asr_iran"))

    # return es.get(index="asr_iran", id=35)

    #query = "(" + part1 + ")^1 (" + part2 + ")^2 (" + part3 + ")^3"


    # search_param={
    #     "query": {
    #         "multi_match": {
    #                 "query":query,
    #                 "analyzer": "parsi",
    #                 "default_field":"Body"
    #         }
    #     }
    # }
    # q = "ایران"

    # search_param = {
    #     "query": {
    #         "multi_match": {
    #             "query": q,
    #             "fields": ["Body"]
    #         }
    #     }
    # }

    string = {'query': {
        'match_all': {}
    }}

    response = es.search(index=index, body=string)

    for doc in response['hits']['hits']:
        print (doc['_id'])
        print(doc['_source'])

    # return response
