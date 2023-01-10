# encoding:utf-8
__author__ = 'wwy'

'''
此Python脚本是对《弹道导弹攻防对抗的建模与仿真》第11章《有突防措施条件下多枚战略弹道导弹突防反导防御系统体系效能模型》的复现。
此书作者：罗小明，出版社：国防工业出版社，文章内容属非涉密范畴。
这里主要结合作者观点，建立体系效能模型，定量研究多弹头和诱饵的影响下，多枚战略弹道导弹在反导防御系统采取不同的拦截方式和拦截
策略情况下的突防效能，并从防御方的角度，建模分析了反导防御方要达到一定的防御效能所需的拦截弹数。
在建模之前，给出以下假设条件：
(1)各枚战略弹道导弹弹头之间相互无影响。
(2)反导防御系统在某一段拦截时，若采取相同的拦截策略且在该段拦截弹未消耗完的条件下，采取相同突防措施的各枚战略弹道导弹弹头在该
段的突防概率相同。
'''

import math
from numpy import *
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.family'] = 'SimHei' # 设置中文字体
rcParams['axes.unicode_minus'] = False  # 解决坐标轴负数的负号显示问题）


parameter = input("是否使用书中预置参数：(Y / N)")
if(parameter == 'N' or parameter == 'n'):
#--------------------------------------用户输入(常量)--------------------------------
    print("--------------------进攻方参数--------------------")
    w = input("请输入发射导弹数：")
    w = int(w)
    Pr = input("请输入可靠性：")
    Pr = int(Pr)
    k = input("请输入分弹头数：")
    k = int(k)
    Mh = input("请输入重诱饵数：")
    Mh = int(Mh)
    Ml = input("请输入轻诱饵数：")
    Ml = int(Ml)
    n1 = input("请输入反导防御系统用于助推段的拦截弹数(注意，助推段拦截弹数会影响后续三段)：")
    n1 = int(n1)
    n2 = input("请输入反导防御系统用于上升段的拦截弹数(注意，上升段拦截弹数会影响后续二段)：")
    n2 = int(n2)
    n3 = input("请输入反导防御系统用于中段的拦截弹数(注意，中段拦截弹数会影响末段)：")
    n3 = int(n3)
    n4 = input("请输入反导防御系统用于末段的拦截弹数：")
    n4 = int(n4)

    print("--------------------助推段拦截参数--------------------")
    Pd1 = input("请输入发现概率：")
    Pd1 = float(Pd1)
    Pt1 = input("请输入跟踪概率：")
    Pt1 = float(Pt1)
    Pww1 = input("请输入识别概率：")
    Pww1 = float(Pww1)
    Plj1 = input("请输入单枚拦截概率：")
    Plj1 = float(Plj1)

    print("--------------------上升段拦截参数--------------------")
    Pd2 = input("请输入发现概率：")
    Pd2 = float(Pd2)
    Pt2 = input("请输入跟踪概率：")
    Pt2 = float(Pt2)
    Pww2 = input("请输入识别概率：")
    Pww2 = float(Pww2)
    Plj2 = input("请输入单枚拦截概率：")
    Plj2 = float(Plj2)

    print("--------------------中段拦截参数--------------------")
    print("-------中段地基拦截参数-------")
    print("----弹头----")
    print("--初次--")
    Pd3 = input("请输入发现概率：")
    Pd3 = float(Pd3)
    Pt3 = input("请输入跟踪概率：")
    Pt3 = float(Pt3)
    Pww3 = input("请输入识别概率：")
    Pww3 = float(Pww3)
    Plj3 = input("请输入单枚拦截概率：")
    Plj3 = float(Plj3)

    print("--再次--")
    Pd32 = input("请输入发现概率：")
    Pd32 = float(Pd32)
    Pt32 = input("请输入跟踪概率：")
    Pt32 = float(Pt32)
    Pww32 = input("请输入识别概率：")
    Pww32 = float(Pww32)
    Plj32 = input("请输入单枚拦截概率：")
    Plj32 = float(Plj32)

    print("----重诱饵----")
    print("--初次--")
    Phd3 = input("请输入发现概率：")
    Phd3 = float(Phd3)
    Pht3 = input("请输入跟踪概率：")
    Pht3 = float(Pht3)
    Phw3 = input("请输入识别概率：")
    Phw3 = float(Phw3)
    Phlj3 = input("请输入单枚拦截概率：")
    Phlj3 = float(Phlj3)

    print("--再次--")
    Phd32 = input("请输入发现概率：")
    Phd32 = float(Phd32)
    Pht32 = input("请输入跟踪概率：")
    Pht32 = float(Pht32)
    Phw32 = input("请输入识别概率：")
    Phw32 = float(Phw32)
    Phlj32 = input("请输入单枚拦截概率：")
    Phlj32 = float(Phlj32)

    print("----轻诱饵----")
    print("--初次--")
    Pld3 = input("请输入发现概率：")
    Pld3 = float(Pld3)
    Plt3 = input("请输入跟踪概率：")
    Plt3 = float(Plt3)
    Plw3 = input("请输入识别概率：")
    Plw3 = float(Plw3)
    Pllj3 = input("请输入单枚拦截概率：")
    Pllj3 = float(Pllj3)

    print("--再次--")
    Pld32 = input("请输入发现概率：")
    Pld32 = float(Pld32)
    Plt32 = input("请输入跟踪概率：")
    Plt32 = float(Plt32)
    Plw32 = input("请输入识别概率：")
    Plw32 = float(Plw32)
    Pllj32 = input("请输入单枚拦截概率：")
    Pllj32 = float(Pllj32)

    print("--------------------末段拦截参数--------------------")
    print("----弹头----")
    Pd4 = input("请输入发现概率：")
    Pd4 = float(Pd4)
    Pt4 = input("请输入跟踪概率：")
    Pt4 = float(Pt4)
    Pww4 = input("请输入识别概率：")
    Pww4 = float(Pww4)
    Plj4 = input("请输入单枚拦截概率：")
    Plj4 = float(Plj4)

    print("----重诱饵----")
    Phd4 = input("请输入发现概率：")
    Phd4 = float(Phd4)
    Pht4 = input("请输入跟踪概率：")
    Pht4 = float(Pht4)
    Phw4 = input("请输入识别概率：")
    Phw4 = float(Phw4)
    Phlj4 = input("请输入单枚拦截概率：")
    Phlj4 = float(Phlj4)

else:
#--------------------------------------书中所给的初始值(常量)--------------------------------
    w = 12
    Pr = 0.9
    k = 1
    Mh = 3
    Ml = 8
    n1 = 0
    n2 = 0
    n3 = 40
    n4 = 0

    Pd1 = 0.85
    Pt1 = 0.7
    Pww1 = 0.7
    Plj1 = 0.6

    Pd2 = 0.85
    Pt2 = 0.7
    Pww2 = 0.7
    Plj2 = 0.6

    Pd3 = 0.8
    Pt3 = 0.82
    Pww3 = 0.85
    Plj3 = 0.65
    Pd32 = 0.85
    Pt32 = 0.86
    Pww32 = 0.9
    Plj32 = 0.65

    Phd3 = 0.8
    Pht3 = 0.7
    Phw3 = 0.2
    Phlj3 = 0.7
    Phd32 = 0.85
    Pht32 = 0.75
    Phw32 = 0.1
    Phlj32 = 0.7

    Pld3 = 0.8
    Plt3 = 0.7
    Plw3 = 0.1
    Pllj3 = 0.7

    Pld32 = 0.85
    Plt32 = 0.75
    Plw32 = 0.05
    Pllj32 = 0.7

    Pd4 = 0.8
    Pt4 = 0.7
    Pww4 = 0.1
    Plj4 = 0.7

    Phd4 = 0.85
    Pht4 = 0.75
    Phw4 = 0.05
    Phlj4 = 0.7


set1 = False
set2 = False
set3 = False
set4 = False

list1234 = []
if(n1 > 0):
    list1234.append("1 助推段")
    set1 = True
if(n2 > 0):
    list1234.append("2 上升段")
    set2 = True
if(n3 > 0):
    list1234.append("3 中段路基")
    set3 = True
if(n4 > 0):
    list1234.append("4 末段")
    set4 = True
if(n1 + n2 + n3 + n4 == 0):
    print("防御方拦截段无效,请重新确认各段拦截弹数......")
    

print("识别防御方拦截段处于-->")
for i in list1234:
    print(i)

num = input("请选择要分析的拦截段序号：")
if(num == str(3)):
    print("中段路基包含3种因素：")
    print("3.1 中段路基——弹头")
    print("3.2 中段路基——重诱饵")
    print("3.3 中段路基——轻诱饵")
    num = input("请选择具体因素：")
if(num == str(4)):
    print("末段包含2种因素：")
    print("4.1 末段——弹头")
    print("4.2 末段——重诱饵")
    num = input("请选择具体因素：")


#--------------------------------------多枚战略弹道导弹突防效能模型--------------------------------

