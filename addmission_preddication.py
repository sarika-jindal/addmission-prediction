# -*- coding: utf-8 -*-
"""addmission preddication

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1W5AmTIJTweHOgtxe1AkNAHN0APm37aig
"""

import pandas as pd

addmission = pd.read_csv('https://github.com/YBIFoundation/Dataset/raw/main/Admission%20Chance.csv')

addmission.head()

addmission.info()

addmission.describe()

# define target (y) and features (X)

addmission.columns

y = addmission['Chance of Admit ']

X = addmission .drop (['Serial No','Chance of Admit '],axis=1)

#from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, train_size=0.7, random_state=2529)

X_train.shape, X_test.shape, y_train.shape, y_test.shape

from sklearn.linear_model import LinearRegression
model = LinearRegression()

model.fit(X_train,y_train)

model.intercept_

model.coef_

y_pred = model.predict(X_test)

y_pred

from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, mean_squared_error

mean_absolute_error(y_test,y_pred)

mean_absolute_percentage_error(y_test,y_pred)

mean_squared_error(y_test,y_pred)