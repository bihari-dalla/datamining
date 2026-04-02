# Aim: Clustering
# Q1) k-means clustering

'''
# Read data
data("iris")
names(iris)

# subset(): Filters rows or columns based on conditions.
# select = -Species: Selects all columns except the Species column.
new_data <- subset(iris, select = c(-Species))
new_data

# kmeans(): Performs K-means clustering.
cl <- kmeans(new_data, 3)
cl

data <- new_data

# Calculates the total within-cluster sum of squares (WSS) for different values of k
# provide range of cluster counts
wss <- sapply(1:15, function(k){kmeans(data, k)$tot.withinss})
wss

# To visualize how WSS changes with different values of k and find the "elbow"
plot(1:15, wss,
     type = "b", pch = 19, frame = FALSE,
     xlab = "Number of clusters K",
     ylab = "Total within-clusters sum of squares")

# Visualizing the clusters
install.packages("cluster")
library(cluster)

clusplot(new_data, cl$cluster, color = TRUE, shade = TRUE, labels = 2, lines = 0)

# To display the cluster assignments for each data point
cl$cluster

# To display the centroids of the clusters
cl$centers
'''
