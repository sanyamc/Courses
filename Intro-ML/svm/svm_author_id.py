#!/usr/bin/python

""" 
    this is the code to accompany the Lesson 2 (SVM) mini-project

    use an SVM to identify emails from the Enron corpus by their authors
    
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

from sklearn import svm
from sklearn.metrics import accuracy_score
import numpy
#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 
t0 = time()
clf = svm.SVC(kernel='rbf',C=10000)

clf.fit(features_train,labels_train)
t1 = time()
print "training time ",t1-t0
pred =  clf.predict(features_test)

score =accuracy_score(pred,labels_test)

print pred[10]
print pred[26]
print pred[50]

print numpy.count_nonzero(pred)

print score



#########################################################
### your code goes here ###

#########################################################