#1.反导防御系统采取不同拦截方式和拦截策略时，单枚战略弹道导弹弹头在各飞行段突防概率的计算模型
#战略弹道导弹数w,单枚弹道导弹弹头最终突防效率为q,弹头在助推段的突防概率为q1,弹头在上升段的突防概率为q2,弹头在中段的突防概率为q3,
#弹头在末段的突防概率为q4
#q = q1 * q2 * q3 * q4
#(1)助推段拦截(导弹未释放弹头和诱饵,需考虑助推阶段弹头可靠性。设战略弹道导弹可靠性为Pr(0-1),反导防御系统用于助推段的拦截弹数为n1,
#该段导弹被发现概率为Pd1,被跟踪概率为Pt1,被识别为导弹的概率为Pww1,单枚拦截概率为Plj1)
#a.采用"二拦一"策略
def func1_1(n1,w,Pr,Pd1,Pt1,Pww1,Plj1):
    if(n1 >= 2 * w * Pr * Pd1 * Pt1 * Pww1):
        q1 = Pr - Pr * Pd1 * Pt1 * Pww1 * (1 - math.pow((1 - Plj1), 2))
        q1a = q1
        q1b = Pr
        n11 = w
        n12 = 0
    else:
        q1 = Pr - (n1 * (Pr - math.pow((1 - Plj1), 2))) / 2 * w
        q1a = math.pow((1 - Plj1), 2)
        q1b = Pr
        n11 = n1 / 2
        n12 = w - n1 / 2
    
    return q1,q1a,q1b,n11,n12

#b.采用"四拦一"策略
def func1_2(n1,w,Pr,Pd1,Pt1,Pww1,Plj1):
    if(n1 >= 4 * w * Pr * Pd1 * Pt1 * Pww1):
        q1 = Pr - Pr * Pd1 * Pt1 * Pww1 * (1 - math.pow((1 - Plj1), 4))
        q1a = q1
        q1b = Pr
        n11 = w
        n12 = 0
    else:
        q1 = Pr - (n1 * (Pr - math.pow((1 - Plj1), 4))) / 4 * w
        q1a = math.pow((1 - Plj1), 4)
        q1b = Pr
        n11 = n1 / 4
        n12 = w - n1 / 4

    return q1,q1a,q1b,n11,n12

#(2)上升段拦截(未释放弹头和诱饵,发动机关机，无需考虑弹头可靠性。设反导防御系统用于上升段的拦截弹数为n2,该段导弹被发现概率为Pd2,
#被跟踪概率为Pt2,被识别为导弹的概率为Pww2,单枚拦截概率为Plj2)
#a.采用"二拦一"策略
def func2_1(n2,w,Pd2,Pt2,Pww2,Plj2):
    if(n2 >= 2 * w * Pd2 * Pt2 * Pww2):
        q2 = 1 - Pd2 * Pt2 * Pww2 * (1 - math.pow((1 - Plj2), 2))
        q2a = q2
        q2b = 1
        n21 = w
        n22 = 0
    else:
        q2 = 1 - (n2 * (1 - math.pow((1 - Plj2), 2))) / 2 * w
        q2a = math.pow((1 - Plj2), 2)
        q2b = 1
        n21 = n2 / 2
        n22 = w - n2 / 2

    return q2,q2a,q2b,n21,n22

#b.采用"四拦一"策略
def func2_2(n2,w,Pd2,Pt2,Pww2,Plj2):
    if(n2 >= 4 * w * Pd2 * Pt2 * Pww2):
        q2 = 1 - Pd2 * Pt2 * Pww2 * (1 - math.pow((1 - Plj2), 4))
        q2a = q2
        q2b = 1
        n21 = w
        n22 = 0
    else:
        q2 = 1 - (n2 * (1 - math.pow((1 - Plj2), 4))) / 4 * w
        q2a = math.pow((1 - Plj2), 4)
        q2b = 1
        n21 = n2 / 4
        n22 = w - n2 / 4

    return q2,q2a,q2b,n21,n22

#(3)中段拦截(考虑重诱饵和轻诱饵的影响。设一枚战略弹道导弹分导弹头数为k,携带的重诱饵数为Mh,轻诱饵数为Ml，反导防御系统用于中段的
#拦截弹数为n3(包括海基和路基拦截弹),重诱饵在中段突防的概率为qh3,反导防御系统在中段的视在弹头数量为w3)
#该段弹头被发现概率为Pd3,被跟踪概率为Pt3,被识别为弹头的概率为Pww3,单枚拦截概率为Plj3
#该段重诱饵被发现概率为Phd3,被跟踪概率为Pht3,被识别为弹头的概率为Phw3,单枚拦截概率为Phlj3
#该段轻诱饵被发现概率为Pld3,被跟踪概率为Plt3,被识别为弹头的概率为Plw3,单枚拦截概率为Pllj3
#a.采用"二拦一"策略
def func3_1(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pht3,Phw3,Phlj3,Pld3,Plt3,Plw3,Pllj3):
    w3 = w * k * Pd3 * Pt3 * Pww3 + w * q1 * q2 * Mh * Phd3 * Pht3 * Phw3 + w * q1 * q2 * Ml * Pld3 * Plt3 * Plw3
    if(n3 >= 2 * w3):
        q3 = 1 - Pd3 * Pt3 * Pww3 * (1 - math.pow((1 - Plj3), 2))
        qh3 = 1 - Phd3 * Pht3 * Phw3 * (1 - math.pow((1 - Phlj3), 2))
        q3a = q3
        q3b = 1
        n31 = w * k
        n32 = 0
    else:
        q3 = 1 - (n3 * Pd3 * Pt3 * Pww3 *(math.pow(1 - (1 - Plj3), 2))) / (2 * w3)
        qh3 = 1 - (n3 * Phd3 * Pht3 * Phw3 *(math.pow(1 - (1 - Phlj3), 2))) / (2 * w3)
        q3a = 1 - Pd3 * Pt3 * Pww3 * (1 - math.pow((1 - Plj3), 2))
        q3b = 1
        n31 = (n3 / 2) * (w * k / w3)
        n32 = w * k - (n3 / 2) * (w * k / w3)

    return q3,q3a,q3b,n31,n32

#b.采用"四拦一"策略
def func3_2(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pht3,Phw3,Phlj3,Pld3,Plt3,Plw3,Pllj3):
    w3 = w * k * Pd3 * Pt3 * Pww3 + w * q1 * q2 * Mh * Phd3 * Pht3 * Phw3 + w * q1 * q2 * Ml * Pld3 * Plt3 * Plw3
    if(n3 >= 4 * w3):
        q3 = 1 - Pd3 * Pt3 * Pww3 * (1 - math.pow((1 - Plj3), 4))
        qh3 = 1 - Phd3 * Pht3 * Phw3 * (1 - math.pow((1 - Phlj3), 4))
        q3a = q3
        q3b = 1
        n31 = w * k
        n32 = 0
    else:
        q3 = 1 - (n3 * Pd3 * Pt3 * Pww3 *(math.pow(1 - (1 - Plj3), 4))) / (4 * w3)
        qh3 = 1 - (n3 * Phd3 * Pht3 * Phw3 *(math.pow(1 - (1 - Phlj3), 4))) / (4 * w3)
        q3a = 1 - Pd3 * Pt3 * Pww3 * (1 - math.pow((1 - Plj3), 4))
        q3b = 1
        n31 = (n3 / 4) * (w * k / w3)
        n32 = w * k - (n3 / 4) * (w * k / w3)

    return q3,q3a,q3b,n31,n32

