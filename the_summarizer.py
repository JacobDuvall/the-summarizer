import random
import glob
from sklearn.metrics import silhouette_score
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.cluster import KMeans
import json
import pickle
import nltk
import numpy as np
import networkx
import os


# look at the format of the json schema
def look_at_the_format_of_the_file(file):
    file = open(file, 'r')
    print(file.read())


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

    return single_large_document_list


# use tfidfvectorizer on the documents to get the matrix
def tfid_vectorize(doc):
    tv = TfidfVectorizer(min_df = 0., max_df=1., use_idf=True)
    tv_matrix = tv.fit_transform(doc)
    pickle.dump(tv_matrix, open('yummy_pickle.pkl', 'wb'))
    return tv, tv_matrix


# use countvectoizer on the documents to get the matrix
def count_vectorize(doc):
    cv = CountVectorizer()
    cv_matrix = cv.fit_transform(doc)
    pickle.dump(cv_matrix, open('yummy_pickle_cv.pkl', 'wb'))
    return cv, cv_matrix


# Takes tokenized documents and clusters them -- Uses Silhouette Coefficient to measure cluster quality.
# Records the documents that are part of each cluster
def cluster_documents(doc_list):
    cv, tokenized_files = count_vectorize(doc_list)
    cluster_range = list(range(2, 8))
    for n_clusters in cluster_range:
        km = KMeans(n_clusters=n_clusters)
        km_predicts = km.fit_predict(tokenized_files)
        pickle_save = 'pickle_km_' + str(n_clusters) + '.pkl'
        pickle.dump(km_predicts, open(pickle_save, 'wb'))

        score = silhouette_score(tokenized_files, km_predicts)
        print("Number of clusters: {}, Silhouette Score: {}".format(n_clusters, score))
    return cv, tokenized_files


# fits the best cluster size and shows the feature names
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


# summarize the documents looking at their top 8 sentences through TextRank
def summarize_documents(string_list):
    count = 0
    for string in string_list:
        sentences = nltk.sent_tokenize(string)
        try:
            if len(sentences) < 8:
                raise Exception
        except Exception:
            continue
        tv, tv_matrix = tfid_vectorize(sentences)
        try:
            tv_matrix = tv_matrix.toarray()
        except:
            print('too large')
            continue
        similarity_matrix = np.matmul(tv_matrix, tv_matrix.T)
        try:
            similarity_graph = networkx.from_numpy_array(similarity_matrix)
        except MemoryError:
            print('memory error 1')
            continue
        try:
            scores = networkx.pagerank(similarity_graph)
        except MemoryError:
            print('memory error')
            continue

        ranked_sentences = sorted(((score, index) for index, score in scores.items()), reverse=True)
        top_sentenc_indices = [ranked_sentences[index][1] for index in range(8)]

        top_sentenc_indices.sort()
        write_summary_to_file(count, np.array(sentences)[top_sentenc_indices])
        count += 1


# write the summaries generated from summarize_documents() to file
def write_summary_to_file(count, summary_array):
    print(count)
    if count < 1:
        try:
            os.remove("SUMMARY.md")
        except:
            pass
        file = open("SUMMARY.md", "w",  encoding='utf-8')
        header = 'This file was generated using TextRank summarization. The process taken was to extract ' \
                 'a random percent sampling of pdf_json files from ' \
                 'https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge. With these ' \
                 'files extracted, I then opened all files, tokenized the sentences of the ' \
                 'files using tfid vectorizer, ' \
                 'and then applied a TextRank algorithm to the tokenized docs. This TextRank allowed me to then ' \
                 'extract the 8 most useful summarized sentences. And voila!'
        file.write(header)
        file.write('\n\n')
        file.close()

    file = open("SUMMARY.md", "a",  encoding='utf-8')
    file.write(str(summary_array))
    file.write('\n\n')
    file.close()