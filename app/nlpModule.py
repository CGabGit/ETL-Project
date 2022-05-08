from typing import Counter
import dbConnection
import pandas as pd
from pandas import ExcelWriter
import re
from bs4 import BeautifulSoup
import nltk; nltk.download('punkt'); nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk import ngrams, FreqDist
from nltk.stem import SnowballStemmer
from datetime import datetime
import time
"""
In this file all functions related to NLP are defined.
The functions conducts on a string input: tokenization,
stopword removal, stemming, n-gram-specific stopwords removal,
count word frequency of one-grams, bi-grams, tri-grams
"""

def loadSpreadsheet(fileId):
    googleSpreadsheet = f"https://docs.google.com/spreadsheets/d/{fileId}/export?format=csv"
    dataframe = pd.read_csv(googleSpreadsheet)
    stop_words = [word for word in dataframe['stop_words'].astype(str)]
    return stop_words

def preprocessing():
    # open database connection and load 'tbl_jobitems' into dataframe
    df = dbConnection.loadTblJI()
    # joins data of all rows of column 'profiletext' together to string
    profiles = ' '. join(df['profiletext'])
    # after character '>' insert an additional white space
    profiles = profiles.replace('>','> ')
    # delete all remaining html-tags
    profiles = BeautifulSoup(profiles, "lxml").text
    # replace some characters to enhance stemming
    profiles = profiles.lower().replace('-', ' ').replace('/', ' ').replace('(', '').replace(')', '').replace(',', '').replace('.', '').replace('–', ' ')
    # keep only characters named explicitely
    profiles = re.sub(r'^[A-Za-z][A-Za-z0-9!ÄäÜüÖö#@$%^&*]*$', ' ', profiles)
    tokenizing(profiles)
    return

def tokenizing(profiles):
    tokens = nltk.WhitespaceTokenizer().tokenize(profiles)
    stopwordRemoval(tokens)
    return

def stopwordRemoval(tokens):
    # load default stop words from google spreadsheet
    german_stop_words = loadSpreadsheet("1sbDqG3tA4_U8fFoMsTjL50G6DB90pBv25dkdfrygCEw")
    tokens = [word for word in tokens if word not in german_stop_words]
    stemming(tokens)
    return 

def stemming(tokens):
    # stemming
    stems = []
    stemmer = SnowballStemmer("german")
    for token in tokens:
        token = stemmer.stem(token)
        if token != "":
            stems.append(token)

    # n-gram-specific stopwords removal

    onegram_stop_words = loadSpreadsheet("1rsVqZSeimDT0wZvY0Szq4b2vCNbzz_jVeRmL64zJ3FY")
    bigram_stop_words = loadSpreadsheet("1P-XzJy1T8FYBtQD2V-6-uo1ZKxq9K_b33sxhjY5f85E")
    trigram_stop_words = loadSpreadsheet("1vju3pX-J8_ZQn-KNOBtSXTRx9JWBNjKQjJJdX9znbUI")

    stems_1 = [word for word in stems if word not in onegram_stop_words]
    stems_2 = [word for word in stems if word not in bigram_stop_words]
    stems_3 = [word for word in stems if word not in trigram_stop_words]

    counted = Counter(stems_1)
    counted_2 = Counter(ngrams(stems_2, 2))
    counted_3 = Counter(ngrams(stems_3, 3))

    word_freq = pd.DataFrame(counted.items(),columns=['word','frequency']).sort_values(by='frequency',ascending=False)
    word_freq['record_date'] = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

    bigrams = pd.DataFrame(counted_2.items(),columns=['bigrams','frequency']).sort_values(by='frequency',ascending=False)
    bigrams['record_date'] = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

    trigrams = pd.DataFrame(counted_3.items(),columns=['trigrams','frequency']).sort_values(by='frequency',ascending=False)
    trigrams['record_date'] = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

    # write df to DB

    dbConnection.insertWordFreq(word_freq.head(40),'tbl_word_freq')
    dbConnection.insertWordFreq(bigrams.head(20),'tbl_bigrams')
    dbConnection.insertWordFreq(trigrams.head(20),'tbl_trigrams')
    time.sleep(10)
    dbConnection.setStatusFinished()
    return print("nplModule finished!")


## open database connection and load 'tbl_jobitems' into dataframe
#df = dbConnection.loadTblJI()
##df.dtypes
##df.info()

# # Preprocessing

# # joins data of all rows of column 'profiletext' together to string
# profiles = ' '. join(df['profiletext'])
# # after character '>' insert an additional white space
# profiles = profiles.replace('>','> ')
# # delete all remaining html-tags
# profiles = BeautifulSoup(profiles, "lxml").text
# # replace some characters to enhance stemming
# profiles = profiles.lower().replace('-', ' ').replace('/', ' ').replace('(', '').replace(')', '').replace(',', '').replace('.', '').replace('–', ' ')
# # keep only characters named explicitely
# profiles = re.sub(r'^[A-Za-z][A-Za-z0-9!ÄäÜüÖö#@$%^&*]*$', ' ', profiles)

