'''
install.packages("caTools")
install.packages("class")
install.packages("ggplot2")

library(caTools)
library(class)
library(ggplot2)

data(iris)
str(iris)   # structure of dataset

set.seed(123)

# Split data
split <- sample.split(iris$Species, SplitRatio = 0.7)

train_cl <- subset(iris, split == TRUE)
test_cl  <- subset(iris, split == FALSE)

# Scale features
train_scale <- scale(train_cl[,1:4])
test_scale  <- scale(test_cl[,1:4])

# Apply KNN
classifier_knn <- knn(train = train_scale,
                      test = test_scale,
                      cl = train_cl$Species,
                      k = 1)

# Confusion matrix
cm <- table(test_cl$Species, classifier_knn)
cm
'''
