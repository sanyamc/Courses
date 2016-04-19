# KMeans_Skeleton.R
# Copyright 2016 by Ernst Henle

# Clear Workspace
rm(list=ls())
# Clear Console:
cat("\014")

# Obtain ClusterPlot.  Obtain samples for observations, clusterCenters, and labels.
source("C:\\RProgramming\\PCE-DS\\KMeans\\KMeansHelper.R")

 ClusterPlot()
# Returns a plot with randomly labelled observations and clusterCenters

 calculateClusterCenters()
# Result: 
#             [,1]        [,2]
# [1,] -0.02392857 -0.02464286
# [2,]  0.1032142  -0.10071429
# [3,] -0.08370370  0.13000000

 findLabelOfClosestCluster()
# Result:
# [1] 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
# [23] 3 3 3 3 3 3 3 3 3 3 3 3 3 1 3 3 3 1 3 3 3 3
# [45] 3 3 3 3 3 3 3 3 3 3 1 3 3 1 3 3 3 3 2 2 3 3
# [67] 2 2 3 3 3 3 2 3 3 3 3 3 3 3 1 3 3

 KMeans()
# Result:  
#            [,1]       [,2]
# [1,]  0.0332000  0.6508000
# [2,]  1.5163158  1.0057895
# [3,] -0.7610256 -0.9071795

# KMeans is a 2D K-means implementation.  
# The function are observations that will be clustered and initial clusterCenters. 
# returns K-mean clusterCenters
# The function does not normalize the inputs. 
KMeans <- function(observations = sampleObservations, clusterCenters = centersGuess)
{   
  # Initialize the cluster labels from the previous iteration with NULL
  previousLabels<-rep_len(NA,nrow(observations))
  # repeat the following processes using a loop.  Prevent infinite loop with a for loop of 25 iterations
  for (iteration in 1:25)
  {
    # For each observation find the label of its closest cluster center
    currentLabels <- findLabelOfClosestCluster(observations,clusterCenters)
    # Plot observations and clusterCenters
    ClusterPlot(observations, clusterCenters, currentLabels)
    # If there was no change in cluster labels, then break
   match <- all(currentLabels==previousLabels)
  
    if (!is.na(match) && match==TRUE) # could also use indentical(currentLabels,previousLabels)
    {
      break
    }
    
    # For each cluster of observations determine its center
    clusterCenters<-calculateClusterCenters(observations,currentLabels)
    # Plot observations and clusterCenters
    ClusterPlot(observations, clusterCenters,  currentLabels)
    # remember currentLabels before currentLabels is re-assigned in the next iteration
    previousLabels<-currentLabels
  } # end of the for loop
  # Return the clusterCenters
   clusterCenters
} # end of KMeans.

# For each cluster of observations determine its center
# The inputs are the observations and the cluster labels of the observations
# The output is a vector of the new clusterCenters
calculateClusterCenters <- function(observations=sampleObservations, clusterLabels=labelsRandom)
{
  # How many clusterCenters will we make?  What is the maximum cluster label? 
    
 number_of_dimensions <- ncol(observations)
 number_of_clusterLabels <-length(unique(clusterLabels))
  # Create a matrix where each row is a cluster center.  The number of columns reflects the dimensionality of the space.
  
  cluster_centers <- matrix(nrow=number_of_clusterLabels,ncol=number_of_dimensions)
  # For loop through each cluster label 
  for (center in 1:number_of_clusterLabels)
  {
    # Get only the observations from one cluster
    observations_per_cluster <- subset(observations,clusterLabels==center)
    # Determine the mean of that cluster in the 1st dimension and assign this mean
    # to the 1st dimension of the center    
    # Determine the mean of that cluster in the 2nd dimension and assign this mean
    # to the 2nd dimension of the center
    cluster_centers[center,]<-colMeans(observations_per_cluster)
  } # Ends the for loop through each cluster id
  # Return the clusterCenters
  cluster_centers
} # end of calculateClusterCenters

# A function that returns the cluster IDs for each observation
# The function takes the observations
# The function takes clusterCenters 
# The cluster that is closest to each observation will determine the cluster ID for that observation
# A cluster ID indicates the allegiance of a observation to a cluster
findLabelOfClosestCluster <- function(observations = sampleObservations, clusterCenters=centersGuess)
{
  # Get the number of clusterCenters
  # number of clusters
  number_of_clusters <- nrow(clusterCenters)
  # Get the number of observations
  number_of_observations <- nrow(observations)
  # Create a matrix that will contain the squared distances from each observation to each center
  # The matrix has numberOfObservations rows and numberOfClusters columns
  # for e.g. if there are 80 points and 3 centers then matrix will have 240 observations
  distances <- matrix(nrow=number_of_observations,ncol=number_of_clusters)
  
  # Determine the distance from the center to each observation
  # For loop for each observation number
  for (point in 1:number_of_observations)
  {
    # For loop for each center number
    for (center in 1:number_of_clusters)
    {
      # What is the difference between the current observation and the current center?
      # In other words: What is the vector between the observation and center?
      diff <- observations[point,] - clusterCenters[center,]
      # What is the distance of this vector?
      distance <- sqrt(sum(diff^2))
      # In other words: what is the sum of the squares of the vector elements?
      # If the distance squared was NA then make it infinite
      if(is.na(distance)) distance <- Inf
      # Assign the distance squared to the proper element in the matrix created above
      distances[point,center] <- distance
    } # end of the for loop for each center number
  } # end of the for loop for each observation number
  # Determine the labels of the closest center
  max.col(-distances)
  
} # end of findLabelOfClosestCluster
