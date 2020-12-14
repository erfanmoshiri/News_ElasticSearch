import requests
from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
print(es.search(index='asr_iran',body={
    "query": {
        "function_score": {
            "query": {"match_all": {}},
            "boost": "5",
            "functions": [
                {
                    "filter": {"match": {"Category": "سیاسی"}},
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
})
)