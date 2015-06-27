#!/usr/bin/python

""" 
    this is the code to accompany the Lesson 3 (decision tree) mini-project

    use an DT to identify emails from the Enron corpus by their authors
    
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

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
print len(features_train[0])
clf = KNeighborsClassifier(10)
t0=time()
clf.fit(features_train,labels_train)
t1=time()
pred = clf.predict(features_test)
print "KNN: ",accuracy_score(pred,labels_test)
print "time taken to train KNN ",(t1-t0)







#########################################################
### your code goes here ###


#########################################################


