import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from matplotlib import style

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
style.use('ggplot')
list = []
#수치 정보를 리스트로 받아 히스토그램을 반환하는 함수
def Show_Histogram(a):

    for i in range(0,100):
        list.append(i)
    plt.hist(a)
    plt.hist(a,list)
    plt.show()

#카테고리와 수치 정보를 리스트로 받아 파이차트를 반환하는 함수
def Show_Piechart(a,b):

    labels = a
    ratio = b
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red']
    plt.pie(ratio, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)

    plt.show()


