import pandas as pd
import scipy.stats as stats
import researchpy as rp
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Loading data
df = pd.read_csv('Logistic Analysis.csv')
df['BUY_NOT_BUY'].replace({0: 'BUY', 1: 'NOT BUY'}, inplace= True)

np = rp.summary_cont(df['TOT_PAG_VIEW_CT'])
pp = rp . summary_cont (df ['TOT_PAG_VIEW_CT'] . groupby (df ['BUY_NOT_BUY']))
pp.to_csv("output.csv", mode='w', encoding = 'utf-8')

results = ols('TOT_PAG_VIEW_CT ~ C(BUY_NOT_BUY)', data=df).fit()
results.summary()