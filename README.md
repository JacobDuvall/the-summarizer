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

#### Summarize documents clusters -- summarize_documents()
This function takes a list of strings, tokenizes them into sentences, extracts the best summarizing sentences using Text Rank, and then selects the top 8 best summary sentences to write.

#### Write summarized clusters to a file -- write_summary_to_file()
This function writes the summaries generated from summarize_documents to SUMMARY.md