# # tokenizing 
# tokens = nltk.WhitespaceTokenizer().tokenize(profiles)

#stopwords removal

# # load default stop words from google spreadsheet
# german_stop_words = loadSpreadsheet("1sbDqG3tA4_U8fFoMsTjL50G6DB90pBv25dkdfrygCEw")
# tokens = [word for word in tokens if word not in german_stop_words]

#stop_words = set(line.strip() for line in open('german-stop-words.txt', 'r',encoding='utf-8'))
#tokens = [word for word in tokens if word not in german_stop_words]

# # stemming
# stems = []
# stemmer = SnowballStemmer("german")
# for token in tokens:
#     token = stemmer.stem(token)
#     if token != "":
#         stems.append(token)


# # n-gram-specific stopwords removal

# onegram_stop_words = loadSpreadsheet("1rsVqZSeimDT0wZvY0Szq4b2vCNbzz_jVeRmL64zJ3FY")
# bigram_stop_words = loadSpreadsheet("1P-XzJy1T8FYBtQD2V-6-uo1ZKxq9K_b33sxhjY5f85E")
# trigram_stop_words = loadSpreadsheet("1vju3pX-J8_ZQn-KNOBtSXTRx9JWBNjKQjJJdX9znbUI")

# stems_1 = [word for word in stems if word not in onegram_stop_words]
# stems_2 = [word for word in stems if word not in bigram_stop_words]
# stems_3 = [word for word in stems if word not in trigram_stop_words]

#onegram_stop_words = set(line.strip() for line in open('onegrams_german-stop-words.txt', 'r',encoding='utf-8'))
#bigram_stop_words = set(line.strip() for line in open('bigrams_german-stop-words.txt', 'r',encoding='utf-8'))
#trigram_stop_words = set(line.strip() for line in open('trigrams_german-stop-words.txt', 'r',encoding='utf-8'))

#stems_1 = [word for word in stems if word not in onegram_stop_words]
#stems_2 = [word for word in stems if word not in bigram_stop_words]
#stems_3 = [word for word in stems if word not in trigram_stop_words]

# count word/n-gram frequency

# counted = Counter(stems_1)
# counted_2 = Counter(ngrams(stems_2, 2))
# counted_3 = Counter(ngrams(stems_3, 3))

# word_freq = pd.DataFrame(counted.items(),columns=['word','frequency']).sort_values(by='frequency',ascending=False)
# word_freq['record_date'] = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

# bigrams = pd.DataFrame(counted_2.items(),columns=['bigrams','frequency']).sort_values(by='frequency',ascending=False)
# bigrams['record_date'] = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

# trigrams = pd.DataFrame(counted_3.items(),columns=['trigrams','frequency']).sort_values(by='frequency',ascending=False)
# trigrams['record_date'] = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

# print(word_freq.head(10))
# print(bigrams.head(10))
# print(trigrams.head(10))
#trigrams.info()

# # write df to DB

# dbConnection.insertWordFreq(word_freq.head(40),'tbl_word_freq')
# dbConnection.insertWordFreq(bigrams.head(20),'tbl_bigrams')
# dbConnection.insertWordFreq(trigrams.head(20),'tbl_trigrams')


# writer = pd.ExcelWriter('stpw.xlsx', engine='xlsxwriter')
# bigrams.to_excel(writer,'Sheet1')
# writer.save()

# all_counts = dict()
# for size in 1 , 2 :
#     all_counts[size] = FreqDist(ngrams(stems, size)).pprint(maxlen=60)
# print(all_counts)


# =================================================
## Entfertnt alle HTML-Tags -> datentyp STRING
#cleantext = BeautifulSoup(raw_html, "lxml").text
#print(cleantext)
## sucht alles was in <li> </li> befindet und speichert jedes listenelement in einer liste -> datentyp LIST
#list_items = re.findall('<li>(.*?)</li>', raw_html)
#print(list_items)
# =================================================
# save df to excel and keep utf8 !
# writer = pd.ExcelWriter('tbl_jobitems.xlsx', engine='xlsxwriter')
# df.to_excel(writer,'Sheet1')
# writer.save()
# ===================================================================

# Tokenizing 

#print(profiles)

def tokenize(text):
        """
        Tokenizes sequences of text and stems the tokens.
        :param text: String to tokenize
        :return: List with stemmed tokens
        """
        tokens = nltk.WhitespaceTokenizer().tokenize(text)
        #tokens = list(set(re.sub("[^a-zA-Z\']", "", token) for token in tokens))
        tokens = [word for word in tokens if word not in nltk.stopwords.words('german')]
        tokens = list(set(re.sub("[^a-zA-Z]", "", token) for token in tokens))
        stems = []
        stemmer = SnowballStemmer("german")
        for token in tokens:
            token = stemmer.stem(token)
            if token != "":
                stems.append(token)
        return stems 
