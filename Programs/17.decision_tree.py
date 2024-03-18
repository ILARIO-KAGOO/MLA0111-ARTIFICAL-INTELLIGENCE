import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

from sklearn.datasets import load_iris
db= load_iris()
iris = pd.DataFrame(data= np.c_[db['data'], db['target']], columns= db['feature_names'] + ['Species'])
print(iris.head())

x = iris.drop("Species", axis=1)
y = iris["Species"]

x_train, x_test, y_train, y_test = train_test_split(x, y,test_size=0.2,random_state=42)


decisiontree = DecisionTreeClassifier()

decisiontree.fit(x_train, y_train)
y=decisiontree.predict(x_test)
print(accuracy_score(y,y_test))