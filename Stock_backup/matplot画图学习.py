import matplotlib.pyplot as plt
import numpy as np
import math
def chap01():
    #最简单的生成图形的代码
    plt.plot([1,2,3,4,5,6])
    plt.show()

def chap02():
    #最简单的生成图形的代码
    plt.plot([1,2,3,4],[1,4,9,16],'ro') #第一个参数是X  第二个参数是Y 第三个参数是画什么阳的图形
    plt.show()

def chap03():
    plt.plot([1,2,3,4],[1,4,9,16],'ro') #第一个参数是X  第二个参数是Y 第三个参数是画什么阳的图形
    plt.axis([0,5,0,20]) # x轴y轴的起点终点
    plt.show()

#设置关键字：linewith=2.0
#主图，子图
def chap04():
    t=np.arange(0,5,0.1)
    y1=np.sin(2*np.pi*t)
    y2 = np.sin(2 * np.pi * t)
    plt.subplot(211) #画第一个图，上下分成两个，水平的不分，先画第一个图
    plt.plot(t,y1,'b-.')
    plt.subplot(212)#画第一个图，上下分成两个，水平的不分，画第二个图
    plt.plot(t,y2,'r--')

if __name__ == '__main__':
    # chap01()
    #chap02()
    t=np.arange(0,2.5,0.1) #产生一系列数据点，是一个List
    y1 =map(math.sin,math.pi*t) #使用map函数，对x轴的一系列数据点英语sin函数
    y2 = map(math.sin, math.pi * t+math.pi/4)  # 使用map函数，对x轴的一系列数据点英语sin函数
    print(y1)