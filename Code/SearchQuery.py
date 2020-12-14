
#!/usr/bin/env python

# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch


# def weightedSearchQuery(part1, part2, part3, index):

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

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

# search_param = {
#     "query": {
#         "multi_match": {
#             "query": "ایران",
#             "fields": ["Body"]
#         }
#     }
# }

# string = {'query': {
#     'match_all': {}
# }}

response = es.search(index='asr_iran', body={
    "query": {
        "function_score": {
            "query": {"match_all": {}},
            "boost": "5",
            "functions": [
                {
                     "filter": {"match": {"Category": "سیاسی"}},
                     "random_score": {},
                    "weight": 30
                },
                {
                    "filter": {"match": {"Category": "اقتصادی"}},
                    "weight": 42
                },
                {
                    "filter": {"match": {"Category": "بین الملل"}},
                    "weight": 37
                },
                {
                    "filter": {"match": {"Category": "اجتماعی"}},
                    "weight": 33
                },
                {
                    "filter": {"match": {"Category": "فرهنگی"}},
                    "weight": 29
                }

            ],
            "max_boost": 42,
            "score_mode": "max",
        }
    }
}
)

# search_param={
#     "query": {
#         "query_string": {
#                 "query":"ایران + سیاسی",
#                 "analyzer": "parsi",
#                 "default_field":"Body"
#         }
#     }

# }
# response = es.search(index=index, body=search_param)

# for doc in response['hits']['hits']:
#     print (doc['_id'])
#     print(doc['_source'])

print(response)

# return response
