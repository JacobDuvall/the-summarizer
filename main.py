from the_summarizer import *


def main():

    look_at_the_format_of_the_file('C:\\Users\\jdale\\OneDrive\\School\\Text Analytics\\json_schema.txt')

    sampling_of_files = choose_documents(glob.glob(
        'C:\\Users\\jdale\\OneDrive\\School\\Text Analytics\\*\\*\\pdf_json'), 10)
    import pprint
    pprint.pprint(sampling_of_files[:10])

    string_of_files_list = files_reader(sampling_of_files)
    pprint.pprint(string_of_files_list[:2])

    cv, tokenized_files = cluster_documents(string_of_files_list)

    best_cluster(cv, tokenized_files, 2)

    summarize_documents(string_of_files_list)


if __name__ == '__main__':
    main()