#c.采用"射击-观察-射击"策略(反导防御系统对第一次射击之后的弹头和诱饵重新进行探测、跟踪、识别和拦截,假设第二次射击时的视在弹头数量为w32)
#设第二次射击时：
#弹头被发现的概率为Pd32,被跟踪概率为Pt32,被识别为弹头的概率为Pww32,单枚拦截概率为Plj32
#重诱饵被发现的概率为Phd32,被跟踪概率为Pht32,被识别为弹头的概率为Phw32,单枚拦截概率为Phlj32
#轻诱饵被发现的概率为Pld32,被跟踪概率为Plt32,被识别为弹头的概率为Plw32,单枚拦截概率为Pllj32
def func3_3(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pht3,Phw3,Phlj3,Phd32,Pht32,Phw32,Phlj32,Pld3,Plt3,Plw3,Pllj3,Pld32,Plt32,Plw32,Pllj32):
    w3 = w * k * Pd3 * Pt3 * Pww3 + w * q1 * q2 * Mh * Phd3 * Pht3 * Phw3 + w * q1 * q2 * Ml * Pld3 * Plt3 * Plw3
    w32 = w * k * (1 - Pd3 * Pt3 * Pww3 * (1 - math.pow((1 - Plj3), 2))) * Pd32 * Pt32 * Pww32 + w * q1 * q2 * Mh * (1 - (1 - math.pow((1 - Phlj3), 2)) * Phd3 * Pht3 * Phw3) * Phd32 * Pht32 * Phw32 + w * q1 * q2 * Ml * (1 - (1 - math.pow((1 - Pllj3), 2) * Pld3 * Plt3 * Plw3)) * Pld32 * Plt32 * Plw32
    if(n3 >= 2 * w3 + 2 * w32):
        q3 = (1 - Pd3 * Pt3 * Pww3 * (1 - math.pow((1 - Plj3), 2))) * (1 - Pd32 * Pt32 * Pww32 * (1 - math.pow((1 - Plj32), 2)))
        qh3 = (1 - Phd3 * Pht3 * Phw3 * (1 - math.pow((1 - Phlj3), 2))) * (1 - Phd32 * Pht32 * Phw32 * (1 - math.pow((1 - Phlj32), 2)))
        q3a = q3
        q3b = 1
        n31 = w * k
        n32 = 0
    elif(n3 < 2 * w3):
        q3 = (1 - n3 * Pd3 * Pt3 * Pww3 * (1 - math.pow((1 - Plj3), 2))) / (2 * w3)
        qh3 = (1 - n3 * Phd3 * Pht3 * Phw3 * (1 - math.pow((1 - Phlj3), 2))) / (2 * w3)
        q3a = (1 - Pd3 * Pt3 * Pww3 * (1 - math.pow((1 - Plj3), 2))) * (1 - Pd32 * Pt32 * Pww32 * (1 - math.pow((1 - Plj32), 2)))
        q3b = 1 - Pd3 * Pt3 * Pww3 * (1 - math.pow((1 - Plj3), 2))
        n31 = (n3 / 2 - w3) * (w * k / w32)
        n32 = w * k - (n3 / 2 - w3) * (w * k / w32)
    else:
        q3 = (1 - Pd3 * Pt3 * Pww3 * (1 - math.pow((1 - Plj3), 2))) * (1 - Pd32 * Pt32 * Pww32 * (1 - math.pow((1 - Plj32), 2)) * (n3 - 2 * w3) / (2 * w32))
        qh3 = (1 - Phd3 * Pht3 * Phw3 * (1 - math.pow((1 - Phlj3), 2))) * (1 - Phd32 * Pht32 * Phw32 * (1 - math.pow((1 - Phlj32), 2)) * (n3 - 2 * w3) / (2 * w32))
        q3a = 1 - Pd3 * Pt3 * Pww3 * (1 - math.pow((1 - Plj3), 2))
        q3b = 1
        n31 = n3 / 2 * (w * k / w3)
        n32 = w * k - n3 / 2 * (w * k / w3)

    return q3,q3a,q3b,n31,n32

#(4)末段拦截(末段轻诱饵被大气层过滤掉,只有重诱饵能盐湖弹头突防，因此该段拦截仅考虑在中段没有被拦截掉的重诱饵的影响。)
#设反导防御系统用于末端的拦截弹数为n4,该段视在弹头数量为w4,且：
#弹头被发现的概率为Pd4,被跟踪概率为Pt4,被识别为弹头的概率为Pww4,单枚拦截概率为Plj4
#重诱饵被发现的概率为Phd4,被跟踪概率为Pht4,被识别为弹头的概率为Phw4,单枚拦截概率为Phlj4
#a.采用"二拦一"策略
def func4_1(q1,q2,Mh,n4,w,Pd4,Pt4,Pww4,Plj4,Phd4,Pht4,Phw4):
    w4 = w * k * Pd4 * Pt4 * Pww4 + w * Mh * q1 * q2 * Phd4 * Pht4 * Phw4
    if(n4 >= 2 * w4):
        q4 = 1 - Pd4 * Pt4 * Pww4 * (1 - math.pow((1 - Plj4), 2))
        q4a = q4
        q4b = 1
        n41 = w * k
        n42 = 0
    else:
        q4 = 1 - (n4 * Pd4 * Pt4 * Pww4 *(math.pow(1 - (1 - Plj4), 2))) / (2 * w4)
        q4a = 1 - Pd4 * Pt4 * Pww4 * (1 - math.pow((1 - Plj4), 2))
        q4b = 1
        n41 = (n4 / 2) * (w * k / w4)
        n42 = w * k - (n4 / 2) * (w * k / w4)

    return q4,q4a,q4b,n41,n42

#b.采用"四拦一"策略
def func4_2(q1,q2,Mh,n4,w,Pd4,Pt4,Pww4,Plj4,Phd4,Pht4,Phw4):
    w4 = w * k * Pd4 * Pt4 * Pww4 + w * Mh * q1 * q2 * Phd4 * Pht4 * Phw4
    if(n4 >= 4 * w4):
        q4 = 1 - Pd4 * Pt4 * Pww4 * (1 - math.pow((1 - Plj4), 4))
        q4a = q4
        q4b = 1
        n41 = w * k
        n42 = 0
    else:
        q4 = 1 - (n4 * Pd4 * Pt4 * Pww4 *(math.pow(1 - (1 - Plj4), 4))) / (4 * w4)
        q4a = 1 - Pd4 * Pt4 * Pww4 * (1 - math.pow((1 - Plj4), 4))
        q4b = 1
        n41 = (n4 / 4) * (w * k / w4)
        n42 = w * k - (n4 / 4) * (w * k / w4)

    return q4,q4a,q4b,n41,n42

#2.用平均突防弹头数和弹头突防效率为准则，衡量多枚弹道导弹突防效能的模型
#平均突防弹头数为N,弹头突防效率为F
def sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42):
    #(1)四层拦截(助推段、上升段、中段和末段均拦截,且各段的拦截弹数都足够,设此时弹头的突防概率为Pp1,突防概率为Pt1的弹头为a1)
    Pp1 = q1a * q2a * q3a * q4a
    a1 = n11 * k * n21 * n31 * n41 / ((n21 + n22) * (n31 + n32) * (n41 + n42))

    #(2)三层拦截(助推段、上升段和中段拦截,且各段的拦截弹数都足够,设此时弹头的突防概率为Pp2,突防概率为Pp1的弹头为a2)
    Pp2 = q1a * q2a * q3a * q4b
    a2 = n11 * k * n21 * n31 * n42 / ((n21 + n22) * (n31 + n32) * (n41 + n42))

    #(3)三层拦截(助推段、上升段和末段拦截,且各段的拦截弹数都足够,设此时弹头的突防概率为Pp3,突防概率为Pp3的弹头为a3)
    Pp3 = q1a * q2a * q3b * q4a
    a3 = n11 * k * n21 * n32 * n41 / ((n21 + n22) * (n31 + n32) * (n41 + n42))

    #(4)三层拦截(助推段、中段和末段拦截,且各段的拦截弹数都足够,设此时弹头的突防概率为Pp4,突防概率为Pp4的弹头为a4)
    Pp4 = q1a * q2b * q3a * q4a
    a4 = n11 * k * n22 * n31 * n41 / ((n21 + n22) * (n31 + n32) * (n41 + n42))

    #(5)三层拦截(上升段、中段和末段拦截,且各段的拦截弹数都足够,设此时弹头的突防概率为Pp5,突防概率为Pp4的弹头为a5)
    Pp5 = q1b * q2a * q3a * q4a
    a5 = n12 * k * n21 * n31 * n41 / ((n21 + n22) * (n31 + n32) * (n41 + n42))

    #(6)两层拦截(助推段和上升段拦截,且各段的拦截弹数都足够,设此时弹头的突防概率为Pp6,突防概率为Pp6的弹头为a6)
    Pp6 = q1a * q2a * q3b * q4b
    a6 = n11 * k * n21 * n32 * n42 / ((n21 + n22) * (n31 + n32) * (n41 + n42))

    #(7)两层拦截(助推段和中段拦截,且各段的拦截弹数都足够,设此时弹头的突防概率为Pp7,突防概率为Pp7的弹头为a7)
    Pp7 = q1a * q2b * q3a * q4b
    a7 = n11 * k * n22 * n32 * n41 / ((n21 + n22) * (n31 + n32) * (n41 + n42))

    #(8)两层拦截(助推段和末段拦截,且各段的拦截弹数都足够,设此时弹头的突防概率为Pp8,突防概率为Pp8的弹头为a8)
    Pp8 = q1a * q2b * q3b * q4a
    a8 = n11 * k * n22 * n32 * n41 / ((n21 + n22) * (n31 + n32) * (n41 + n42))

    #(9)两层拦截(上升段和中段拦截,且各段的拦截弹数都足够,设此时弹头的突防概率为Pp9,突防概率为Pp9的弹头为a9)
    Pp9 = q1b * q2a * q3a * q4b
    a9 = n12 * k * n21 * n31 * n42 / ((n21 + n22) * (n31 + n32) * (n41 + n42))

    #(10)两层拦截(上升段和末段拦截,且各段的拦截弹数都足够,设此时弹头的突防概率为Pp10,突防概率为Pp10的弹头为a10)
    Pp10 = q1b * q2a * q3b * q4a
    a10 = n12 * k * n21 * n32 * n41 / ((n21 + n22) * (n31 + n32) * (n41 + n42))

    #(11)两层拦截(中段和末段拦截,且各段的拦截弹数都足够,设此时弹头的突防概率为Pp11,突防概率为Pp11的弹头为a11)
    Pp11 = q1b * q2b * q3a * q4a
    a11 = n12 * k * n22 * n31 * n41 / ((n21 + n22) * (n31 + n32) * (n41 + n42))

    #(12)单层拦截(仅助推段拦截,且拦截弹数足够,设此时弹头的突防概率为Pp12,突防概率为Pp12的弹头为a12)
    Pp12 = q1a * q2b * q3b * q4b
    a12 = n11 * k * n22 * n32 * n42 / ((n21 + n22) * (n31 + n32) * (n41 + n42))

    #(13)单层拦截(仅上升段拦截,且拦截弹数足够,设此时弹头的突防概率为Pp13,突防概率为Pp13的弹头为a13)
    Pp13 = q1b * q2a * q3b * q4b
    a13 = n12 * k * n21 * n32 * n42 / ((n21 + n22) * (n31 + n32) * (n41 + n42))

    #(14)单层拦截(仅中段拦截,且拦截弹数足够,设此时弹头的突防概率为Pp14,突防概率为Pp14的弹头为a14)
    Pp14 = q1b * q2b * q3a * q4b
    a14 = n12 * k * n22 * n31 * n42 / ((n21 + n22) * (n31 + n32) * (n41 + n42))

    #(15)单层拦截(仅末段拦截,且拦截弹数足够,设此时弹头的突防概率为Pp15,突防概率为Pp15的弹头为a15)
    Pp15 = q1b * q2b * q3b * q4a
    a15 = n12 * k * n22 * n32 * n41 / ((n21 + n22) * (n31 + n32) * (n41 + n42))

    #(16)任意段拦截,但拦截弹数不够(设此时弹头的突防概率为Pp16,突防概率为Pp16的弹头为a16)
    Pp16 = q1b * q2b * q3b * q4b
    a16 = n12 * k * n22 * n32 * n42 / ((n21 + n22) * (n31 + n32) * (n41 + n42))

    N= 0
    N += Pp1 * a1 
    N += Pp2 * a2 
    N += Pp3 * a3
    N += Pp4 * a4
    N += Pp5 * a5
    N += Pp6 * a6
    N += Pp7 * a7
    N += Pp8 * a8
    N += Pp9 * a9
    N += Pp10 * a10
    N += Pp11 * a11
    N += Pp12 * a12
    N += Pp13 * a13
    N += Pp14 * a14
    N += Pp15 * a15
    N += Pp16 * a16

    F = N / (w * k)

    return F

