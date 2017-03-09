#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

print len(features_train)
print len(labels_train)
print len(features_test)
print len(labels_test)


#########################################################
### your code goes here ###
def create_classifier(min_samples_split=40):
    from sklearn.tree import DecisionTreeClassifier
    return DecisionTreeClassifier(min_samples_split=min_samples_split)

def train_classifier(clf, features_train, labels_train):
clf.fit(features_train, labels_train)
    return clf

def calc_accuracy(trained_clf, features_test, labels_test):
    from sklearn.metrics import accuracy_score
    preds = train_classifier.predict(features_test)
    return accuracy_score(labels_test, preds)

clf = create_classifier()
trained_clf = train_classifier(clf, features_train, labels_train)

print calc_accuracy(trained_clf, features_test, labels_test)

#########################################################


