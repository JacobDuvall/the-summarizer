import the_summarizer
import glob

sampling_of_files = the_summarizer.choose_documents(glob.glob('C:\\Users\\jdale\\OneDrive\\School'
                                                              '\\Text Analytics\\*\\*\\pdf_json'), .0025)

the_summarizer.text_rank(sampling_of_files)