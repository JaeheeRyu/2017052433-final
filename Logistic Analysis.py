import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

#독립변수(X) - 페이지 조회수(ViewCount), 세션 유지 시간
#종속변수(Y) – 구매(1), 미구매(0)
#위와 같은 데이터로 로지스틱 회귀 분석
df = pd.read_csv('Logistic Analysis.csv')

Y = df['BUY_NOT_BUY']
X = df.iloc[:,0:2]
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, random_state=0)

log_clf = LogisticRegression(solver='lbfgs').fit(X_train,Y_train)
log_clf.score(X_test, Y_test)
