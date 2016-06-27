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

from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.metrics import accuracy_score
#print len(features_train[0])
clf1 = RandomForestClassifier()
t0=time()
clf1.fit(features_train,labels_train)
t1=time()
pred = clf1.predict(features_test)
print "RandomForest: ",accuracy_score(pred,labels_test)
print "time taken to train RandomForest ",(t1-t0)

clf2 = AdaBoostClassifier()
t0=time()
clf2.fit(features_train,labels_train)
t1=time()
pred = clf2.predict(features_test)
print "ADABoost: ",accuracy_score(pred,labels_test)
print "time taken to train RandomForest ",(t1-t0)







#########################################################
### your code goes here ###


#########################################################

