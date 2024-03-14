import numpy
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

iris= pd.read_csv("Datasets/iris.csv")
print(iris.head())

x = iris.drop("species", axis=1)
y = iris["species"]

x_train, x_test, y_train, y_test = train_test_split(x, y,test_size=0.2,random_state=42)


decisiontree = DecisionTreeClassifier()

decisiontree.fit(x_train, y_train)
x=decisiontree.predict(x_test)
print(x)