import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

data=pd.read_csv('cars.csv')
data=data.drop(['Gender','User ID'],axis=1)
x=data.drop(['Purchased'],axis=1)
y=data['Purchased']

from sklearn.ensemble import RandomForestClassifier
rfc=RandomForestClassifier(random_state=0)
rfc.fit(x,y)
ans=rfc.predict(x)

from sklearn.metrics import accuracy_score
print(accuracy_score(y,ans))


import pickle
pickle.dump(rfc,open('pick.pkl','wb'))

model=pickle.load(open('pick.pkl','rb'))
print(model.predict([[22,200000]]))