#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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
# print len(features_train)
# features_train = features_train[:len(features_train)/100] 
# labels_train = labels_train[:len(labels_train)/100] 
# print len(features_train)
print "features train size: ", len(features_train)
print "labels train size: ", len(labels_train)



#########################################################
### your code goes here ###
from sklearn.svm import SVC

clf = SVC(kernel="rbf", C=10000.)
t0 = time()
clf.fit(features_train, labels_train)
print "fitting", time() - t0, "s"
t1 = time()
preds = clf.predict(features_test)
print "predicition", time() - t1, "s"

print len([item for item in preds if (item == 1)])


# from sklearn.metrics import accuracy_score
# print accuracy_score(labels_test, preds)
#########################################################


