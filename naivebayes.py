'''
# Install and load required package
install.packages("e1071") # Run only once
library(e1071)

# Load dataset
data(iris)

# View first few rows
head(iris)

# Split dataset into training and testing
set.seed(123)
index <- sample(1:nrow(iris), 0.7 * nrow(iris))
train_data <- iris[index, ]
test_data <- iris[-index, ]

# Build Naïve Bayes model
nb_model <- naiveBayes(Species ~ ., data = train_data)

# View model details
nb_model

# Make predictions on test data
predictions <- predict(nb_model, test_data)

# Confusion Matrix
table(Predicted = predictions, Actual = test_data$Species)

# Calculate accuracy
accuracy <- mean(predictions == test_data$Species)
accuracy
'''
