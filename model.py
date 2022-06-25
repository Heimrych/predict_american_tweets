"""Build a language detector model
The goal of this exercise is to train a linear classifier on text features
that represent sequences of up to 3 consecutive characters so as to be
recognize natural languages by using the frequencies of short character
sequences as 'fingerprints'.
"""
# Author: Olivier Grisel <olivier.grisel@ensta.org>
# License: Simplified BSD

import pickle
import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# Formatting training data using pandas
df = pd.read_csv('training.csv', sep=";")
df["american"] = (df['country_code'] == "US").astype(int)

data_list = df["text"]
targets_list = df["american"]

# The training data folder must be passed as first argument
# languages_data_folder = sys.argv[1]
# dataset = load_files(languages_data_folder)

# Split the dataset in training and test set:
# docs_train, docs_test, y_train, y_test = train_test_split(
#     dataset.data, dataset.target, test_size=0.5)

count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(data_list)
X_train_counts.shape

tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
X_train_tf = tf_transformer.transform(X_train_counts)
X_train_tf.shape

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
X_train_tfidf.shape

clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', MultinomialNB()),
])

clf.fit(data_list, targets_list)

test_df = pd.read_csv('test.csv', sep=";")
test_df["american"] = (test_df['country_code'] == "US").astype(int)

test_data_list = test_df["text"]
test_targets_list = test_df["american"]

predicted = clf.predict(test_data_list)
print(np.mean(predicted == test_targets_list))

with open('model.pickle', 'wb') as f:
    pickle.dump(clf, f)