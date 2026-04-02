'''
# Hierarchical Clustering: Agglomerative clustering

# Read data
data("iris")
names(iris)

# To perform hierarchical clustering
clusters <- hclust(dist(iris[, 3:4]))

# To visualize the hierarchical clustering (dendrogram)
plot(clusters)

# Cut dendrogram into 3 clusters
clusterCut <- cutree(clusters, 3)

# Compare clusters with actual species
table(clusterCut, iris$Species)

# Visualization using ggplot2
install.packages("ggplot2")
library(ggplot2)

ggplot(iris, aes(Petal.Length, Petal.Width, color = iris$Species)) +
  geom_point(alpha = 0.4, size = 3.5) +
  geom_point(aes(color = as.factor(clusterCut)), size = 2) +
  scale_color_manual(values = c('black', 'red', 'green'))

# Using average linkage method
clusters <- hclust(dist(iris[, 3:4]), method = "average")

clusterCut1 <- cutree(clusters, 3)

table(clusterCut1, iris$Species)

plot(clusters)

ggplot(iris, aes(Petal.Length, Petal.Width, color = iris$Species)) +
  geom_point(alpha = 0.4, size = 3.5) +
  geom_point(aes(color = as.factor(clusterCut1)), size = 2) +
  scale_color_manual(values = c('black', 'red', 'green'))
  '''
