import pandas as pd

#세션시간과 뷰카운트의 상관관계 분석
product = pd.read_csv('Logistic Analysis.csv')
TOT_SESS_HR_V = list(product['TOT_SESS_HR_V'])
TOT_PAG_VIEW_CT = list(product['TOT_PAG_VIEW_CT'])

lst = [TOT_SESS_HR_V,
       TOT_PAG_VIEW_CT]

df = pd.DataFrame(lst).T
corr = df.corr(method = 'pearson')
print(corr)

#세션시간과 검색량의 상관관계 분석
product = pd.read_csv('corr_between_Search_SessionTime.csv')
TOT_SESS_HR_V = list(product['TOT_SESS_HR_V'])
SEARCH_CNT = list(product['SEARCH_CNT'])

lst = [TOT_SESS_HR_V,
       SEARCH_CNT]

df = pd.DataFrame(lst).T
corr = df.corr(method = 'pearson')
print(corr)