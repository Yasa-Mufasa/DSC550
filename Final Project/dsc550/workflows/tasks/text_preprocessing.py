'''
Bellevue University
DSC 550: Data Mining Final Project

This task is to load and pre-process the text data. The data to be used is in the ~/source
folder and is title 'controversial-comments.jsonl'.
'''

import json
import pandas as pd
from multiprocessing import Pool
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def reading_data(file):
    data = []
    with open(file) as f:
        for line in f:
            data.append(json.loads(line))
    return data


def clean(self):
    self = self.replace('.', '').replace('*', '').replace(',', '').replace('!', '').replace('\n', '').replace('?', '').replace('(', '').replace(')', '').replace('[', '').replace(']', '').replace(';', '').replace("'", '').replace('`', '').replace('r/', '').replace('/', '').replace('"', '').replace('&', '').replace(':', '').lower()
    return self


def tokenize_documents(df, n_processes):
    with Pool(n_processes) as pool:
        tok_docs = pool.map(word_tokenize, df['txt'])
    return tok_docs


def formating_data(data, n_processes):
    # Breaking the data into the respective lists
    contro = []
    txt = []
    for i in range(len(data)):
        contro.append(data[i]['con'])
        txt.append(data[i]['txt'])

    # Cleaning the Strings
    cleaned_strings = []
    for string in txt:
        cleaned_strings.append(clean(string))

    # Putting the data into a Data Frame
    d = {'txt': cleaned_strings, 'con': contro}
    df = pd.DataFrame(data=d)
    df.to_pickle('C:/Users/yasam/OneDrive/Documents/Workspaces/DSC550/Final Project/data/interim/starting_df.pkl')

    # Now to tokenize the strings
    tokens = tokenize_documents(df, n_processes)

    # Now let's put this into another Data Frame and return it
    d1 = {'con': contro}
    df1 = pd.DataFrame(data=d1)
    df1['txt'] = tokens
    print(df1.head(5))

    # Let's save this to the to the processed folder
    df1.to_pickle('C:/Users/yasam/OneDrive/Documents/Workspaces/DSC550/Final Project/data/processed/tokenized_document.pkl')

    return df1


def main(file_location, n_processes=16):
    read_file = reading_data(file_location)
    tok_df = formating_data(read_file, n_processes)
    return tok_df


if __name__ == '__main__':
    developed_df = main('C:/Users/yasam/Documents/DS550 Data Mining/data/reddit/controversial-comments.jsonl', 16)
    print(developed_df)
