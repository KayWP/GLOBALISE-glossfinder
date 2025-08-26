#import necessary packages
import pandas as pd
import os
from tqdm import tqdm
import sys

def main():
    if len(sys.argv) < 4:
        print('Please input all the necessary command line variables: a file extension, a folder path to the input folder, the name you want for the output file (minus .csv)')
        exit()

    #define the filetype we're interested in    
    file_extension = sys.argv[1]

    #set the folder path
    folder_path = sys.argv[2]

    #set the name of the csv
    output_file_name = sys.argv[3]
            
    #define what values can be used as an indicator
    of_dict = ['of', 'ofwel', 'oftewel', 'off', 'ofte', 'offe', 'ook wel', 'ookwel', 'of wel', 'offte', 'oft', 'oofte', 'efte', 'offf']

    #list all files in the folder with the necessary expansion
    files_to_analyze = [f for f in os.listdir(folder_path) if f.endswith(file_extension)]

    # Initialize CSV file with headers to output to
    output_file_path = output_file_name + '.csv'
    first_file = True

    # Use tqdm to create a progress bar
    with tqdm(total=len(files_to_analyze), desc="Processing files") as pbar:
        # Iterate over each file and apply the analyze_dictionary function
        for file_name in files_to_analyze:
            file_path = os.path.join(folder_path, file_name)
            token_dict = parse_pages(file_path)
            df = analyze_dictionary(token_dict, of_dict, 5)
            # Write to CSV after processing each file
            if first_file:
                # Write with header for the first file
                df.to_csv(output_file_path, index=False)
                first_file = False
            else:
                # Append without header for subsequent files
                df.to_csv(output_file_path, mode='a', header=False, index=False)

            # Clear variables to free memory
            del token_dict
            del df
            pbar.update(1)  # Increment progress bar

def parse_pages(file_path, encoding='utf-8'):
    #looks through a GLOBALISE text file and splits the information into scan-level text chunks
    pages = {}
    current_page = None

    with open(file_path, 'r', encoding=encoding) as file:
        for line in file:
            #checks through every line to see if it contains a scan-filename
            if 'NL-HaNA_' in line:
                if current_page:
                    # Tokenize the content of the previous page
                    pages[current_page] = tokenize_text(page_content.strip())
                page_content = ""
                current_page = line.strip()
            elif current_page:
                page_content += line

    # Add the content of the last page and tokenize it
    if current_page and page_content:
        pages[current_page] = tokenize_text(page_content.strip())

    return pages

def tokenize_text(text):
    # Split text into words
    words = text.split()
    return words

def analyze_dictionary(tokenized_dict, gloss_indicators, gloss_length):
    output = []
    for key in tokenized_dict.keys():
        output = output + glosses_on_page(tokenized_dict[key], gloss_indicators, gloss_length, key)
    
    return pd.DataFrame(output, columns=['Term', 'Indicator', 'Glossed As', 'Page'])

def glosses_on_page(tokenized_text, gloss_indicators, gloss_length, page):
    
    output = []
    
    #cursor = 0
    
    for index, token in enumerate(tokenized_text):
        for indicator in gloss_indicators:
            if token == indicator:
                
                gloss = ''
                try:
                    for i in range(1, gloss_length+1):
                        gloss = gloss + ' ' + tokenized_text[index + i]
                except IndexError:
                    next_index = index + 1
                    while next_index < len(tokenized_text) and not tokenized_text[next_index] in gloss_indicators:
                        gloss += ' ' + tokenized_text[next_index]
                        next_index += 1
                
                output.append([tokenized_text[index-1].strip(','), token, gloss.strip(), page])
                
    return output


if __name__ == "__main__":
    main()