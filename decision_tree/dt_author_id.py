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


#########################################################
### your code goes here ###

## calculate accuracy
from calc_accuracy import train_and_calc_acc
print train_and_calc_acc(features_train, features_test, labels_train, labels_test)

## calc_amount_of_features
# from calc_amount_of_features import calc_amount_of_features
# print calc_amount_of_features(features_train)

#########################################################


