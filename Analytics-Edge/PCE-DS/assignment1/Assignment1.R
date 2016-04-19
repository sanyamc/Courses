
# 
# 3. Review the patterns described in DataScience01a.R and use R to get the Indian Liver Patient Dataset
# from the UCI machine learning repository

url <- "http://archive.ics.uci.edu/ml/machine-learning-databases/00225/Indian%20Liver%20Patient%20Dataset%20(ILPD).csv"

ILPD <-read.csv(url,header=FALSE,stringsAsFactors=FALSE)

# 4. Gather 11 column names from http://archive.ics.uci.edu/ml/datasets/ILPD+(Indian+Liver+Patient+Dataset) 
# and add headers to the data frame.



a.headers <- c("Age","Gender","TB","DB","Alkphos","Sgpt","Sgot","TP","ALB","A/G","Selector")
names(ILPD) <- a.headers

# 5. Observe first 6 rows of data frame.
head(ILPD)



# 6. Review the patterns described in DataScience01a.R. Write code to determine the mean, median,
# and standard deviation (sd) of each column and present their values in the console. Some
# calculations may fail. Where applicable, fix the failures by using na.rm = TRUE. Type ?median to see
# how.

summary(ILPD)
sapply(ILPD,mean,na.rm=TRUE)
sapply(ILPD,median,na.rm=TRUE)
sapply(ILPD,sd,na.rm=TRUE)

# 7.Review the patterns described in DataScience01a.R Create Histograms (hist) for each column where possible.

hist(ILPD[,1],col=rgb(0,1,0,.5))
hist(ILPD[,3],col=rgb(0,1,0,.5))
hist(ILPD[,4],col=rgb(0,1,0,.5))
hist(ILPD[,5],col=rgb(0,1,0,.5))
hist(ILPD[,6],col=rgb(0,1,0,.5))

# 8. Review the patterns described in DataScience01a.R 
#    Use the plot(ILPD) function on this data frame to present a general overview of the data. 
#    You want to see a matrix of many plots. You may have some problems because the Gender column is not numeric. 
#   You can skip the Gender column, or you can turn the gender column into a numeric column. 
#   You might need help from a fellow student, the LinkedIn group, or me.

ILPD$Gender[ILPD$Gender=="Male"]<-1
ILPD$Gender[ILPD$Gender=="Female"]<-0
ILPD$Gender<-as.numeric(ILPD$Gender)
plot(ILPD)

# 9 Look at the plots from plot(ILPD) and answer: 
#   9a What can you say about the data?
# ANSWER: 
#     - We can see that data is composed of both discrete and continuous values.
#     - There is either a positive or no correlation among variables
#     -  Just by looking at the plot its very easy to identify the values a variable take, their population and their
#        correlation with other variables.
#   9b How can you tell if a vector contains continuous numbers or binary data? 
#     ANSWER:
#     - Continuous values are scattered all over the chart in a plot while binary values have straight line along x
#       axis with y=0 or along y axis with x=0.for e.g. Gender and Selector are example of binary values while TB, DB 
#        are example of continuous variables.

#   9c How can you tell if two vectors are correlated?
#     ANSWER: 
#     - Two vectors are correlated if for a value in one vector the value in other vector either increases or decreases
#       If we plot all the points in two vectors, then we can see that majority of points should lie close to straight
#       line with +ve or -ve slope.


# 10 Review the patterns described in DataScience01b.R  Write code to remove outliers 
#    from the following vector and present the result in the console: c(-1, 1, -1, 1, 1, 17, -3, 1, 1, 3)
x <- c(-1, 1, -1, 1, 1, 17, -3, 1, 1, 3)
highLimit <- mean(x) + 2*sd(x)
lowLimit <- mean(x) - 2*sd(x)
goodFlag <- (x < highLimit) & (x > lowLimit)
x[goodFlag]
x
x <- x[goodFlag]
x

# 11 Review the patterns described in DataScience01b.R  Write code to relabel the following vector.
# Use the shortest strings for each category in the relabeled version.
# Present the result in the console: c('BS', 'MS', 'PhD', 'HS', 'Bachelors', 'Masters', 'High School', 'BS', 'MS', 'MS') 
x <- c('BS', 'MS', 'PhD', 'HS', 'Bachelors', 'Masters', 'High School', 'BS', 'MS', 'MS') 
x[x=='Bachelors'] <-'BS'
x[x=='High School'] <- 'HS'
x[x=="Masters"] <- 'MS'
x

# 12 Review the patterns described in DataScience01b.R
# Write code to normalize the following vector using a Min-Max normalization and 
# present the result in the console:  c(-1, 1, -1, 1, 1, 17, -3, 1, 1, 3) 
x <- c(-1, 1, -1, 1, 1, 17, -3, 1, 1, 3) 
a <- min(x)
b <- max(x)-min(x)
normalized <- (x-a)/b
normalized


# 13 Review the patterns described in DataScience01b.R
# Write code to normalize the following vector using a Z-score normalization 
# and present the result in the console:  c(-1, 1, -1, 1, 1, 17, -3, 1, 1, 3) 

x<-c(-1, 1, -1, 1, 1, 17, -3, 1, 1, 3)
a <- mean(x)
b <- sd(x)
normalized <- (x - a) / b
normalized


# 14 Review the patterns described in DataScience01b.R 
# Write code to binarize: c('Red', 'Green', 'Blue', Green', 'Blue', 'Blue', 'Blue', 'Red', 'Green', 'Blue')  
# and present the result in the console 
x <- c('Red', 'Green', 'Blue', 'Green', 'Blue', 'Blue', 'Blue', 'Red', 'Green', 'Blue') 
isRed <- x == 'Red'
isGreen <- x == 'Green'
isBlue <- x == 'Blue'

isRed
isGreen
isBlue

isRed <- as.numeric(isRed)
isGreen <- as.numeric(isGreen)
isBlue <- as.numeric(isBlue)

# as a data frame
data.frame(isRed, isGreen, isBlue)


# 15 Review the patterns described in DataScience01b.R  
# Write code to discretize the following vector into 3 bins of equal range
# and present the result in the console: c(81, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 9, 12, 23, 24, 25) 

x<- c(81, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 9, 12, 23, 24, 25) 
range <- max(x) - min(x)
binWidth <- range / 3
bin1Min <- -Inf
bin1Max <- min(x) + binWidth
bin2Max <- min(x) + 2*binWidth
bin3Max <- Inf
xDiscretized <- rep(NA, length(x))
xDiscretized
xDiscretized[bin1Min < x & x <= bin1Max] <- "Low"
xDiscretized[bin1Max < x & x <= bin2Max] <- "Moderate"
xDiscretized[bin2Max < x & x <= bin3Max] <- "High"
xDiscretized

# 16 Discretize the following vector into 3 bins of equal of near equal amounts of numbers. 
# No Code is necessary, just present the results as commented text. c(81, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 9, 12, 23, 24, 25) 

# x<6 == 'low' ( 11 entries)
# 6<=x<8 == 'moderate' (9 entries)
# x>=8 == "high" (8 entries)

# 
# discrete
# 1      high
# 2       low
# 3       low
# 4       low
# 5       low
# 6       low
# 7       low
# 8       low
# 9       low
# 10      low
# 11      low
# 12      low
# 13 moderate
# 14 moderate
# 15 moderate
# 16 moderate
# 17 moderate
# 18 moderate
# 19 moderate
# 20 moderate
# 21 moderate
# 22     high
# 23     high
# 24     high
# 25     high
# 26     high
# 27     high
# 28     high