def matplotfig(x,y1,y2,y3,y4,title):   
    plt.figure(figsize=(15, 7), dpi=100)
    plt.plot(x, y1, c='red', label="发现概率")
    plt.plot(x, y2, c='green', linestyle='--', label="跟踪概率")
    plt.plot(x, y3, c='blue', linestyle='-.', label="识别概率")
    plt.plot(x, y4, c='k', linestyle='-.', label="单发拦截概率")
    plt.scatter(x, y1, c='red')
    plt.scatter(x, y2, c='green')
    plt.scatter(x, y3, c='blue')
    plt.scatter(x, y4, c='k')
    plt.legend(loc='best')
    plt.yticks(linspace(0, 1, 11))
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.xlabel("概率", fontdict={'size': 16})
    plt.ylabel("弹头突防效率", fontdict={'size': 16})
    plt.title(title, fontdict={'size': 18})
    plt.show()


#3.以至少突防一定数量战略弹道导弹弹头的概率为准则，衡量多枚战略弹道导弹突防效能的模型


strategy1 = 0
strategy2 = 0
strategy3 = 0
strategy4 = 0
global q1,q1a,q1b,n11,n12,q2,q2a,q2b,n21,n22,q3,q3a,q3b,n31,n32,q4,q4a,q4b,n41,n42

try:
    if not set1:
        q1 = Pr
        q1a = 0
        n11 = 0
        q1b = Pr
        n12 = w
    else:
        print("助推段包含2种拦截策略：")
        print("1.1 '二拦一'策略")
        print("1.2 '四拦一'策略")
        strategy1 = input("请选择拦截策略：")

    if not set2:
        q2 = 1
        q2a = 0
        n21 = 0
        q2b = 1
        n22 = w
    else:
        print("上升段包含2种拦截策略：")
        print("2.1 '二拦一'策略")
        print("2.2 '四拦一'策略")
        strategy2 = input("请选择拦截策略：")

    if not set3:
        q3 = 1
        qh3 = 1
        q3a = 0
        n31 = 0
        q3b = 1
        n32 = w * k
    else:
        print("中段路基包含3种拦截策略：")
        print("3.1 '二拦一'策略")
        print("3.2 '四拦一'策略")
        print("3.3 '射击——观察——射击'策略")
        strategy3 = input("请选择拦截策略：")

    if not set4:
        q4 = 1
        q4a = 0
        n41 = 0
        q4b = 1
        n42 = w * k
    else:
        print("末段包含2种拦截策略：")
        print("4.1 '二拦一'策略")
        print("4.2 '四拦一'策略")
        strategy4 = input("请选择拦截策略：")

except:
    print("您输入的参数有误，请检查......")


#num == 1,2,3.1,3.2,3.3,4.1,4.2
if(num == str(1)):
    if(strategy1 != 0):
        if(strategy1 == str(1.1)):
            q1,q1a,q1b,n11,n12 = func1_1(n1,w,Pr,Pd1,Pt1,Pww1,Plj1)
        else:
            q1,q1a,q1b,n11,n12 = func1_2(n1,w,Pr,Pd1,Pt1,Pww1,Plj1)

    if(strategy2 != 0):
        if(strategy2 == str(2.1)):
            q2,q2a,q2b,n21,n22 = func2_1(n2,w,Pd2,Pt2,Pww2,Plj2)
        else:
            q2,q2a,q2b,n21,n22 = func2_2(n2,w,Pd2,Pt2,Pww2,Plj2)

    if(strategy3 != 0):
        if(strategy3 == str(3.1)):
            q3,q3a,q3b,n31,n32 = func3_1(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pht3,Phw3,Phlj3,Pld3,Plt3,Plw3,Pllj3)
        elif(strategy3 == str(3.2)):
            q3,q3a,q3b,n31,n32 = func3_2(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pht3,Phw3,Phlj3,Pld3,Plt3,Plw3,Pllj3)
        else:
            q3,q3a,q3b,n31,n32 = func3_3(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pht3,Phw3,Phlj3,Phd32,Pht32,Phw32,Phlj32,Pld3,Plt3,Plw3,Pllj3,Pld32,Plt32,Plw32,Pllj32)

    if(strategy4 != 0):
        if(strategy4 == str(4.1)):
            q4,q4a,q4b,n41,n42 = func4_1(q1,q2,Mh,n4,w,Pd4,Pt4,Pww4,Plj4,Phd4,Pht4,Phw4)
        else:
            q4,q4a,q4b,n41,n42 = func4_2(q1,q2,Mh,n4,w,Pd4,Pt4,Pww4,Plj4,Phd4,Pht4,Phw4)

    if(strategy1 == str(1.1)):
        list_Pd1 = []
        list_Pt1 = []
        list_Pww1 = []
        list_Plj1 = []
        title = "'二拦一'策略时弹头突防效率与反导防御系统对弹头发现、跟踪、识别和单枚拦截概率关系图(助推段)"
        for Pd1_now in linspace(0, 1, 11):
            q1,q1a,q1b,n11,n12 = func1_1(n1,w,Pr,Pd1_now,Pt1,Pww1,Plj1)
            F_Pd1 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pd1.append(F_Pd1)

        for Pt1_now in linspace(0, 1, 11):
            q1,q1a,q1b,n11,n12 = func1_1(n1,w,Pr,Pd1,Pt1_now,Pww1,Plj1)
            F_Pt1 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pt1.append(F_Pt1)

        for Pww1_now in linspace(0, 1, 11):
            q1,q1a,q1b,n11,n12 = func1_1(n1,w,Pr,Pd1,Pt1,Pww1_now,Plj1)
            F_Pww1 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pww1.append(F_Pww1)

        for Plj1_now in linspace(0, 1, 11):
            q1,q1a,q1b,n11,n12 = func1_1(n1,w,Pr,Pd1,Pt1,Pww1,Plj1_now)
            F_Plj1 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Plj1.append(F_Plj1)

        matplotfig(linspace(0, 1, 11),list_Pd1,list_Pt1,list_Pww1,list_Plj1,title)

    else:
        list_Pd1 = []
        list_Pt1 = []
        list_Pww1 = []
        list_Plj1 = []
        title = "'四拦一'策略时弹头突防效率与反导防御系统对弹头发现、跟踪、识别和单枚拦截概率关系图(助推段)"
        for Pd1_now in linspace(0, 1, 11):
            q1,q1a,q1b,n11,n12 = func1_2(n1,w,Pr,Pd1_now,Pt1,Pww1,Plj1)
            F_Pd1 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pd1.append(F_Pd1)

        for Pt1_now in linspace(0, 1, 11):
            q1,q1a,q1b,n11,n12 = func1_2(n1,w,Pr,Pd1,Pt1_now,Pww1,Plj1)
            F_Pt1 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pt1.append(F_Pt1)

        for Pww1_now in linspace(0, 1, 11):
            q1,q1a,q1b,n11,n12 = func1_2(n1,w,Pr,Pd1,Pt1,Pww1_now,Plj1)
            F_Pww1 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pww1.append(F_Pww1)

        for Plj1_now in linspace(0, 1, 11):
            q1,q1a,q1b,n11,n12 = func1_2(n1,w,Pr,Pd1,Pt1,Pww1,Plj1_now)
            F_Plj1 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Plj1.append(F_Plj1)

        matplotfig(linspace(0, 1, 11),list_Pd1,list_Pt1,list_Pww1,list_Plj1,title)


