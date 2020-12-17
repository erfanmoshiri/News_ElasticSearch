import json
from pathlib import Path

from elasticsearch import Elasticsearch
from trectools import misc, TrecRun, TrecQrel, procedures,TrecEval
import gzip
import struct

from Code.SearchQuery import search_query


class calculate_map():
    def __init__(self):
        self.es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

    def map(self):
        qrels_file = TrecQrel("../Data/qrel.txt")
        path_to_runs = TrecRun("../Data/run.txt")
        te =  TrecEval(path_to_runs,qrels_file)
        dic = {"map":te.get_map(),"ndcg":te.get_ndcg()}
        return dic
    def write_qrl(self, category):
        f = open(Path("../Data/news.json"))

        data = json.load(f)
        qrel = open("../Data/qrel.txt", "a")
        qrel.truncate(0)

        for d in data:
            print(d["Category"])
            if d["Category"] == category:
                relevance = 1
            else:
                relevance = 0
            qrel.write('1 1 ' + str(d["Id"]) + " " + str(relevance) + "\n")
    def write_run(self,response,query_id):
        print(response)
        rank = 0
        with open("../Data/run.txt", "a") as f:
            f.truncate(0)
            for word in response['hits']['hits']:

                ##query-id Q0 document-id rank score STANDARD
                string = "1 1 "+str(word['_source']['Id']) +" "+str(rank)+" "+str(word['_score'])+ " "+"STANDARD"+"\n"
                rank += 1
                f.write((string))

    def cal_map(self,w1,w2,w3,w4):
        s = search_query()
        self.write_qrl("بین الملل")
        self.write_run(s.search_on_body(w1,w2,w3,w4), "id")
        print(self.map())
        return self.map()







