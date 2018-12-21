import pandas as pd
import numpy as np

infos = pd.read_csv("ACTION.csv")
#클라이언트ID와 세션ID를 입력하면 검색어와 횟수를 반환해주는 함수
def info_return(a):
    b = int(a)
    info = list(infos[infos['CLNT_ID_SESS_ID'] == 37573389649532]['ACTION'])
    for i in range(0,len(info)):
        print(info[i], "\n")

