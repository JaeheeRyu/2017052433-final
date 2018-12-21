import pandas as pd
#카테고리별 남/녀확률 계산
from pandas import Series, DataFrame

category_list = ["화장품/뷰티케어", "스포츠패션", "퍼스널케어", "유아동의류", "패션잡화", "아웃도어/레저", "시즌스포츠", "남성의류", "여성의류",
                "침구/수예", "건강식품", "문구/사무용품", "출산/육아용품", "주방잡화", "속옷/양말/홈웨어", "상품권", "과일", "식기/조리기구",
                "원예/애완", "인테리어/조명", "음료", "청소/세탁/욕실용품", "생활/주방가전", "완구", "구기/필드스포츠", "세제/위생", "냉장/세탁가전",
                "가구", "모바일", "냉장식품", "축산물", "영상/음향가전", "컴퓨터", "헬스/피트니스", "냉동식품", "계절가전", "자동차용품"]

data_frame = pd.read_csv("Gender_training_set-80%.csv")
count = 0
count_gender = []
M_probability = []
F_probability = []
#1차: 전체 고객 성별 비율 반영된 카테고리별 성별 분류
for category in category_list:
    count_gender = list(data_frame[data_frame['CLAC1_NM']==category]['CLNT_GENDER'].value_counts())
    F_probability.append((count_gender[0]/(count_gender[0]+count_gender[1]))*0.15*100)
    M_probability.append((count_gender[1]/(count_gender[0]+count_gender[1]))*0.85*100)

Class_dict = {}
for i in range(0,37):
    if M_probability[i] < F_probability[i]:
        Class_dict.update({category_list[i]:'F'})
    elif M_probability[i] > F_probability[i]:
        Class_dict.update({category_list[i]:"M"})

#2차: 전체 고객 성별 비율 반영된 카테고리별 성별 분류(모두 F로 분류됨)
count_gender = []
M_probability = []
F_probability = []
for category in category_list:
    count_gender = list(data_frame[data_frame['CLAC1_NM']==category]['CLNT_GENDER'].value_counts())
    F_probability.append((0.85*(count_gender[0]/(count_gender[0]+count_gender[1])))/
                        ((0.85 * (count_gender[0] / (count_gender[0] + count_gender[1])))+
                        (0.15 * (count_gender[1] / (count_gender[0] + count_gender[1]))))*100)
    M_probability.append((0.15*(count_gender[1]/(count_gender[0]+count_gender[1])))/
                        ((0.15 * (count_gender[1] / (count_gender[0] + count_gender[1])))+
                        (0.85 * (count_gender[0] / (count_gender[0] + count_gender[1]))))*100)

Class_dict = {}
for i in range(0,37):
    if M_probability[i] < F_probability[i]:
        Class_dict.update({category_list[i]:'F'})
    elif M_probability[i] > F_probability[i]:
        Class_dict.update({category_list[i]:"M"})

