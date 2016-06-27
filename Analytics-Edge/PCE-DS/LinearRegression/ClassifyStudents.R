# ClassifyStudents.R

# Clear objects from Memory
rm(list=ls())
# Clear Console:
cat("\014")

source("CollegeStudentsDatasets.R")

# Set repeatable random seed
set.seed(4)

###################################################

# Partition data between training and testing sets

# Replace the following line with a function that partitions the data correctly
StudentsSplit <- PartitionExact(Students, fractionOfTest=0.4) # ********** Change here
TestStudents <- StudentsSplit$testingData
TrainStudents <-StudentsSplit$trainingData

###################################################

# Logistic Regression (glm, binomial)

# http://data.princeton.edu/R/glms.html
# http://www.statmethods.net/advstats/glm.html
# http://stat.ethz.ch/R-manual/R-patched/library/stats/html/glm.html
# http://www.stat.umn.edu/geyer/5931/mle/glm.pdf

# Create logistic regression
glm_model <- glm(formula,family="binomial",data=TrainStudents)
# ********** add code here
predictedProb_glm <- predict(glm_model,newdata=TestStudents,type="response")
# Predict the outcomes for the test data. (predict type="response")
# ********** add code here
###################################################

# Naive Bayes

# http://cran.r-project.org/web/packages/e1071/index.html
# http://cran.r-project.org/web/packages/e1071/e1071.pdf
# Get the algorithm

reposURL <- "http://cran.rstudio.com/"
# install package with naive bayes if not alreay installed
if (!require("e1071")) {install.packages("e1071", dep=TRUE, repos=reposURL)} else {" e1071 is already installed "}
# Now that the package is installed, we want to load the package so that we can use its functions
library(e1071)
# adding a comment
# Create Naive Bayes model
nb_model <- naiveBayes(formula,data=TrainStudents,type="raw")
# Predict the outcomes for the test data. (predict type="raw")
predictedProb_nb <- predict(nb_model,newdata=TestStudents,type="raw")

###################################################

# Confusion Matrices

actual <- ifelse(TestStudents$CollegePlans, "Attend", "NotAttend")
threshold = 0.7

accuracy <- function(predicted, actual)
    {
    eq <- length(predicted[predicted == actual])
    neq <- length(predicted[predicted != actual])
    return(eq / (eq + neq))
    }


#Confusion Matrix for Logistic Regression
# convert the predicted probabilities to predictions using a threshold
# 
print(" ")
print(" -------------------------------- ")
print("Confusion Matrix for Logistic Regression")
predicted.GLM <- ifelse(predictedProb_glm > threshold, "Attend", "NotAttend")
# create a table to compare predicted values to actual values
print(table(predicted.GLM, actual))
print(accuracy(predicted.GLM, actual))
# ********** add code here

#Confusion Matrix for Naive Bayes
# convert the predicted probabilities to predictions using a threshold
# ********** add code here
print(" ")
print(" -------------------------------- ")
print("Confusion Matrix Naive Bayes")
# create a table to compare predicted values to actual values
predicted.NB <- ifelse(predictedProb_nb[,2] > threshold, "Attend", "NotAttend")
# create a table to compare predicted values to actual values
print(table(predicted.NB, actual))
print(accuracy(predicted.NB, actual))



###################################################

# Bad Partition; threshold = 0.5
# 
# --------------------------------
# "Confusion Matrix for Logistic Regression"
#              Actual
# Predicted    Attend  NotAttend
# Attend        934        116
# NotAttend     759       1071
# Accuracy defined as fraction of predictions that are correct
# Accuracy:  (934 + 1071)/(934 + 759 + 116 + 1071) = 70%
# 
# --------------------------------
# "Confusion Matrix Naive Bayes"
#            Actual
# Predicted   Attend NotAttend
# Attend       325        84
# NotAttend   1368      1103
# Accuracy defined as fraction of predictions that are correct
# Accuracy:  (325 + 1103)/(325 + 1368 + 84 + 1103) = 50%

# Fill in the rest:

# Exact Partition; threshold = 0.5
#
# --------------------------------
# "Confusion Matrix for Logistic Regression"
#            Actual
# Predicted   Attend NotAttend
# Attend      679    209   add results here
# NotAttend   278    1714   add results here 
# Accuracy defined as fraction of predictions that are correct
# Accuracy:   83.09%
#
# --------------------------------
# "Confusion Matrix Naive Bayes"
#            Actual
# Predicted   Attend NotAttend
# Attend      547    206   add results here
# NotAttend   410    1717   add results here
# Accuracy defined as fraction of predictions that are correct
# Accuracy:   78.6%  add results here

# Fast Partition; threshold = 0.5
#
# --------------------------------
# "Confusion Matrix for Logistic Regression"
#            Actual
# Predicted   Attend NotAttend
# Attend      691    227   add results here
# NotAttend   262    1715  add results here
# Accuracy defined as fraction of predictions that are correct
# Accuracy:   83.10%   add results here
#
# --------------------------------
# "Confusion Matrix Naive Bayes"
#            Actual
# Predicted   Attend NotAttend
# Attend      572    211   add results here
# NotAttend   381    1731   add results here
# Accuracy defined as fraction of predictions that are correct
# Accuracy:   79.55%   add results here

# Exact Partition;  threshold = 0.7
#
# --------------------------------
# "Confusion Matrix for Logistic Regression"
#            Actual
# Predicted   Attend NotAttend
# Attend      471    72   add results here
# NotAttend   486    1851   add results here
# Accuracy defined as fraction of predictions that are correct
# Accuracy:   80.62%   add results here
#
# --------------------------------
# "Confusion Matrix Naive Bayes"
#            Actual
# Predicted   Attend NotAttend
# Attend      393    76   add results here
# NotAttend   564    1847   add results here
# Accuracy defined as fraction of predictions that are correct
# Accuracy:   77.78%   add results here