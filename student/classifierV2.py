import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
train = pd.read_excel('ModifiedNumericDataSetV2.xlsx',index=False)
X = train
y = train['Placed/Unplaced']
Y=y
X=X.drop('Tier',axis=1)
X=X.drop('Placed/Unplaced',axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3,shuffle=False)
clf = RandomForestClassifier(n_estimators=219
                             , max_depth=100,random_state=0)
clf.fit(X_train, y_train)
y_pred=clf.predict(X_test)
cm = confusion_matrix(y_test,y_pred)
clf.predict_proba()
