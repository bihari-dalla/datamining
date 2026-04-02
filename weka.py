'''
Performing Classification on Data
Sets(weather.nominal.arff)
a. Building a Decision Tree Classifier in WEKA
Aim:
To build a Decision Tree classifier (J48) using a given dataset in WEKA.
Steps:
1. Open WEKA GUI → Explorer.
2. Click Open File and load the dataset (e.g., weather.arff or any .csv/.arff file).
3. Go to the Classify tab.
4. Select the classifier:
trees → J48 (implementation of C4.5 Decision Tree).
5. Choose Percentage Split or Cross Validation for testing method.
Example: 10-fold cross-validation.
6. Click Start to build the model.
7. WEKA will display:
o Decision tree structure
o Correctly and incorrectly classified instances
o Confusion matrix
o Accuracy, precision, recall, F-measure
Result:
A Decision Tree classifier is successfully built and evaluated on the dataset.
b. Applying Naïve Bayes on Dataset for Classification
Aim:
To apply Naïve Bayes classifier on a dataset and evaluate performance.
Steps:
1. Open WEKA → Explorer.
2. Load the required dataset.
3. Click on the Classify tab.
4. Select:
bayes → NaiveBayes.
5. Choose testing method:
o 10-fold cross validation
o Or Percentage split
6. Click Start.
7. WEKA shows:
o Class probabilities
o Correct and incorrect predictions
o Accuracy
o Confusion matrix
Result:
Naïve Bayes classifier is applied and classification accuracy is obtained.
c. Creating the Testing Dataset
Aim:
To create a testing dataset for evaluating machine learning models.
Steps:
1. Open the dataset in WEKA’s Preprocess tab.
2. Use Remove Percentage filter to separate data:
o Example: Keep 70 percent for training
o Remaining 30 percent is the testing dataset
3. Save the separated testing data as:
testing_dataset.arff
4. Alternatively, manually create a testing dataset in Excel/Notepad:
o Keep same attributes
o Remove class labels if needed
o Save as CSV
o Convert to ARFF using WEKA
Result:
Testing dataset is created and saved for evaluating classification models.
'''
