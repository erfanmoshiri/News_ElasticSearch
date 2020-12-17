from elasticsearch import Elasticsearch
from elasticsearch import helpers

import utility
from pathlib import Path
class index_data():
    def __init__(self):
        self.es =  Elasticsearch()
    def create_or_index(self):
        if not self.es.indices.exists(index="asr_iran"):
            print("index Doesnt exists")
            print("index Created")
        else:
            self.es.indices.delete("asr_iran")
            print("index Deleted")
    def insert(self):
        self.es.indices.create(index="asr_iran", body={"mappings": {
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


        docs = utility.convertToArrayDictionary(Path("./Data/100_news.json"))

        activity = [{
            "_index" : "asr_iran",
            "_source" : news
        }
        for news in docs
        ]

        helpers.bulk(self.es, activity)

        print("indexed successfuly")