from src.tfidf import * 
from src.utils import * 
import json 

def retrieve(documents, query):
    tok_query = tokenize(query)

    tfidf_matrix = soft_tf_idf(documents, tok_query)
    cosine_compare = cosine_similarity(*tfidf_matrix)
    max_key = get_max_key_dict(cosine_compare)
    return " ".join(documents[max_key])

with open("src/data_19.12.2021.json", encoding='utf-8') as f:
    documents = json.load(f) 

query = "modern research?"
best_match = retrieve(documents, query)
print("Best match for query '{}' is: {}".format(query, best_match))

query = "How to do modern research?"
best_match = retrieve(documents, query)
print("Best match for query '{}' is: {}".format(query, best_match))