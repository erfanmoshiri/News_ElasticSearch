from Code.Indexing import index_data
from Code.Learning import ML
index = index_data()
index.create_or_index()
index.insert()
ml = ML()
ml.learn_method()