# cs5293sp20-project2
# Author: Jacob Duvall


# Description:
This program extracts and examines COVID-19 articles made available via https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge. With the articles loaded locally, I sample a percentage of them for analysis. This analysis creates clusters via KMeans clustering to examine similaries and the clusters and analyzed via their Silhouette Coefficients to find the optimal clustering size. Finally, summaries of each article are extracted by creating analytic matrices through TfidfVectorizer and TextRank where the summaries are printed to the file SUMMARY.md.

# Process:
The process of the code is outlined and explained as follows:
A user passes in an argument into the terminal via the command:

 - python main.py --input demo_files/JimWalmsley.txt --output demo_files_redacted/ --names --genders --dates --concept state --stats stdout
OR
 - pipenv run python main.py --input demo_files/JimWalmsley.txt --output demo_files_redacted/ --names --genders --dates --concept state --stats stdout
OR 
 - py main.py --input demo_files/JimWalmsley.txt --output demo_files_redacted/ --names --genders --dates --concept state --stats stdout

python worked for me in pycharm, py worked for my in windows powershell, pipenv worked on linux; 

WHERE the arguments are defined as:
--input: a glob of files to be redacted
--output: the directory where redactions will be made
--names: flag that takes no arguments to redact all names
--genders: flag that takes no arguments to redact all genders
--dates: flag that thakes no arguments to redact all dates
--concept: flag that can take a list of arguments with concepts to be redacted
--stats: flag that takes either "stderr", "stdout", or a file location to write stats file

With the command passed, the program cleans the files located in the input glob. 

Clean files manages the process by extracted all files from the glob and looping through each file. For each individual file, the process checks for the flags that are turned on. 

If the names flag is turned on, then all names are redacted using a stanford model for name entity recognition.
If the genders flag is turned on, then all genders are redacted by comparing the words of the document with gender words I found online.
If the dates flag is turned on, then all dates are redacted by searching the document for dates using the search_dates function from dateparser.
If the concepts flag is turned on, then all concepts related to the concept all redacted by using the synonym of all words specified.
If the stats flag is turned on, then the stats of the removed words are all formattted in a dictionary and they are shown via stderr, stdout, or written to a file for storage. 

# How To Run:
 From terminal, run via: python main.py --input <glob file> --output <directory> --names --genders --dates --concept <[list of concepts]> --stats <stdout,stderr,file_location/name>
  where names, genders, dates, concept, and stats are optional
 
 Some examples of this look like: 
 - python main.py --input demo_files/JimWalmsley.txt --output demo_files_redacted/ --names --genders --dates --concept state --stats stdout
- python main.py --input demo_files/JimWalmsley.txt --output demo_files_redacted/ --names
- python main.py --input demo_files/JimWalmsley.txt --output demo_files_redacted/ --names --stats stderr
 
 # Test File:
 My code has a test file called test_functions. 
 The test file tests that names, genders, dates, and concepts are all working at they should.
 
 To run the test file, execute command: pipenv run python -m pytest.
 
# Summary of all functions:
 #### main.py
 ##### main(arguments)
 - arguments from terminal
 * This function passes into project_1 and controls the workflow.
 
 #### project_1.py
 #### clean_files(arguments)
 - arguments from terminal
 * Takes arguments from terminal; Downloads nltk files; controls stats; collects all files using glob; cleans the files;
 
 #### download_nltk_stuff
 * These are nltk models necessary to run the program
 
 #### process_file_flags(dirty_string, arguments)
 - dirty_string to process
 - arguments from terminal
 - Process the file flags (name, gender, date, concept)
 
 #### redact_names(old_string)
 - dirty_string to process
 - Redacts all names from the file using StanfordNERTagger
 
 #### redact_genders(old_string)
 - dirty_string to process
 - Redact all genders and gendered words from the file

#### redact_dates(old_string)
- dirty string to process
- redact all dates from the file

#### redact_concepts(old_string, concept):
- dirty string to process
- concept to be redacted
- redact a specified concept

#### write_redacted_file(file_name, clean_string, directory)
- file name to write
- cleaned up string to write into file
- directory for file
- write the redacted file with new name to directory specified

#### write_stats(stats, output)
- stats dictionary
- ooutput type
- write the stats to stderr, stdout, or a file


# Discussion to cover all the discussion points
I am happy with how my program works overall. Names are accurately removed using the stanford model. This took a ton of work to set up and get working properly. Dates are removed well using the date parser. Sometimes they are a little liberal in what they remove but I think this is better than the alternative and writing regular expressions for everything else would under redact and be too time consuming. The gender list is a little long but it removes genders. And for concepts, I like my implementation of removing sentences with synonyms of a concept. Given more time I was working to implemenent a function to remove phone numbers using regular expression. 
