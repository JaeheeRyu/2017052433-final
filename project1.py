import pandas as pd
import Visualization

#히스토그램 생성
data_frame = pd.read_csv("view time buy.csv")
data_frame2 = pd.read_csv("view time notbuy.csv")
a = data_frame['TOT_SESS_HR_V']
b = data_frame2['TOT_SESS_HR_V']
Visualization.Show_Histogram(b)
Visualization.Show_Histogram(a)



import numpy as np
input_file = "01.Custom.csv"
input_file2 = "05.Session.csv"

#성별기준 customer 파이차트 생성
M=0
F=0
data_frame = pd.read_csv(input_file)
a = list(data_frame['CLNT_GENDER'])
for gender in a:
    if gender == 'M':
        M = M+1
    elif gender == 'F':
        F = F+1


gender_list_label = ['남자', '여자']
gender_list_value = [M, F]
Visualization.Show_Piechart(gender_list_label, gender_list_value)

#연령기준 customer 파이차트 생성
Age10 =0
Age20 =0
Age30 =0
Age40 =0
AgeElse =0

data_frame = pd.read_csv(input_file)
a = list(data_frame['CLNT_AGE'])
for age in a:
    if age == 10:
        Age10 = Age10+1
    elif age == 20:
        Age20 = Age20 + 1
    elif age == 30:
        Age30 = Age30 + 1
    elif age == 40:
        Age40 = Age40 + 1
    else:
        AgeElse += 1

age_list_label = ['10대', '20대', '30대', '40대', '기타']
age_list_value = [Age10, Age20, Age30, Age40, AgeElse]
#Visualization.Show_Piechart(age_list_label, age_list_value)


#구매환경기준 customer 파이차트 생성
Mobile=0
Desktop=0
Tablet=0
data_frame = pd.read_csv(input_file2)
a = list(data_frame['DVC_CTG_NM'])
for usase in a:
    if usase == 'mobile':
        Mobile = Mobile+1
    elif usase == 'desktop':
        Desktop = Desktop+1
    else:
        Tablet = Tablet+1

usase_list_label = ['Mobile', 'Desktop', 'Tablet']
usase_list_value = [Mobile, Desktop, Desktop]
#Visualization.Show_Piechart(usase_list_label, usase_list_value)


#구매환경기준 customer 파이차트 생성
Mobile=0
Desktop=0
Tablet=0
data_frame = pd.read_csv(input_file2)
a = list(data_frame['DVC_CTG_NM'])
for usase in a:
    if usase == 'mobile':
        Mobile = Mobile+1
    elif usase == 'desktop':
        Desktop = Desktop+1
    else:
        Tablet = Tablet+1

usase_list_label = ['Mobile', 'Desktop', 'Tablet']
usase_list_value = [Mobile, Desktop, Desktop]
#Visualization.Show_Piechart(usase_list_label, usase_list_value)

#히스토그램 생성
data_frame = pd.read_csv("view time buy.csv")
a = list(data_frame['TOT_PAG_VIEW_CT'])
Visualization.Show_Histogram(a)