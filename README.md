# cs5293sp20-project2
# Author: Jacob Duvall


# Description:
This program extracts and examines COVID-19 articles made available via https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge. With the articles loaded locally, I sample a percentage of them for analysis. This analysis creates clusters via KMeans clustering to examine similaries and the clusters and analyzed via their Silhouette Coefficients to find the optimal clustering size. Finally, summaries of each article are extracted by creating analytic matrices through TfidfVectorizer and TextRank where the summaries are printed to the file SUMMARY.md.

# Process:
The process of the code is outlined and explained as follows:
This project is primarily an analysis based project. There are two paths one can take to follow along. First, I have uploaded a Jupyter notebook that can simply be analyzed to gain the insight of the project. If not this, then one can examine my code in main.py and the_summarizer.py to run the code within their own environment. 

The code has 6 primary functions:
1. Look at the format of the file.
2. Choose documents.
3. Files reader.
4. Cluster documents.
5. Summarize documents clusters.
6. Write summarized clusters to a file.

# Summary of all functions
#### Look at the format of the file -- look_at_the_format_of_the_file()
This function takes the json_schema.txt file supplied from the Kaggle repo and examines the json description the author provides.

#### Choose documents -- choose_documents()
This function takes a glob of the directory and a percent of files to examine and returns a random percent sampling of those files.

#### Files reader -- files_reader()
This function takes a list of sampled files and returns the content of those files in a single large document with their text.

#### TFIDF Vectorizer -- tfid_vectorize()
This function takes a document list and tokenizes it into a matrix using TfidfVectorizer

#### Count Vectorizer -- count_vectorize()
This function takes a document list and tokenizes it into a matrix using CountVectorizer

#### Cluster documents -- cluster_documents()
This function takes a tokenized document and clusters it using KMeans cluster; It finds the ideal n_clusters using the silhouette score.

#### Best cluster -- best_cluster()
takes the count vectorizer model, the tokenized matrix, and the n_clusters ideal size to visualize the feature names of the clusters.

#### Summarize documents clusters -- summarize_documents()
This function takes a list of strings, tokenizes them into sentences, extracts the best summarizing sentences using Text Rank, and then selects the top 8 best summary sentences to write.

#### Write summarized clusters to a file -- write_summary_to_file()
This function writes the summaries generated from summarize_documents to SUMMARY.md

# Discussions
## Discussion of data format
The json file format makes the text extraction easy to work with an examine. This data format is extracted and analyzed in the json_schema file supplied by the Kaggle repo. It was very helpful for me to easily extract out the information I needed. Since I only wanted to look at the actual text of the articles, I was able to throw out a lot of things immediately. For instance, I didn't necessarily care about the paper_id or some of the various other forms of metadata supplied within each file. Rather, I was immediately drawn to the fields that contained raw textual content like abstract, text, and body_text. Upon further examination, I found that all the information I needed for extracting and examining the raw text was stored within the body_text, so I got all my text from here. To do this, I just took every line from the body_text and complied them together into one document string so that everything for that one file was stored as one long string. Then I placed every other document in this same format and compiled them all into a list. This clean json_schema format helped me to easily compile all of this data for analysis.

## Discussion of tokenizer
For this analysis, I analyzed two tokenizers. The first I looked at was the TFIDF_Tokenizer. The TF_IDF (Term Frequency-Inverse Document Frequency) model is a combination of two metrics. The technique was developed as a metric for showing search engine results based on user queries. It has become part of information retrieval and text feature extraction. I liked this model a lot for summarizing documents, but I found it not as good for clustering. I also looked at the CountVectoizer model. This model is similar to TF-IDF, but rather than counting the value proportionally and offsetting that count by corpus, it just count raw word frequency. It is as simple as that. I found them both useful here and I am glad that I experimented in analysis using both.

## Discussion of clustering method
For the clustering aspect of the analysis, I looked to KMeans clustering. I found this clustering method to be particularly easy to implement so I worked with it. KMeans clustering works on textual data similar to how it works on numeric data. it tries to cluster data into groups of equal variance and minimize its inertia. The model is very popular for analysis because it scales well for large data. To implement the clustering I tokenized the data as previously discussed, and then I fit the data to the model. To find the best n_clusters, I used the silhouette score to measure. With the best n_clusters found, I then wrote a function using all of this discovered information to analyze the cluster centers and look at some of the feature names discovered within these clusters.

## Discussion of summarization
Reading through every coronavirus file found in the Kaggle repo would be beneficial, but hard to do. There are tens of thousands of articles in the repository. It would be much easier to read through these files to find the ones that would help us the most if they were summarized. The summarization part of the analysis does this. It breaks down the articles into their most useful sentences for summarization. The process to do this takes an articles string and vectorizes the string. The string is then broken into an array where it is multiplied using linear algebra and put into a similarity matrix. This similarity matrix can then be put into a graph via the networkx library. Once it is formatted in this fashion, the sentences can be ranked via Text Rank and scored. This score then helps us find the best summarization sentences. The summarization sentences can then be written to a file where they are used for summary purposes. 