if(num == str(2)):
    if(strategy1 != 0):
        if(strategy1 == str(1.1)):
            q1,q1a,q1b,n11,n12 = func1_1(n1,w,Pr,Pd1,Pt1,Pww1,Plj1)
        else:
            q1,q1a,q1b,n11,n12 = func1_2(n1,w,Pr,Pd1,Pt1,Pww1,Plj1)

    if(strategy2 != 0):
        if(strategy2 == str(2.1)):
            q2,q2a,q2b,n21,n22 = func2_1(n2,w,Pd2,Pt2,Pww2,Plj2)
        else:
            q2,q2a,q2b,n21,n22 = func2_2(n2,w,Pd2,Pt2,Pww2,Plj2)

    if(strategy3 != 0):
        if(strategy3 == str(3.1)):
            q3,q3a,q3b,n31,n32 = func3_1(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pht3,Phw3,Phlj3,Pld3,Plt3,Plw3,Pllj3)
        elif(strategy3 == str(3.2)):
            q3,q3a,q3b,n31,n32 = func3_2(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pht3,Phw3,Phlj3,Pld3,Plt3,Plw3,Pllj3)
        else:
            q3,q3a,q3b,n31,n32 = func3_3(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pht3,Phw3,Phlj3,Phd32,Pht32,Phw32,Phlj32,Pld3,Plt3,Plw3,Pllj3,Pld32,Plt32,Plw32,Pllj32)

    if(strategy4 != 0):
        if(strategy4 == str(4.1)):
            q4,q4a,q4b,n41,n42 = func4_1(q1,q2,Mh,n4,w,Pd4,Pt4,Pww4,Plj4,Phd4,Pht4,Phw4)
        else:
            q4,q4a,q4b,n41,n42 = func4_2(q1,q2,Mh,n4,w,Pd4,Pt4,Pww4,Plj4,Phd4,Pht4,Phw4)

    if(strategy2 == str(2.1)):
        list_Pd2 = []
        list_Pt2 = []
        list_Pww2 = []
        list_Plj2 = []
        title = "'二拦一'策略时弹头突防效率与反导防御系统对弹头发现、跟踪、识别和单枚拦截概率关系图(上升段)"
        for Pd2_now in linspace(0, 1, 11):
            q2,q2a,q2b,n21,n22 = func2_1(n2,w,Pd2_now,Pt2,Pww2,Plj2)
            F_Pd2 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pd2.append(F_Pd2)

        for Pt2_now in linspace(0, 1, 11):
            q2,q2a,q2b,n21,n22 = func2_1(n2,w,Pd2,Pt2_now,Pww2,Plj2)
            F_Pt2 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pt2.append(F_Pt2)

        for Pww2_now in linspace(0, 1, 11):
            q2,q2a,q2b,n21,n22 = func2_1(n2,w,Pd2,Pt2,Pww2_now,Plj2)
            F_Pww2 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pww2.append(F_Pww2)

        for Plj2_now in linspace(0, 1, 11):
            q2,q2a,q2b,n21,n22 = func2_1(n2,w,Pd2,Pt2,Pww2,Plj2_now)
            F_Plj2 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Plj2.append(F_Plj2)

        matplotfig(linspace(0, 1, 11),list_Pd2,list_Pt2,list_Pww2,list_Plj2,title)

    else:
        list_Pd2 = []
        list_Pt2 = []
        list_Pww2 = []
        list_Plj2 = []
        title = "'四拦一'策略时弹头突防效率与反导防御系统对弹头发现、跟踪、识别和单枚拦截概率关系图(上升段)"
        for Pd2_now in linspace(0, 1, 11):
            q2,q2a,q2b,n21,n22 = func2_2(n2,w,Pd2_now,Pt2,Pww2,Plj2)
            F_Pd2 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pd2.append(F_Pd2)

        for Pt2_now in linspace(0, 1, 11):
            q2,q2a,q2b,n21,n22 = func2_2(n2,w,Pd2,Pt2_now,Pww2,Plj2)
            F_Pt2 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pt2.append(F_Pt2)

        for Pww2_now in linspace(0, 1, 11):
            q2,q2a,q2b,n21,n22 = func2_2(n2,w,Pd2,Pt2,Pww2_now,Plj2)
            F_Pww2 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pww2.append(F_Pww2)

        for Plj2_now in linspace(0, 1, 11):
            q2,q2a,q2b,n21,n22 = func2_2(n2,w,Pd2,Pt2,Pww2,Plj2_now)
            F_Plj2 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Plj2.append(F_Plj2)

        matplotfig(linspace(0, 1, 11),list_Pd2,list_Pt2,list_Pww2,list_Plj2,title)


