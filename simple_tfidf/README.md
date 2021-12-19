# Installation 

First we install environment by `pip install -r requirements.txt`, then just use it. Example show in `main.py`
```python
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
```

## Crawl 
To crawl new data to use instead of using `src/data_19.12.2021.json`, we only need to look at `src/craw_now.py` to change the query text and saved file's name at the end.  