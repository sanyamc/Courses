# KMeansNorm.R

KMeansNorm <- function(observations = sampleObservations, clusterCenters = centersGuess, normD1 = F, normD2 = F)
{
  if (normD1)
  {
    # Determine mean and standard deviation of 1st dimension in observations
    means_1d <- mean(observations[,1])
    sd_1d <- sd(observations[,1])
    
    # normalize 1st dimension of observations
    normalized_1d <- (observations[,1]-means_1d)/sd_1d
  
    # normalize 1st dimension of clusterCenters
    normalized_cc_1d <- (clusterCenters[,1]-means_1d)/sd_1d
      
    clusterCenters[,1] <- normalized_cc_1d
    observations[,1] <- normalized_1d    
    
   # hist(observations[,1], col=rgb(1,1,0,1))
   
  }
  if (normD2)
  {
    # Determine mean and standard deviation of 2nd dimension in observations
    means_2d <- mean(observations[,2])
    sd_2d <- sd(observations[,2])
    
    # normalize 2nd dimension of observations
    normalized_2d <- (observations[,2]-means_2d)/sd_2d
    
    # normalize 2nd dimension of clusterCenters
    normalized_cc_2d <- (clusterCenters[,2]-means_2d)/sd_2d
    
    clusterCenters[,2] <- normalized_cc_2d
    observations[,2] <- normalized_2d  
    #hist(observations[,2], col=rgb(0,0,1,0.25), add=T)
    
  }
  clusterCenters <- KMeans(observations, clusterCenters)
  if (normD1)
  {
    # assertion means_1d !=NULL & sd_1d !=NULL
    
    # denormalize in first dimension
    clusterCenters[,1]<-(clusterCenters[,1]*sd_1d)+means_1d
  } 
  if (normD2)
  {
    # denormalize in second dimension
    clusterCenters[,2]<-(clusterCenters[,2]*sd_2d)+means_2d
  } 
  return(clusterCenters)
}

# 3a) What is the single most obvious difference between these two distributions?
# Answer: 
# 1) TestObservations[,1] is way smaller in magnitude than Testobservations[,2] for most observations
# 2) TestObservations[,2] is lot more dispersed than TestObservation[,1]. In other words, TestObservation[,1] has way
# less standard deviation than TestObservation[,2]

# 3b) Does clustering in Test 1 occur along one or two dimensions?  Which dimensions?  Why?
#Answer: Clustering occurs along one dimension, along y axis. Its because y-axis values are so high that it shadows
#        the cluster effect of x-axis. We can observe this effect if we make x and y plots with same scale.

# 3c) Does clustering in Test 2 occur along one or two dimensions? Which dimensions? Why?
# Answer: Clustering occurs along one dimension, across y axis. This happens because we have normalized across
#   x-axis however y axis values are so large that it shadows any clustering effect of x-axis.

# 3d) Does clustering in Test 3 occur along one or two dimensions? Which dimensions? Why?
#   Answer: Clustering occurs along one dimension, across x-axis. This happens because we have normalized across y-axis
#           however this time x-axis values are large to shadow normalized y-axis values. As I observed that y-axis values
#            after normalizing are centered around 0 with normalized y-axis values for centers being -.08,.6 and .8 
#            which is very less compared to x-axis hence clustering happens around x-axis.

# 3e) Does clustering in Test 4 occur along one or two dimensions? Which dimensions? Why?
#  Answer: Clustering finally happens across both the dimensions as both values are normalized. None of the axis
#          dominates other and if we plot histogram of normalized observations then we see that both dimensions are 
#          comparable and one doesn't dominates/shadows the other. Clustering can finally be helpful!


#  4) Why is normalization important in K-means clustering? Add answer as a comment to bottom of the completed
#     KMeansNorm.R .
#  Answer: As we can see from above, if a dimension isn't normalized than it can impact clustering as mean across
#          that dimension will be very high and will dominate while comparing eucledian distance; making other dimension
#          meaningless.

#  5) How do you encode categorical data in a K-means clustering? Add answer as a comment to bottom of the
#     completed KMeansNorm.R .
#   Answer: We can binarize categorical data to numerical data for K-means purposes as we did with colors 
#           in assignment 1.

#  6) Why is clustering un-supervised learning as opposed to supervised learning? Add answer as a comment to
#     bottom of the completed KMeansNorm.R .
#     Answer: Clustering is un-supervised learning because 
#           a) We don't partition data into training and test set to train and test the algorithm.
#           b) Algorithm doesn't predict an outcome acting as an expert label; instead clustering just segments data.
