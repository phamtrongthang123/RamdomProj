from typing import *
from collections import defaultdict
import numpy as np

def soft_tf_idf(documents: List[List], query: List):
    tf = {}
    idf = defaultdict(int)
    count = defaultdict(int)
    for i,doc in enumerate(documents):
        tf[i] = defaultdict(int)
        n = len(doc)
        count_i = defaultdict(int) 
        for term in doc:
            tf[i][term] += 1 / n 
            count_i[term] += 1 
        for k,v in count_i.items():
            count[k] += min(1,v) 
    
    for k,v in count.items():
        idf[k] = np.log10(len(documents) / (v)) +1

    tf_idf_doc = {}
    for i,doc in enumerate(documents):
        tf_idf_doc[i] = {}
        for term in doc:
            tf_idf_doc[i][term] = tf[i][term] * idf[term] 

    tf_query = defaultdict(int)
    tf_idf_query = defaultdict(int)
    for term in query:
        if term in idf.keys():
            tf_query[term] += 1 / len(query)
            # note that we use assign here, so only max tf_query will remain after looping all term
            tf_idf_query[term] = tf_query[term] * idf[term]
    return  tf_idf_doc, tf_idf_query

def cosine_similarity(tf_idf_doc, tf_idf_query):
    vector_compare = {}
    denomirator_query = 0
    for k,v in tf_idf_query.items():
        denomirator_query += v*v 
    for i,doc in tf_idf_doc.items():
        numerator = 0
        denomirator_doc = 0
        for term_doc,v in doc.items():
            numerator += v * tf_idf_query[term_doc]
            denomirator_doc += v*v 
        vector_compare[i] = numerator / (np.sqrt(denomirator_doc) * np.sqrt(denomirator_query))
    return vector_compare
    

if __name__=="__main__":
    doc_1 = 'a a b a b c'
    doc_2 = 'b b b c'
    doc_3 = 'c d d d c a'
    documents =[doc_1.split(), doc_2.split(), doc_3.split()]
    query = 'b c e'.split()
    tf_idf = soft_tf_idf(documents, query)
    cosine_compare = cosine_similarity(*tf_idf)
    max_key = max(cosine_compare, key=cosine_compare.get)
    print("Best match is: doc", max_key)
