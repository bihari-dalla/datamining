'''
if(!require(rpart)) install.packages("rpart")
if(!require(rpart.plot)) install.packages("rpart.plot")

library(rpart)
library(rpart.plot)

data(iris)

iris$Species <- as.factor(iris$Species)

set.seed(123)
index <- sample(1:nrow(iris), 0.7 * nrow(iris))
train <- iris[index, ]
test <- iris[-index, ]

model <- rpart(Species ~ ., data = train, method = "class")

rpart.plot(model)

pred <- predict(model, test, type = "class")

table(Predicted = pred, Actual = test$Species)

accuracy <- mean(pred == test$Species)
accuracy
'''
