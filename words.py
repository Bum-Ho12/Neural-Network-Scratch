import nltk
import re, numpy as np#, pandas as pd


corpus = ['The sky is blue and beautiful.',
    'Love this blue and beautiful sky!',
    'The quick brown fox jumps over the lazy dog.',
    'The brown fox is quick and the blue dog is lazy!',
    'The sky is very blue and the sky is very beautiful today',
    'The dog is lazy but the brown fox is quick!'
    ]
# labels = ['weather', 'weather', 'animals', 'animals', 'weather', 'animals']
# corpuses = np.array(corpus)
# corpus_df = pd.DataFrame({'Document': corpuses,
#     'Category': labels})
# corpus_df = corpus_df[['Document', 'Category']]
# print(corpus_df)

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