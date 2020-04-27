import os
import random
import glob
from sklearn.metrics import silhouette_score
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.cluster import KMeans
import json
import pickle
import nltk
import numpy as np
import pandas as pd


# Takes glob and randomly extracts a percent of the files in a list
def choose_documents(folders, percent):
    file_list = list()
    for folder in folders:
        files = os.listdir(folder)
        for file in files:
            file_list.append(file)
    size = int(len(file_list) * (percent*(10**-2)))
    return random.sample(file_list, size)


# Takes a list of files and tokenizes the data in the files using CountVectorizer
def files_reader(files_list):
    directory = 'C:\\Users\\jdale\\OneDrive\\School\\Text Analytics\\' \
                '*\\*\\pdf_json\\'
    single_large_document_list = list()
    for file in files_list:
        dir = glob.glob(str(directory + file))
        with open(dir[0]) as file_json:
            data = json.load(file_json)
            document_string = ''
            for line in data['body_text']:
                document_string = document_string + line['text']
            single_large_document_list.append(document_string)
    #cv = CountVectorizer()
    #cv_matrix = cv.fit_transform(single_large_document_list)
    tv = TfidfVectorizer()
    tv_matrix = tv.fit_transform(single_large_document_list)
    return tv, tv_matrix


# Takes tokenized documents and clusters them -- Uses Silhouette Coefficient to measure cluster quality.
# Records the documents that are part of each cluster
def cluster_documents(tokenized_files):
    cluster_range = list(range(2, 8))
    for n_clusters in cluster_range:
        km = KMeans(n_clusters=n_clusters)
        km_predicts = km.fit_predict(tokenized_files)
        pickle_save = 'pickle_km_' + str(n_clusters) + '.pkl'
        pickle.dump(km_predicts, open(pickle_save, 'wb'))

        score = silhouette_score(tokenized_files, km_predicts)
        print("Number of clusters: {}, Silhouette Score: {}".format(n_clusters, score))


def text_rank(files_list):

    DOCUMENT = ''

    directory = 'C:\\Users\\jdale\\OneDrive\\School\\Text Analytics\\' \
                '*\\*\\pdf_json\\'
    single_large_document_list = list()
    for file in files_list:
        dir = glob.glob(str(directory + file))
        with open(dir[0]) as file_json:
            data = json.load(file_json)
            document_string = ''
            for line in data['body_text']:
                document_string = document_string + line['text']
            DOCUMENT = document_string


    nltk.download('stopwords')
    stop_words = nltk.corpus.stopwords.words('english')

    def normalize_document(doc):
        doc = doc.lower()
        doc = doc.strip()

        tokens = nltk.word_tokenize(doc)

        filtered_tokens = [token for token in tokens if token not in stop_words]

        doc = ' '.join(filtered_tokens)
        return doc

    normalize_corpus = np.vectorize(normalize_document)

    sentences = nltk.sent_tokenize(DOCUMENT)

    norm_sentences = normalize_corpus(sentences)

    tv = TfidfVectorizer(min_df = 0., max_df=1., use_idf=True)
    dt_matrix = tv.fit_transform(norm_sentences)
    dt_matrix = dt_matrix.toarray()

    vocab = tv.get_feature_names()
    td_matrix = dt_matrix.T
    print(td_matrix.shape)
    print(pd.DataFrame(np.round(td_matrix, 2), index = vocab).head(100))

def best_cluster(cv, tokenized_files, size):
    km = KMeans(n_clusters=size).fit(tokenized_files)
    feature_names = cv.get_feature_names()
    ordered_centroids = km.cluster_centers_.argsort()[:, ::-1]
    for cluster_num in range(2):
        print('CLUSTER #' +str(cluster_num+1))
        feature_list = list()
        for i in ordered_centroids[cluster_num, :10]:
            feature_list.append(feature_names[i])
        print(feature_list)

