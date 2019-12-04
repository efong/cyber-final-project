"""
Machine learning for identifying phishing URLs uding logistic regression

Created on 2019-12-03

Authors: Erik Fong, Julian Gardner, Daniel Kalam
with help from
https://www.kdnuggets.com/2016/10/machine-learning-detect-malicious-urls.html
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer


def getTokens(input):
    """
    Tokenize a URL.
    Tokens are split by slash, hyphen, and dot.
    Redundant tokens are removed.
    The token "com" is removed from the list since it is a common TLD
    that should not be used for our purposes.
    Mostly taken from the website linked above.
    """
    tokensSlash = str(input.split('/'))
    allTokens = []
    for i in tokensSlash:
        tokensDash = str(i).split('-')
        tokensDot = []
        for j in range(0,len(tokensDash)):
            tokens = str(tokensDash[j]).split('.')
            tokensDot = tokensDot + tokens
        allTokens = allTokens + tokensDash + tokensDot
    allTokens = list(set(allTokens)) # remove duplicates
    if 'com' in allTokens:
        allTokens.remove('com')
    return allTokens


def TrainingAlgorithm():
    """
    Use the data to train the logistic regression algorithm.
    Takes in data from a file in csv format with columns corresponding to
    URL and label.
    Returns the logistic regression object and the vector for each URL.
    Also mostly taken from the website at the beginning of the file.
    """
    urlFile = 'C:\\Users\\pokef\\Documents\\CybersecurityProg\\badandgoodurls.csv' # Replace this with data file path
    urlCSV = pd.read_csv(urlFile, ',',error_bad_lines=False)
    urlDF = pd.DataFrame(urlCSV)
    
    urlData = np.array(urlDF)
    
    labels = [d[1] for d in urlData]
    corpus = [d[0] for d in urlData]
    vectorizer = TfidfVectorizer(tokenizer=getTokens) # get a vector for each URL but use our tokenizer
    X = vectorizer.fit_transform(corpus)
    X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)
    
    logisticReg = LogisticRegression()
    logisticReg.fit(X_train, y_train)
    print(logisticReg.score(X_test, y_test)) # print accuracy score
    return vectorizer, logisticReg

vectorizer, logisticReg = TrainingAlgorithm()

# To check URLs uncomment the following code:

#toPredict = ['wikipedia.com','google.com'] # replace this list with the URLs to check
#toPredict = vectorizer.transform(toPredict)
#prediction = logisticReg.predict(toPredict)
#print(prediction)