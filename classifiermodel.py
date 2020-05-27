import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import accuracy_score
import sys

stdoutOrigin=sys.stdout
sys.stdout = open("/home/srimoyee/Desktop/Srimoyee-PROJECT_REPORT/stage3/Output_final.txt", "w")


df3=pd.read_excel('/home/srimoyee/Desktop/Srimoyee-PROJECT_REPORT/stage1/Merged_data.xlsx', sheet_name='Merged')

le = preprocessing.LabelEncoder()
# Converting string labels into numbers.
df3['salary']=le.fit_transform(df3['salary'])
df3['dept']=le.fit_transform(df3['dept'])

X=df3.drop('left',axis=1)
y=df3['left']

X_train, X_test, y_train, y_test =train_test_split(X,y,test_size=0.3,random_state=42)

cl=GradientBoostingClassifier()

cl.fit(X_train, y_train)


y_pred = cl.predict(X_test)

print('gradient boost')
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test,y_pred))

op=pd.DataFrame({'actual':y_test, 'predicted':y_pred})
print(op)

sys.stdout.close()
sys.stdout=stdoutOrigin

print('gradient boost')
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test,y_pred))