if(num == str(3.1)):
    if(strategy1 != 0):
        if(strategy1 == str(1.1)):
            q1,q1a,q1b,n11,n12 = func1_1(n1,w,Pr,Pd1,Pt1,Pww1,Plj1)
        else:
            q1,q1a,q1b,n11,n12 = func1_2(n1,w,Pr,Pd1,Pt1,Pww1,Plj1)

    if(strategy2 != 0):
        if(strategy2 == str(2.1)):
            q2,q2a,q2b,n21,n22 = func2_1(n2,w,Pd2,Pt2,Pww2,Plj2)
        else:
            q2,q2a,q2b,n21,n22 = func2_2(n2,w,Pd2,Pt2,Pww2,Plj2)

    if(strategy3 != 0):
        if(strategy3 == str(3.1)):
            q3,q3a,q3b,n31,n32 = func3_1(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pht3,Phw3,Phlj3,Pld3,Plt3,Plw3,Pllj3)
        elif(strategy3 == str(3.2)):
            q3,q3a,q3b,n31,n32 = func3_2(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pht3,Phw3,Phlj3,Pld3,Plt3,Plw3,Pllj3)
        else:
            q3,q3a,q3b,n31,n32 = func3_3(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pht3,Phw3,Phlj3,Phd32,Pht32,Phw32,Phlj32,Pld3,Plt3,Plw3,Pllj3,Pld32,Plt32,Plw32,Pllj32)

    if(strategy4 != 0):
        if(strategy4 == str(4.1)):
            q4,q4a,q4b,n41,n42 = func4_1(q1,q2,Mh,n4,w,Pd4,Pt4,Pww4,Plj4,Phd4,Pht4,Phw4)
        else:
            q4,q4a,q4b,n41,n42 = func4_2(q1,q2,Mh,n4,w,Pd4,Pt4,Pww4,Plj4,Phd4,Pht4,Phw4)

    if(strategy3 == str(3.1)):
        list_Pd3 = []
        list_Pt3 = []
        list_Pww3 = []
        list_Plj3 = []
        title = "'二拦一'策略时弹头突防效率与反导防御系统对弹头发现、跟踪、识别和单枚拦截概率关系图(中段)"
        for Pd3_now in linspace(0, 1, 11):
            q3,q3a,q3b,n31,n32 = func3_1(q1,q2,Mh,Ml,n3,w,k,Pd3_now,Pt3,Pww3,Plj3,Phd3,Pht3,Phw3,Phlj3,Pld3,Plt3,Plw3,Pllj3)
            F_Pd3 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pd3.append(F_Pd3)

        for Pt3_now in linspace(0, 1, 11):
            q3,q3a,q3b,n31,n32 = func3_1(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3_now,Pww3,Plj3,Phd3,Pht3,Phw3,Phlj3,Pld3,Plt3,Plw3,Pllj3)
            F_Pt3 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pt3.append(F_Pt3)

        for Pww3_now in linspace(0, 1, 11):
            q3,q3a,q3b,n31,n32 = func3_1(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3_now,Plj3,Phd3,Pht3,Phw3,Phlj3,Pld3,Plt3,Plw3,Pllj3)
            F_Pww3 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pww3.append(F_Pww3)

        for Plj3_now in linspace(0, 1, 11):
            q3,q3a,q3b,n31,n32 = func3_1(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3_now,Phd3,Pht3,Phw3,Phlj3,Pld3,Plt3,Plw3,Pllj3)
            F_Plj3 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Plj3.append(F_Plj3)

        matplotfig(linspace(0, 1, 11),list_Pd3,list_Pt3,list_Pww3,list_Plj3,title)

    elif(strategy3 == str(3.2)):
        list_Pd3 = []
        list_Pt3 = []
        list_Pww3 = []
        list_Plj3 = []
        title = "'四拦一'策略时弹头突防效率与反导防御系统对弹头发现、跟踪、识别和单枚拦截概率关系图(中段)"
        for Pd3_now in linspace(0, 1, 11):
            q3,q3a,q3b,n31,n32 = func3_2(q1,q2,Mh,Ml,n3,w,k,Pd3_now,Pt3,Pww3,Plj3,Phd3,Pht3,Phw3,Phlj3,Pld3,Plt3,Plw3,Pllj3)
            F_Pd3 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pd3.append(F_Pd3)

        for Pt3_now in linspace(0, 1, 11):
            q3,q3a,q3b,n31,n32 = func3_2(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3_now,Pww3,Plj3,Phd3,Pht3,Phw3,Phlj3,Pld3,Plt3,Plw3,Pllj3)
            F_Pt3 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pt3.append(F_Pt3)

        for Pww3_now in linspace(0, 1, 11):
            q3,q3a,q3b,n31,n32 = func3_2(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3_now,Plj3,Phd3,Pht3,Phw3,Phlj3,Pld3,Plt3,Plw3,Pllj3)
            F_Pww3 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pww3.append(F_Pww3)

        for Plj3_now in linspace(0, 1, 11):
            q3,q3a,q3b,n31,n32 = func3_2(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3_now,Phd3,Pht3,Phw3,Phlj3,Pld3,Plt3,Plw3,Pllj3)
            F_Plj3 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Plj3.append(F_Plj3)

        matplotfig(linspace(0, 1, 11),list_Pd3,list_Pt3,list_Pww3,list_Plj3,title)
    
    else:
        list_Pd3 = []
        list_Pt3 = []
        list_Pww3 = []
        list_Plj3 = []
        title = "'射击——观察——射击'策略时弹头突防效率与反导防御系统对弹头发现、跟踪、识别和单枚拦截概率关系图(中段)"
        for Pd3_now in linspace(0, 1, 11):
            q3,q3a,q3b,n31,n32 = func3_3(q1,q2,Mh,Ml,n3,w,k,Pd3_now,Pt3,Pww3,Plj3,Phd3,Pht3,Phw3,Phlj3,Phd32,Pht32,Phw32,Phlj32,Pld3,Plt3,Plw3,Pllj3,Pld32,Plt32,Plw32,Pllj32)
            F_Pd3 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pd3.append(F_Pd3)

        for Pt3_now in linspace(0, 1, 11):
            q3,q3a,q3b,n31,n32 = func3_3(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3_now,Pww3,Plj3,Phd3,Pht3,Phw3,Phlj3,Phd32,Pht32,Phw32,Phlj32,Pld3,Plt3,Plw3,Pllj3,Pld32,Plt32,Plw32,Pllj32)
            F_Pt3 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pt3.append(F_Pt3)

        for Pww3_now in linspace(0, 1, 11):
            q3,q3a,q3b,n31,n32 = func3_3(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3_now,Plj3,Phd3,Pht3,Phw3,Phlj3,Phd32,Pht32,Phw32,Phlj32,Pld3,Plt3,Plw3,Pllj3,Pld32,Plt32,Plw32,Pllj32)
            F_Pww3 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pww3.append(F_Pww3)

        for Plj3_now in linspace(0, 1, 11):
            q3,q3a,q3b,n31,n32 = func3_3(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3_now,Phd3,Pht3,Phw3,Phlj3,Phd32,Pht32,Phw32,Phlj32,Pld3,Plt3,Plw3,Pllj3,Pld32,Plt32,Plw32,Pllj32)
            F_Plj3 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Plj3.append(F_Plj3)

        matplotfig(linspace(0, 1, 11),list_Pd3,list_Pt3,list_Pww3,list_Plj3,title)


if(num == str(3.2)):
    if(strategy1 != 0):
        if(strategy1 == str(1.1)):
            q1,q1a,q1b,n11,n12 = func1_1(n1,w,Pr,Pd1,Pt1,Pww1,Plj1)
        else:
            q1,q1a,q1b,n11,n12 = func1_2(n1,w,Pr,Pd1,Pt1,Pww1,Plj1)

    if(strategy2 != 0):
        if(strategy2 == str(2.1)):
            q2,q2a,q2b,n21,n22 = func2_1(n2,w,Pd2,Pt2,Pww2,Plj2)
        else:
            q2,q2a,q2b,n21,n22 = func2_2(n2,w,Pd2,Pt2,Pww2,Plj2)

    if(strategy3 != 0):
        if(strategy3 == str(3.1)):
            q3,q3a,q3b,n31,n32 = func3_1(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pht3,Phw3,Phlj3,Pld3,Plt3,Plw3,Pllj3)
        elif(strategy3 == str(3.2)):
            q3,q3a,q3b,n31,n32 = func3_2(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pht3,Phw3,Phlj3,Pld3,Plt3,Plw3,Pllj3)
        else:
            q3,q3a,q3b,n31,n32 = func3_3(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pht3,Phw3,Phlj3,Phd32,Pht32,Phw32,Phlj32,Pld3,Plt3,Plw3,Pllj3,Pld32,Plt32,Plw32,Pllj32)

    if(strategy4 != 0):
        if(strategy4 == str(4.1)):
            q4,q4a,q4b,n41,n42 = func4_1(q1,q2,Mh,n4,w,Pd4,Pt4,Pww4,Plj4,Phd4,Pht4,Phw4)
        else:
            q4,q4a,q4b,n41,n42 = func4_2(q1,q2,Mh,n4,w,Pd4,Pt4,Pww4,Plj4,Phd4,Pht4,Phw4)

    if(strategy3 == str(3.1)):
        list_Pd3 = []
        list_Pt3 = []
        list_Pww3 = []
        list_Plj3 = []
        title = "'二拦一'策略时弹头突防效率与反导防御系统对重诱饵发现、跟踪、识别和单枚拦截概率关系图(中段)"
        for Pd3_now in linspace(0, 1, 11):
            q3,q3a,q3b,n31,n32 = func3_1(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Pd3_now,Pht3,Phw3,Phlj3,Pld3,Plt3,Plw3,Pllj3)
            F_Pd3 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pd3.append(F_Pd3)

        for Pt3_now in linspace(0, 1, 11):
            q3,q3a,q3b,n31,n32 = func3_1(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pt3_now,Phw3,Phlj3,Pld3,Plt3,Plw3,Pllj3)
            F_Pt3 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pt3.append(F_Pt3)

        for Pww3_now in linspace(0, 1, 11):
            q3,q3a,q3b,n31,n32 = func3_1(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pht3,Pww3_now,Phlj3,Pld3,Plt3,Plw3,Pllj3)
            F_Pww3 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pww3.append(F_Pww3)

        for Plj3_now in linspace(0, 1, 11):
            q3,q3a,q3b,n31,n32 = func3_1(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pht3,Phw3,Plj3_now,Pld3,Plt3,Plw3,Pllj3)
            F_Plj3 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Plj3.append(F_Plj3)

        matplotfig(linspace(0, 1, 11),list_Pd3,list_Pt3,list_Pww3,list_Plj3,title)

    elif(strategy3 == str(3.2)):
        list_Pd3 = []
        list_Pt3 = []
        list_Pww3 = []
        list_Plj3 = []
        title = "'四拦一'策略时弹头突防效率与反导防御系统对重诱饵发现、跟踪、识别和单枚拦截概率关系图(中段)"
        for Pd3_now in linspace(0, 1, 11):
            q3,q3a,q3b,n31,n32 = func3_2(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Pd3_now,Pht3,Phw3,Phlj3,Pld3,Plt3,Plw3,Pllj3)
            F_Pd3 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pd3.append(F_Pd3)

        for Pt3_now in linspace(0, 1, 11):
            q3,q3a,q3b,n31,n32 = func3_2(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pt3_now,Phw3,Phlj3,Pld3,Plt3,Plw3,Pllj3)
            F_Pt3 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pt3.append(F_Pt3)

        for Pww3_now in linspace(0, 1, 11):
            q3,q3a,q3b,n31,n32 = func3_2(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pht3,Pww3_now,Phlj3,Pld3,Plt3,Plw3,Pllj3)
            F_Pww3 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pww3.append(F_Pww3)

        for Plj3_now in linspace(0, 1, 11):
            q3,q3a,q3b,n31,n32 = func3_2(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pht3,Phw3,Plj3_now,Pld3,Plt3,Plw3,Pllj3)
            F_Plj3 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Plj3.append(F_Plj3)

        matplotfig(linspace(0, 1, 11),list_Pd3,list_Pt3,list_Pww3,list_Plj3,title)
    
    else:
        list_Pd3 = []
        list_Pt3 = []
        list_Pww3 = []
        list_Plj3 = []
        title = "'射击——观察——射击'策略时弹头突防效率与反导防御系统对重诱饵发现、跟踪、识别和单枚拦截概率关系图(中段)"
        for Pd3_now in linspace(0, 1, 11):
            q3,q3a,q3b,n31,n32 = func3_3(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Pd3_now,Pht3,Phw3,Phlj3,Phd32,Pht32,Phw32,Phlj32,Pld3,Plt3,Plw3,Pllj3,Pld32,Plt32,Plw32,Pllj32)
            F_Pd3 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pd3.append(F_Pd3)

        for Pt3_now in linspace(0, 1, 11):
            q3,q3a,q3b,n31,n32 = func3_3(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pt3_now,Phw3,Phlj3,Phd32,Pht32,Phw32,Phlj32,Pld3,Plt3,Plw3,Pllj3,Pld32,Plt32,Plw32,Pllj32)
            F_Pt3 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pt3.append(F_Pt3)

        for Pww3_now in linspace(0, 1, 11):
            q3,q3a,q3b,n31,n32 = func3_3(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pht3,Pww3_now,Phlj3,Phd32,Pht32,Phw32,Phlj32,Pld3,Plt3,Plw3,Pllj3,Pld32,Plt32,Plw32,Pllj32)
            F_Pww3 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pww3.append(F_Pww3)

        for Plj3_now in linspace(0, 1, 11):
            q3,q3a,q3b,n31,n32 = func3_3(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pht3,Phw3,Plj3_now,Phd32,Pht32,Phw32,Phlj32,Pld3,Plt3,Plw3,Pllj3,Pld32,Plt32,Plw32,Pllj32)
            F_Plj3 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Plj3.append(F_Plj3)

        matplotfig(linspace(0, 1, 11),list_Pd3,list_Pt3,list_Pww3,list_Plj3,title)


