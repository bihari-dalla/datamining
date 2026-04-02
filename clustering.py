# Step 1: Load Required Libraries
install.packages("ggplot2")
library(ggplot2)

# Step 2: Load the Wholesale Customer Dataset
url <- "https://archive.ics.uci.edu/ml/machine-learning-databases/00292/Wholesale%20customers%20data.csv"
data <- read.csv(url)

head(data)

# Step 3: Select Features for Clustering
X <- data[, c("Fresh", "Milk", "Grocery", "Frozen", "Detergents_Paper", "Delicassen")]

# Step 4: Standardize the Data
X_scaled <- scale(X)

# Step 5: Elbow Method to Find Optimal K
wcss <- c()
for (i in 1:10) {
  kmeans_model <- kmeans(X_scaled, centers = i, nstart = 20)
  wcss[i] <- kmeans_model$tot.withinss
}

plot(1:10, wcss, type = "b",
     xlab = "Number of Clusters (K)",
     ylab = "WCSS",
     main = "Elbow Method for Optimal K")

# Step 6: Apply K-Means (Choose K=3 for example)
set.seed(123)
kmeans_final <- kmeans(X_scaled, centers = 3, nstart = 25)

# Step 7: Add Cluster Labels to Dataset
data$Cluster <- kmeans_final$cluster

head(data)

# Step 8: Cluster Centers
kmeans_final$centers
