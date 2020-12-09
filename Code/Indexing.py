from elasticsearch import Elasticsearch
from elasticsearch import helpers

import utility
from pathlib import Path

es = Elasticsearch()

if not es.indices.exists(index="asr_iran"):
    print("index Doesnt exists")
    print("index Created")
else:
    es.indices.delete("asr_iran")
    print("index Deleted")

es.indices.create(index="asr_iran", body={"mappings": {
    "properties": {
        "Body": {
            "type": "text",
            "analyzer": "parsi"
        },
        "Category": {
            "type": "text",
            "analyzer": "parsi"
        }
    }
}})


docs = utility.convertToArrayDictionary(Path("Data/news.json"))

activity = [{
 
    "_index" : "asr_iran",
    "_source" : news
    }
    for news in docs
]

helpers.bulk(es, activity)

print("indexed successfuly")