if(num == str(3.3)):
    if(strategy1 != 0):
        if(strategy1 == str(1.1)):
            q1,q1a,q1b,n11,n12 = func1_1(n1,w,Pr,Pd1,Pt1,Pww1,Plj1)
        else:
            q1,q1a,q1b,n11,n12 = func1_2(n1,w,Pr,Pd1,Pt1,Pww1,Plj1)

    if(strategy2 != 0):
        if(strategy2 == str(2.1)):
            q2,q2a,q2b,n21,n22 = func2_1(n2,w,Pd2,Pt2,Pww2,Plj2)
        else:
            q2,q2a,q2b,n21,n22 = func2_2(n2,w,Pd2,Pt2,Pww2,Plj2)

    if(strategy3 != 0):
        if(strategy3 == str(3.1)):
            q3,q3a,q3b,n31,n32 = func3_1(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pht3,Phw3,Phlj3,Pld3,Plt3,Plw3,Pllj3)
        elif(strategy3 == str(3.2)):
            q3,q3a,q3b,n31,n32 = func3_2(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pht3,Phw3,Phlj3,Pld3,Plt3,Plw3,Pllj3)
        else:
            q3,q3a,q3b,n31,n32 = func3_3(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pht3,Phw3,Phlj3,Phd32,Pht32,Phw32,Phlj32,Pld3,Plt3,Plw3,Pllj3,Pld32,Plt32,Plw32,Pllj32)

    if(strategy4 != 0):
        if(strategy4 == str(4.1)):
            q4,q4a,q4b,n41,n42 = func4_1(q1,q2,Mh,n4,w,Pd4,Pt4,Pww4,Plj4,Phd4,Pht4,Phw4)
        else:
            q4,q4a,q4b,n41,n42 = func4_2(q1,q2,Mh,n4,w,Pd4,Pt4,Pww4,Plj4,Phd4,Pht4,Phw4)

    if(strategy3 == str(3.1)):
        list_Pd3 = []
        list_Pt3 = []
        list_Pww3 = []
        list_Plj3 = []
        title = "'二拦一'策略时弹头突防效率与反导防御系统对轻诱饵发现、跟踪、识别和单枚拦截概率关系图(中段)"
        for Pd3_now in linspace(0, 1, 11):
            q3,q3a,q3b,n31,n32 = func3_1(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pht3,Phw3,Phlj3,Pd3_now,Plt3,Plw3,Pllj3)
            F_Pd3 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pd3.append(F_Pd3)

        for Pt3_now in linspace(0, 1, 11):
            q3,q3a,q3b,n31,n32 = func3_1(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pht3,Phw3,Phlj3,Pld3,Pt3_now,Plw3,Pllj3)
            F_Pt3 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pt3.append(F_Pt3)

        for Pww3_now in linspace(0, 1, 11):
            q3,q3a,q3b,n31,n32 = func3_1(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pht3,Phw3,Phlj3,Pld3,Plt3,Pww3_now,Pllj3)
            F_Pww3 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pww3.append(F_Pww3)

        for Plj3_now in linspace(0, 1, 11):
            q3,q3a,q3b,n31,n32 = func3_1(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pht3,Phw3,Phlj3,Pld3,Plt3,Plw3,Plj3_now)
            F_Plj3 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Plj3.append(F_Plj3)

        matplotfig(linspace(0, 1, 11),list_Pd3,list_Pt3,list_Pww3,list_Plj3,title)

    elif(strategy3 == str(3.2)):
        list_Pd3 = []
        list_Pt3 = []
        list_Pww3 = []
        list_Plj3 = []
        title = "'四拦一'策略时弹头突防效率与反导防御系统对轻诱饵发现、跟踪、识别和单枚拦截概率关系图(中段)"
        for Pd3_now in linspace(0, 1, 11):
            q3,q3a,q3b,n31,n32 = func3_2(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pht3,Phw3,Phlj3,Pd3_now,Plt3,Plw3,Pllj3)
            F_Pd3 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pd3.append(F_Pd3)

        for Pt3_now in linspace(0, 1, 11):
            q3,q3a,q3b,n31,n32 = func3_2(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pht3,Phw3,Phlj3,Pld3,Pt3_now,Plw3,Pllj3)
            F_Pt3 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pt3.append(F_Pt3)

        for Pww3_now in linspace(0, 1, 11):
            q3,q3a,q3b,n31,n32 = func3_2(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pht3,Phw3,Phlj3,Pld3,Plt3,Pww3_now,Pllj3)
            F_Pww3 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pww3.append(F_Pww3)

        for Plj3_now in linspace(0, 1, 11):
            q3,q3a,q3b,n31,n32 = func3_2(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pht3,Phw3,Phlj3,Pld3,Plt3,Plw3,Plj3_now)
            F_Plj3 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Plj3.append(F_Plj3)

        matplotfig(linspace(0, 1, 11),list_Pd3,list_Pt3,list_Pww3,list_Plj3,title)
    
    else:
        list_Pd3 = []
        list_Pt3 = []
        list_Pww3 = []
        list_Plj3 = []
        title = "'射击——观察——射击'策略时弹头突防效率与反导防御系统对轻诱饵发现、跟踪、识别和单枚拦截概率关系图(中段)"
        for Pd3_now in linspace(0, 1, 11):
            q3,q3a,q3b,n31,n32 = func3_3(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pht3,Phw3,Phlj3,Phd32,Pht32,Phw32,Phlj32,Pd3_now,Plt3,Plw3,Pllj3,Pld32,Plt32,Plw32,Pllj32)
            F_Pd3 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pd3.append(F_Pd3)

        for Pt3_now in linspace(0, 1, 11):
            q3,q3a,q3b,n31,n32 = func3_3(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pht3,Phw3,Phlj3,Phd32,Pht32,Phw32,Phlj32,Pld3,Pt3_now,Plw3,Pllj3,Pld32,Plt32,Plw32,Pllj32)
            F_Pt3 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pt3.append(F_Pt3)

        for Pww3_now in linspace(0, 1, 11):
            q3,q3a,q3b,n31,n32 = func3_3(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pht3,Phw3,Phlj3,Phd32,Pht32,Phw32,Phlj32,Pld3,Plt3,Pww3_now,Pllj3,Pld32,Plt32,Plw32,Pllj32)
            F_Pww3 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pww3.append(F_Pww3)

        for Plj3_now in linspace(0, 1, 11):
            q3,q3a,q3b,n31,n32 = func3_3(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pht3,Phw3,Phlj3,Phd32,Pht32,Phw32,Phlj32,Pld3,Plt3,Plw3,Plj3_now,Pld32,Plt32,Plw32,Pllj32)
            F_Plj3 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Plj3.append(F_Plj3)

        matplotfig(linspace(0, 1, 11),list_Pd3,list_Pt3,list_Pww3,list_Plj3,title)


