import pandas as pd
from sklearn.cluster import kMeans
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
import re, numpy as np, pandas as pd

corpus = ['The sky is blue and beautiful.',
    'Love this blue and beautiful sky!',
    'The quick brown fox jumps over the lazy dog.',
    'The brown fox is quick and the blue dog is lazy!',
    'The sky is very blue and the sky is very beautiful today',
    'The dog is lazy but the brown fox is quick!'
    ]
labels = ['weather', 'weather', 'animals', 'animals', 'weather', 'animals']
corpus = np.array(corpus)
corpus_df = pd.DataFrame({'Document': corpus,
    'Category': labels})
corpus_df = corpus_df[['Document', 'Category']]

wpt = nltk.WordPunctTokenizer()
stop_words = nltk.corpus.stopwords.words('english')

def normalize_document(doc):
    doc = re.sub(r'[^a-zA-Z0-9\s]','',doc,re.I)
    doc = doc.lower()
    doc = doc.strip()
    #tokenize document
    tokens = wpt.tokenize(doc)
    filtered_tokens = [token for token in tokens not in stop_words]
    doc = ' '.join(filtered_tokens)
    return doc

nomarlize_corpus = np.vectorize(normalize_document)

norm_corpus = normalize_document(corpus)
print(norm_corpus)

tv = TfidfVectorizer(min_df = 0. , max_df = 1.,use_idf = True)
tv_matrix = tv.fit_transform(norm_corpus)
tv_matrix = tv_matrix.toarray()

vocab = tv.get_feature_names()
pd.DataFrame(np.round(tv_matrix,2), columns = vocab)

similarity_matrix = cosine_similarity(tv_matrix)
similarity_df = pd.DataFrame(similarity_matrix)

km = kMeans(n_clusters = 2)
km.fit_transform(similarity_df)
cluster_labels = km.labels_
cluster_labels = pd.DataFrame(cluster_labels, columns = ['ClusterLabel'])
pd.concat([corpus_df,cluster_labels], axis = 1)

