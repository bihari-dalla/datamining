''''
# Clustering on Agriculture Dataset (Seeds)
# UCI Machine Learning Repository
# Algorithm: K-Means Clustering

# Step 1: Install and load required library
install.packages("ggplot2")
library(ggplot2)

# Step 2: Load the Seeds dataset directly from UCI
url <- "https://archive.ics.uci.edu/ml/machine-learning-databases/00236/seeds_dataset.txt"
data <- read.table(url)

# Step 3: Assign column names
colnames(data) <- c(
  "Area",
  "Perimeter",
  "Compactness",
  "Kernel_Length",
  "Kernel_Width",
  "Asymmetry",
  "Groove_Length",
  "Class"
)

# Step 4: Remove class column (unsupervised learning)
X <- data[, 1:7]

# Step 5: Standardize the data
X_scaled <- scale(X)

# Step 6: Elbow Method to find optimal number of clusters
wcss <- c()
for (i in 1:10) {
  model <- kmeans(X_scaled, centers = i, nstart = 10)
  wcss[i] <- model$tot.withinss
}

# Plot Elbow graph
plot(
  1:10,
  wcss,
  type = "b",
  xlab = "Number of Clusters",
  ylab = "Within Cluster Sum of Squares",
  main = "Elbow Method for Optimal K"
)

# Step 7: Apply K-Means with optimal K = 3
kmeans_final <- kmeans(X_scaled, centers = 3, nstart = 25)

# Step 8: Add cluster labels to dataset
data$Cluster <- kmeans_final$cluster

# Step 9: View clustered data
head(data)

# Step 10: Visualize clusters using first two features
ggplot(data, aes(x = Area, y = Perimeter, color = as.factor(Cluster))) +
  geom_point(size = 2) +
  labs(title = "K-Means Clustering on Agriculture Dataset",
       color = "Cluster") 
'''