if(num == str(4.1)):
    if(strategy1 != 0):
        if(strategy1 == str(1.1)):
            q1,q1a,q1b,n11,n12 = func1_1(n1,w,Pr,Pd1,Pt1,Pww1,Plj1)
        else:
            q1,q1a,q1b,n11,n12 = func1_2(n1,w,Pr,Pd1,Pt1,Pww1,Plj1)

    if(strategy2 != 0):
        if(strategy2 == str(2.1)):
            q2,q2a,q2b,n21,n22 = func2_1(n2,w,Pd2,Pt2,Pww2,Plj2)
        else:
            q2,q2a,q2b,n21,n22 = func2_2(n2,w,Pd2,Pt2,Pww2,Plj2)

    if(strategy3 != 0):
        if(strategy3 == str(3.1)):
            q3,q3a,q3b,n31,n32 = func3_1(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pht3,Phw3,Phlj3,Pld3,Plt3,Plw3,Pllj3)
        elif(strategy3 == 3.2):
            q3,q3a,q3b,n31,n32 = func3_2(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pht3,Phw3,Phlj3,Pld3,Plt3,Plw3,Pllj3)
        else:
            q3,q3a,q3b,n31,n32 = func3_3(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pht3,Phw3,Phlj3,Phd32,Pht32,Phw32,Phlj32,Pld3,Plt3,Plw3,Pllj3,Pld32,Plt32,Plw32,Pllj32)

    if(strategy4 == str(4.1)):
        list_Pd4 = []
        list_Pt4 = []
        list_Pww4 = []
        list_Plj4 = []
        title = "'二拦一'策略时弹头突防效率与反导防御系统对弹头发现、跟踪、识别和单枚拦截概率关系图(末段)"
        for Pd4_now in linspace(0, 1, 11):
            q4,q4a,q4b,n41,n42 = func4_1(q1,q2,Mh,n4,w,Pd4_now,Pt4,Pww4,Plj4,Phd4,Pht4,Phw4)
            F_Pd4 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pd4.append(F_Pd4)

        for Pt4_now in linspace(0, 1, 11):
            q4,q4a,q4b,n41,n42 = func4_1(q1,q2,Mh,n4,w,Pd4,Pt4_now,Pww4,Plj4,Phd4,Pht4,Phw4)
            F_Pt4 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pt4.append(F_Pt4)

        for Pww4_now in linspace(0, 1, 11):
            q4,q4a,q4b,n41,n42 = func4_1(q1,q2,Mh,n4,w,Pd4,Pt4,Pww4_now,Plj4,Phd4,Pht4,Phw4)
            F_Pww4 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pww4.append(F_Pww4)

        for Plj4_now in linspace(0, 1, 11):
            q4,q4a,q4b,n41,n42 = func4_1(q1,q2,Mh,n4,w,Pd4,Pt4,Pww4,Plj4_now,Phd4,Pht4,Phw4)
            F_Plj4 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Plj4.append(F_Plj4)

        matplotfig(linspace(0, 1, 11),list_Pd4,list_Pt4,list_Pww4,list_Plj4,title)

    else:
        list_Pd4 = []
        list_Pt4 = []
        list_Pww4 = []
        list_Plj4 = []
        title = "'二拦一'策略时弹头突防效率与反导防御系统对弹头发现、跟踪、识别和单枚拦截概率关系图(末段)"
        for Pd4_now in linspace(0, 1, 11):
            q4,q4a,q4b,n41,n42 = func4_2(q1,q2,Mh,n4,w,Pd4_now,Pt4,Pww4,Plj4,Phd4,Pht4,Phw4)
            F_Pd4 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pd4.append(F_Pd4)

        for Pt4_now in linspace(0, 1, 11):
            q4,q4a,q4b,n41,n42 = func4_2(q1,q2,Mh,n4,w,Pd4,Pt4_now,Pww4,Plj4,Phd4,Pht4,Phw4)
            F_Pt4 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pt4.append(F_Pt4)

        for Pww4_now in linspace(0, 1, 11):
            q4,q4a,q4b,n41,n42 = func4_2(q1,q2,Mh,n4,w,Pd4,Pt4,Pww4_now,Plj4,Phd4,Pht4,Phw41)
            F_Pww4 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pww4.append(F_Pww4)

        for Plj4_now in linspace(0, 1, 11):
            q4,q4a,q4b,n41,n42 = func4_2(q1,q2,Mh,n4,w,Pd4,Pt4,Pww4,Plj4_now,Phd4,Pht4,Phw4)
            F_Plj4 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Plj4.append(F_Plj4)

        matplotfig(linspace(0, 1, 11),list_Pd4,list_Pt4,list_Pww4,list_Plj4,title)


if(num == str(4.2)):
    if(strategy1 != 0):
        if(strategy1 == str(1.1)):
            q1,q1a,q1b,n11,n12 = func1_1(n1,w,Pr,Pd1,Pt1,Pww1,Plj1)
        else:
            q1,q1a,q1b,n11,n12 = func1_2(n1,w,Pr,Pd1,Pt1,Pww1,Plj1)

    if(strategy2 != 0):
        if(strategy2 == str(2.1)):
            q2,q2a,q2b,n21,n22 = func2_1(n2,w,Pd2,Pt2,Pww2,Plj2)
        else:
            q2,q2a,q2b,n21,n22 = func2_2(n2,w,Pd2,Pt2,Pww2,Plj2)

    if(strategy3 != 0):
        if(strategy3 == str(3.1)):
            q3,q3a,q3b,n31,n32 = func3_1(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pht3,Phw3,Phlj3,Pld3,Plt3,Plw3,Pllj3)
        elif(strategy3 == 3.2):
            q3,q3a,q3b,n31,n32 = func3_2(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pht3,Phw3,Phlj3,Pld3,Plt3,Plw3,Pllj3)
        else:
            q3,q3a,q3b,n31,n32 = func3_3(q1,q2,Mh,Ml,n3,w,k,Pd3,Pt3,Pww3,Plj3,Phd3,Pht3,Phw3,Phlj3,Phd32,Pht32,Phw32,Phlj32,Pld3,Plt3,Plw3,Pllj3,Pld32,Plt32,Plw32,Pllj32)

    if(strategy4 == str(4.1)):
        list_Pd4 = []
        list_Pt4 = []
        list_Pww4 = []
        list_Plj4 = []
        title = "'四拦一'策略时弹头突防效率与反导防御系统对弹头发现、跟踪、识别和单枚拦截概率关系图(末段)"
        for Pd4_now in linspace(0, 1, 11):
            q4,q4a,q4b,n41,n42 = func4_1(q1,q2,Mh,n4,w,Pd4_now,Pt4,Pww4,Plj4,Phd4,Pht4,Phw4)
            F_Pd4 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pd4.append(F_Pd4)

        for Pt4_now in linspace(0, 1, 11):
            q4,q4a,q4b,n41,n42 = func4_1(q1,q2,Mh,n4,w,Pd4,Pt4_now,Pww4,Plj4,Phd4,Pht4,Phw4)
            F_Pt4 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pt4.append(F_Pt4)

        for Pww4_now in linspace(0, 1, 11):
            q4,q4a,q4b,n41,n42 = func4_1(q1,q2,Mh,n4,w,Pd4,Pt4,Pww4_now,Plj4,Phd4,Pht4,Phw4)
            F_Pww4 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pww4.append(F_Pww4)

        for Plj4_now in linspace(0, 1, 11):
            q4,q4a,q4b,n41,n42 = func4_1(q1,q2,Mh,n4,w,Pd4,Pt4,Pww4,Plj4_now,Phd4,Pht4,Phw4)
            F_Plj4 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Plj4.append(F_Plj4)

        matplotfig(linspace(0, 1, 11),list_Pd4,list_Pt4,list_Pww4,list_Plj4,title)

    else:
        list_Pd4 = []
        list_Pt4 = []
        list_Pww4 = []
        list_Plj4 = []
        title = "'二拦一'策略时弹头突防效率与反导防御系统对弹头发现、跟踪、识别和单枚拦截概率关系图(末段)"
        for Pd4_now in linspace(0, 1, 11):
            q4,q4a,q4b,n41,n42 = func4_2(q1,q2,Mh,n4,w,Pd4_now,Pt4,Pww4,Plj4,Phd4,Pht4,Phw4)
            F_Pd4 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pd4.append(F_Pd4)

        for Pt4_now in linspace(0, 1, 11):
            q4,q4a,q4b,n41,n42 = func4_2(q1,q2,Mh,n4,w,Pd4,Pt4_now,Pww4,Plj4,Phd4,Pht4,Phw4)
            F_Pt4 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pt4.append(F_Pt4)

        for Pww4_now in linspace(0, 1, 11):
            q4,q4a,q4b,n41,n42 = func4_2(q1,q2,Mh,n4,w,Pd4,Pt4,Pww4_now,Plj4,Phd4,Pht4,Phw4)
            F_Pww4 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Pww4.append(F_Pww4)

        for Plj4_now in linspace(0, 1, 11):
            q4,q4a,q4b,n41,n42 = func4_2(q1,q2,Mh,n4,w,Pd4,Pt4,Pww4,Plj4_now,Phd4,Pht4,Phw4)
            F_Plj4 = sumF(q1a,q1b,q2a,q2b,q3a,q3b,q4a,q4b,n11,n12,n21,n22,n31,n32,n41,n42)
            list_Plj4.append(F_Plj4)

        matplotfig(linspace(0, 1, 11),list_Pd4,list_Pt4,list_Pww4,list_Plj4,title)















