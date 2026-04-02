# In Python
# cmd -> pip install -U scikit-learn
# cmd -> pip install -U seaborn
# cmd -> pip install matplotlib

# Code
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import confusion_matrix
import seaborn as sn
import matplotlib.pyplot as plt

iris = load_iris()
print(iris)
print(iris.feature_names)

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=2
)

knn = KNeighborsClassifier(n_neighbors=10)

train = knn.fit(X_train, y_train)

print("Target Names are :", iris.target_names)
print("Values for target class :", iris.target)

print("Size of the Train data :", len(X_train))
print("Size of the Test data :", len(X_test))

print("X values of test :", X_test)
print("Y values of Test data :", y_test)

print("Predicted classes for the above testing data :")
y_pred = train.predict(X_test)

print("Predicted class values of Test data :", y_pred)

print("Accuracy of the model :")
print(knn.score(X_test, y_test))

print("Confusion matrix of the model :")
cm = confusion_matrix(y_test, y_pred)
print(cm)

plt.figure(figsize=(7,5))

# Graphical representation of data using colors to visualize
# If annot = True, write the data value on the heatmap

sn.heatmap(cm, annot=True)
plt.xlabel('Predicted')
plt.ylabel('Truth')

plt.show()
