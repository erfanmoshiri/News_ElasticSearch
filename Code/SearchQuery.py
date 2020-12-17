from elasticsearch import Elasticsearch

class search_query():
    def __init__(self):
        self.es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


    def search_on_category(self, w1, w2, w3, w4):

        query = "(" + "سیاسی" + ")^{} (".format(w1) + "اقتصادی" + ")^{} (".format(w2) + "اجتماعی" + ")^{} (".format(w3)+ "بین الملل" + ")^{}".format(w4)
        print(query)

        search_param = {
            "query": {
                "query_string": {
                    "query": query,
                    "default_field": "Category"
                }
            }
        }
        # get another response from the cluster
        response = self.es.search(index='asr_iran', body=search_param, request_timeout=40)
        return response
    def search_on_body(self, w1, w2, w3, w4):
        query = "(" + "سیاسی" + ")^{} (".format(w1) + "اقتصادی" + ")^{} (".format(w2) + "اجتماعی" + ")^{} (".format(w3)+ "بین الملل" + ")^{}".format(w4)
        print(query)
        search_param = {
            "query": {
                "query_string": {
                    "query": query,
                    "default_field": "Body"
                }
            }
        }
        response = self.es.search(index='asr_iran', body=search_param, request_timeout=40, size="1000")
        return response
