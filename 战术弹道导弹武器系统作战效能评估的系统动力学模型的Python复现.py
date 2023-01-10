# encoding:utf-8
__author__ = 'wwy'

'''
此Python脚本是对《弹道导弹攻防对抗的建模与仿真》第8章《战术弹道导弹武器系统作战效能评估的系统动力学模型》的复现。
此书作者：罗小明，出版社：国防工业出版社，文章内容属非涉密范畴。
因卫星信息支援下战术弹道导弹武器系统作战效能评估受到许多环节和因素的影响，且相互作用复杂，属于开放式反馈系统，要描述这样
的系统需要多个状态变量，反映多个变量因果关系的模型必定是高阶次的非线性问题；多个决策者、多种功能又使得系统有多个反馈回路。
这里主要结合作者观点，针对影响弹道导弹系统动力学模型建立DYNAMO方程式，根据用户输入，分析各类因素对系统动力学模型的影响情
况，并绘制成图。
'''

import math
import random
import matplotlib.pyplot as plt


#--------------------------------------涉及参数--------------------------------
#q1:蓝方现存兵力水平
#q2:红方预定发射弹道导弹数
#q3:红方规定发射时间(min)
#q4:红方弹道导弹平均飞行时间(min)
#q5:红方弹道导弹杀伤半径(m)
#q6:红方火力突击所需成爆弹量
#q7:红方射前生存阶段弹道导弹数
#q8:红方飞行阶段弹道导弹数
#q9:红方突防弹道导弹数
#q10:红方成爆弹量
#q11:红方弹道导弹生存阶段毁伤率
#q12:红方弹道导弹发射率
#q13:红方弹道导弹成爆率
#q14:红方单枚弹道导弹对蓝方的毁伤率
#q15:红方弹道导弹打击精确率
#q16:红方弹道导弹对蓝方毁伤率
#q17:红方进攻弹相对飞行速度(m/s)
#q18:蓝方单枚拦截导弹的拦截概率
#q19:蓝方拦截导弹的杀伤半径(m)
#q20:蓝方导弹对红方弹道导弹的拦截率
#q21:蓝方拦截导弹数
#q22:蓝方拦截导弹对红方进攻导弹的不确定性半径(m)
#q23:红方成像侦察卫星情报侦察能力
#q24:红方环境监测卫星环境监测能力
#q25:红方导航定位卫星目标定位能力
#q26:红方通信卫星通信容量
#q27:红方通信卫星平均时延(ms)
#q28:红方通信卫星可靠性
#q29:红方指挥控制系统平均时延(ms)
#q30:红方指挥控制能力
#q31:红方作战保障能力对指挥控制能力的影响
#q32:红方指挥保障能力对指挥控制能力的影响
#q33:红方指挥控制系统平均时延对指挥控制能力的影响
#q34:红方信息系统分发系统信息输入量
#q35:红方信息系统分发系统信息容量
#q36:红方信息系统分发系统平均时延(ms)
#q37:红方信息系统分发系统可靠性
#q38:红方弹道导弹武器系统对空防御生存能力
#q39:红方弹道导弹武器系统伪装能力
#q40:蓝方对红方弹道导弹系统二次发现概率
#q41:蓝方飞机机动时间(min)
#q42:蓝方每批次出动飞机数
#q43:蓝方每批次出动飞机的时间间隔(min)
#q44:绿方预警卫星预警探测能力
#q45:绿方预警卫星可靠性
#q46:绿方预警卫星系统、蓝方地基雷达系统对进攻弹的不确定性半径(m)
#q47:蓝方通信卫星通信容量
#q48:蓝方通信卫星平均时延(ms)
#q49:蓝方通信卫星生存能力
#q50:蓝方情报侦察监视系统侦察能力
#q51:蓝方侦察卫星侦察能力
#q52:蓝方其他侦察监视系统侦察能力
#q53:蓝方信息传输分发系统信息输入量
#q54:蓝方信息传输分发系统信息容量
#q55:蓝方信息传输分发系统平均时延(ms)
#q56:蓝方信息传输分发系统的可靠性
#q57:蓝方信息传输分发系统的生存能力
#q58:绿方情报侦察监视系统支援能力

#--------------------------------------用户输入(常量)--------------------------------
#parameter = input("是否使用书中预置参数：(Y / N)")
#if(parameter == 'N' or parameter == 'n'):
print("--------------------红方导弹参数--------------------")
q2 = input("请输入预发导弹数：")
q2 = float(q2)
q3 = input("请输入规定发射时间(min)：")
q3 = float(q3)
q4 = input("请输入平均飞行时间(min)：")
q4 = float(q4)
q5 = input("请输入导弹杀伤半径(m)：")
q5 = float(q5)
q6 = input("请输入火力突击所需成爆量：")
q6 = float(q6)
q13 = input("请输入导弹成爆率(0-1)：")
q13 = float(q13)
q17 = input("请输入进攻弹相对飞行速度(m/s)：")
q17 = float(q17)
q19 = input("请输入蓝方拦截导弹的杀伤半径(m)：")
q19 = float(q19)
V2 = input("请输入导弹发射单元的机动速度(m/s)：")
V2 = float(V2)
q39 = input("请输入导弹武器系统伪装能力(0-1)：")
q39 = float(q39)

print("--------------------红方其他参数--------------------")
q23 = input("请输入红方侦察卫星能力(0-1)：")
q23 = float(q23)
q24 = input("请输入环境监测卫星能力(0-1)：")
q24 = float(q24)
q25 = input("请输入导航定位卫星能力(0-1)：")
q25 = float(q25)
q26 = input("请输入通信卫星通信容量(MHZ)：")
q26 = float(q26)
q31 = input("请输入保障分系统效能的影响(0-1)：")
q31 = float(q31)
q27 = input("请输入通信卫星平均时延(ms)：")
q27 = float(q27)
q28 = input("请输入通信卫星的可靠性(0-1)：")
q28 = float(q28)
u1 = input("请输入每条信息的比特数：")
u1 = float(u1)
q32 = input("请输入指挥分系统效能的影响(0-1)：")
q32 = float(q32)

print("--------------------蓝方作战飞机参数--------------------")
q41 = input("请输入机动时间(min)：")
q41 = float(q41)
q42 = input("请输入每批次出动飞机数：")
q42 = float(q42)
q43 = input("请输入每批次出动飞机的间隔时间(min)：")
q43 = float(q43)
W = input("请输入搜索宽度(m)：")
W = float(W)
V1 = input("请输入搜索速度(m/s)：")
V1 = float(V1)
T1 = input("请输入搜索时间(min)：")
T1 = float(T1)

print("--------------------蓝绿方其他参数--------------------")
q44 = input("请输入绿方预警卫星预警时间(min)：")
q44 = float(q44)
q45 = input("请输入绿方预警卫星的可靠性(0-1)：")
q45 = float(q45)
q46 = input("请输入绿方预警卫星、地基雷达对进攻弹的不确定性半径(m)：")
q46 = float(q46)
q47 = input("请输入蓝方通信卫星通信容量(MHZ)：")
q47 = float(q47)
q48 = input("请输入蓝方通信卫星平均时延(ms)：")
q48 = float(q48)
q49 = input("请输入蓝方通信卫星生存能力(0-1)：")
q49 = float(q49)
q51 = input("请输入蓝方侦察卫星能力(0-1)：")
q51 = float(q51)
q52 = input("请输入蓝方其他侦察系统能力(0-1)：")
q52 = float(q52)
q56 = input("请输入蓝方信息传输分发系统可靠性(0-1)：")
q56 = float(q56)
u2 = input("请输入蓝方每条信息的比特数：")
u2 = float(u2)
q58 = input("请输入绿方侦察监视支援能力(0-1)：")
q58 = float(q58)
#K的值应该不会这么简单，范围应该有些问题，书中并未提到真实数据
K1 = input("请输入比例系数K1的值(q54与q47)：")
K1 = float(K1)
K2 = input("请输入比例系数K2的值(q53与q10)：")
K2 = float(K2)
K3 = input("请输入比例系数K3的值(q35与q26)：")
K3 = float(K3)
K4 = input("请输入比例系数K4的值(q34与q1)：")
K4 = float(K4)
K5 = input("请输入比例系数K5的值(q29与q36)：")
K5 = float(K5)
K6 = input("请输入比例系数K6的值(q37与q28)：")
K6 = float(K6)
#K2 = random.uniform(1, 2)

#else:
'''
#--------------------------------------书中所给的初始值(常量)--------------------------------
    q2 = 18
    q3 = 10
    q4 = 6
    q5 = 25.5
    q6 = 12
    q13 = 0.65
    q17 = 180
    q19 = 10
    V2 = 35
    q39 = 0.78

    q23 = 0.93
    q24 = 0.89
    q25 = 0.9
    q26 = 246.8
    q31 = 0.65
    q27 = 270
    q28 = 0.95
    u1 = 3200
    q32 = 0.75

    q41 = 5
    q42 = 10
    q43 = 0.15
    W = 265
    V1 = 515
    T1 = 45

    q44 = 15
    q45 = 0.83
    q46 = 10.2
    q47 = 250
    q48 =  275.6
    q49 = 0.89
    q51 = 0.82
    q52 = 0.79
    q56 = 0.83
    u2 = 3200
    q58 = 0.91
'''

#--------------------------------------函数关系--------------------------------
def random2():
    a = 0
    b = 0
    a = random.random()
    b = 1 - a
    return [a,b]

def random3():
    c = 0
    d = 0
    e = 0
    c = random.random()
    while True:
        d = random.random()
        e = 1 - c - d
        if(e > 0):
            break
        else:
            continue
    return [c,d,e]

def Rlength(low,step,num):
    list = []
    for i in range(step):
        list.append(low)
        low += num
    return list
    
m = 10000
q1 = m
q10 = 0
q12 = q2 / q3
q30 = 1

N1_2_3 = random3()
N1 = N1_2_3[0]
N2 = N1_2_3[1]
N3 = N1_2_3[2]
N4_5_6 = random3()
N4 = N4_5_6[0]
N5 = N4_5_6[1]
N6 = N4_5_6[2]
N7_8 = random2()
N7 = N7_8[0]
N8 = N7_8[1]
N9_10_11 = random3()
N9 = N9_10_11[0]
N10 = N9_10_11[1]
N11 = N9_10_11[2]
T0 = random.uniform(10, 30) 

def BlueForceLevelVariesOverTime(q1,q10,q12,q30):
    q1_list1 = [m]
    T_list = [0]
    Ts = Rlength(30,19,30)

    for T in Ts:
        q37 = K6 * q28  #q28为常量
        q50 = N7 * q52 + N8 * q51  #q52,q52为常量
        p1 = N4 * q50 + N5 * q58 + N6 * (1 - q39)  #q39,q58为常量
        q35 = K4 * q26  #q26为常量
        q34 = K3 * pow(q1,2)  #初始值 假设q1 = m
        q36 = q27 + 4 / ((1 / u1) * q35 -q34)  #u1为每条信息bit数,q27为常量
        q29 = K5 * q36  #K3,K4,K5
        q54 = K1 * q47  #K1为比例因子,q47为常量
        q53 = K2  * math.pow(q10,2)  #K2为比例因子,初始值 假设q10 = 0
        q55 = q48 + 5 / ((1 / u2) * q54 - q53)  #u2为每条信息bit数,q48为常量
        p2 = 1 - math.exp(-W * V1 * T1 * q42 / (math.pi * math.pow(V2,2) * (q55 + q41 - q29) * (q55 + q41 + T1 - q29)))  ##q41,q42为常量
        q38 = (1 - p1 * p2) * q37
        q33 = 3 * math.exp(-4.5 * math.pow((q29 - q41 - q55) / q41,2)) / (math.pow(2 * math.pi, 1/2) * q41)  #q41为常量
        if(q31 == 1 or q32 == 1 or q33 == 1):
            B = 1
        else:
            B = N9 * q31 + N10 * q32 + N11 * q33  #q31,q32为常量

        q30 = q30 * (1 - B)
        q11 = (1 - q38 - q30 + q38 * q30) / q43  #q43为常量
        if(T == 30):
            q7 = q2
        else:
            q7 = -(q12 + q11) * T  #q7 

        q12 = q7 / q3  #q3为常量
        #q12 = (q2 - q11) * T / (q3 + T)
        q8 = q4 * q12  #q4为常量
        q21 = 2 * q8
        PD_S = q44 - q55  #q44为常量
        if(PD_S < T0): #T0需要给定
            S = float('inf')
        else:
            S = 1

        q57 = q45 * q49  #q45,q49为常量
        q22 = 2 * (10 * q46 * (1 - 0.9 * q53) + q17 * q55) * S / (q56 + q57)  #q17,q46,q56为常量
        q18 = math.pow(q19 / q22, 2)  #q19为常量
        q20 = 1 - math.pow((1 - q18), q21)
        q9 = q8 * (1 - q20)
        q15 = N1 * q23 + N2 * q24 + N3 * q25  #q23,q24,q25为常量,N1\N2\N3
        q14 = math.pi * q15 * math.pow(q5,2)  #q5为常量
        q10 = q9 * q13  #q13为常量
        PD_q16 = q10 - q6  #q6为常量
        if(PD_q16 < 0):
            q16 = 0
        else:
            q16 = q9 * q13 * q14 / q4  #q4,q13为常量

        q1 = -1 * q16 * T
        T_list.append(T)
        q1_list1.append(q1)

    return [T_list,q1_list1]


def BlueForceLevelVariesOverQ23(q1,q10,q12,q30):
    q1_list2 = [m]
    q23_list = [0]
    q23s = Rlength(0,9,0.1)
    T = 60

    for q23 in q23s:
        q37 = K6 * q28  #q28为常量
        q50 = N7 * q52 + N8 * q51  #q52,q52为常量
        p1 = N4 * q50 + N5 * q58 + N6 * (1 - q39)  #q39,q58为常量
        q35 = K4 * q26  #q26为常量
        q34 = K3 * pow(q1,2)  #初始值 假设q1 = m
        q36 = q27 + 4 / ((1 / u1) * q35 -q34)  #u1为每条信息bit数,q27为常量
        q29 = K5 * q36  #K3,K4,K5
        q54 = K1 * q47  #K1为比例因子,q47为常量
        q53 = K2  * math.pow(q10,2)  #K2为比例因子,初始值 假设q10 = 0
        q55 = q48 + 5 / ((1 / u2) * q54 - q53)  #u2为每条信息bit数,q48为常量
        p2 = 1 - math.exp(-W * V1 * T1 * q42 / (math.pi * math.pow(V2,2) * (q55 + q41 - q29) * (q55 + q41 + T1 - q29)))  ##q41,q42为常量
        q38 = (1 - p1 * p2) * q37
        q33 = 3 * math.exp(-4.5 * math.pow((q29 - q41 - q55) / q41,2)) / (math.pow(2 * math.pi, 1/2) * q41)  #q41为常量
        if(q31 == 1 or q32 == 1 or q33 == 1):
            B = 1
        else:
            B = N9 * q31 + N10 * q32 + N11 * q33  #q31,q32为常量

        q30 = q30 * (1 - B)
        q11 = (1 - q38 - q30 + q38 * q30) / q43  #q43为常量
        if(T == 30):
            q7 = q2
        else:
            q7 = -(q12 + q11) * T  #q7 
        q12 = q7 / q3  #q3为常量
        q8 = q4 * q12  #q4为常量
        q21 = 2 * q8
        PD_S = q44 - q55  #q44为常量
        if(PD_S < T0): #T0需要给定
            S = float('inf')
        else:
            S = 1

        q57 = q45 * q49  #q45,q49为常量
        q22 = 2 * (10 * q46 * (1 - 0.9 * q53) + q17 * q55) * S / (q56 + q57)  #q17,q46,q56为常量
        q18 = math.pow(q19 / q22, 2)  #q19为常量
        q20 = 1 - math.pow((1 - q18), q21)
        q9 = q8 * (1 - q20)
        q15 = N1 * q23 + N2 * q24 + N3 * q25  #q23,q24,q25为常量,N1\N2\N3
        q14 = math.pi * q15 * math.pow(q5,2)  #q5为常量
        q10 = q9 * q13  #q13为常量
        PD_q16 = q10 - q6  #q6为常量
        if(PD_q16 < 0):
            q16 = 0
        else:
            q16 = q9 * q13 * q14 / q4  #q4,q13为常量

        q1 = -1 * q16 * T
        q23_list.append(q23)
        q1_list2.append(q1)

    return [q23_list,q1_list2]


def survivingBallisticMissilesOverTime(q1,q10,q12,q30):
    q7_list = []
    T_list = []
    Ts = Rlength(30,20,30)

    for T in Ts:
        q37 = K6 * q28  #q28为常量
        q50 = N7 * q52 + N8 * q51  #q52,q52为常量
        p1 = N4 * q50 + N5 * q58 + N6 * (1 - q39)  #q39,q58为常量
        q35 = K4 * q26  #q26为常量
        q34 = K3 * pow(q1,2)  #初始值 假设q1 = m
        q36 = q27 + 4 / ((1 / u1) * q35 -q34)  #u1为每条信息bit数,q27为常量
        q29 = K5 * q36  #K3,K4,K5
        q54 = K1 * q47  #K1为比例因子,q47为常量
        q53 = K2  * math.pow(q10,2)  #K2为比例因子,初始值 假设q10 = 0
        q55 = q48 + 5 / ((1 / u2) * q54 - q53)  #u2为每条信息bit数,q48为常量
        p2 = 1 - math.exp(-W * V1 * T1 * q42 / (math.pi * math.pow(V2,2) * (q55 + q41 - q29) * (q55 + q41 + T1 - q29)))  ##q41,q42为常量
        q38 = (1 - p1 * p2) * q37
        q33 = 3 * math.exp(-4.5 * math.pow((q29 - q41 - q55) / q41,2)) / (math.pow(2 * math.pi, 1/2) * q41)  #q41为常量
        if(q31 == 1 or q32 == 1 or q33 == 1):
            B = 1
        else:
            B = N9 * q31 + N10 * q32 + N11 * q33  #q31,q32为常量

        q30 = q30 * (1 - B)
        q11 = (1 - q38 - q30 + q38 * q30) / q43  #q43为常量
        if(T == 30):
            q7 = q2
        else:
            q7 = -(q12 + q11) * T  #q7 

        q12 = q7 / q3  #q3为常量
        #q12 = (q2 - q11) * T / (q3 + T)
        q8 = q4 * q12  #q4为常量
        q21 = 2 * q8
        PD_S = q44 - q55  #q44为常量
        if(PD_S < T0): #T0需要给定
            S = float('inf')
        else:
            S = 1

        q57 = q45 * q49  #q45,q49为常量
        q22 = 2 * (10 * q46 * (1 - 0.9 * q53) + q17 * q55) * S / (q56 + q57)  #q17,q46,q56为常量
        q18 = math.pow(q19 / q22, 2)  #q19为常量
        q20 = 1 - math.pow((1 - q18), q21)
        q9 = q8 * (1 - q20)
        q15 = N1 * q23 + N2 * q24 + N3 * q25  #q23,q24,q25为常量,N1\N2\N3
        q14 = math.pi * q15 * math.pow(q5,2)  #q5为常量
        q10 = q9 * q13  #q13为常量
        PD_q16 = q10 - q6  #q6为常量
        if(PD_q16 < 0):
            q16 = 0
        else:
            q16 = q9 * q13 * q14 / q4  #q4,q13为常量

        q1 = -1 * q16 * T
        T_list.append(T)
        q7_list.append(q1)

    return [T_list,q7_list]


def ammunitionOverTime(q1,q10,q12,q30):
    q10_list = []
    T_list = []
    Ts = Rlength(30,20,30)

    for T in Ts:
        q37 = K6 * q28  #q28为常量
        q50 = N7 * q52 + N8 * q51  #q52,q52为常量
        p1 = N4 * q50 + N5 * q58 + N6 * (1 - q39)  #q39,q58为常量
        q35 = K4 * q26  #q26为常量
        q34 = K3 * pow(q1,2)  #初始值 假设q1 = m
        q36 = q27 + 4 / ((1 / u1) * q35 -q34)  #u1为每条信息bit数,q27为常量
        q29 = K5 * q36  #K3,K4,K5
        q54 = K1 * q47  #K1为比例因子,q47为常量
        q53 = K2  * math.pow(q10,2)  #K2为比例因子,初始值 假设q10 = 0
        q55 = q48 + 5 / ((1 / u2) * q54 - q53)  #u2为每条信息bit数,q48为常量
        p2 = 1 - math.exp(-W * V1 * T1 * q42 / (math.pi * math.pow(V2,2) * (q55 + q41 - q29) * (q55 + q41 + T1 - q29)))  ##q41,q42为常量
        q38 = (1 - p1 * p2) * q37
        q33 = 3 * math.exp(-4.5 * math.pow((q29 - q41 - q55) / q41,2)) / (math.pow(2 * math.pi, 1/2) * q41)  #q41为常量
        if(q31 == 1 or q32 == 1 or q33 == 1):
            B = 1
        else:
            B = N9 * q31 + N10 * q32 + N11 * q33  #q31,q32为常量

        q30 = q30 * (1 - B)
        q11 = (1 - q38 - q30 + q38 * q30) / q43  #q43为常量
        if(T == 30):
            q7 = q2
        else:
            q7 = -(q12 + q11) * T  #q7 

        q12 = q7 / q3  #q3为常量
        #q12 = (q2 - q11) * T / (q3 + T)
        q8 = q4 * q12  #q4为常量
        q21 = 2 * q8
        PD_S = q44 - q55  #q44为常量
        if(PD_S < T0): #T0需要给定
            S = float('inf')
        else:
            S = 1

        q57 = q45 * q49  #q45,q49为常量
        q22 = 2 * (10 * q46 * (1 - 0.9 * q53) + q17 * q55) * S / (q56 + q57)  #q17,q46,q56为常量
        q18 = math.pow(q19 / q22, 2)  #q19为常量
        q20 = 1 - math.pow((1 - q18), q21)
        q9 = q8 * (1 - q20)
        q15 = N1 * q23 + N2 * q24 + N3 * q25  #q23,q24,q25为常量,N1\N2\N3
        q14 = math.pi * q15 * math.pow(q5,2)  #q5为常量
        q10 = q9 * q13  #q13为常量
        PD_q16 = q10 - q6  #q6为常量
        if(PD_q16 < 0):
            q16 = 0
        else:
            q16 = q9 * q13 * q14 / q4  #q4,q13为常量

        q1 = -1 * q16 * T
        T_list.append(T)
        q10_list.append(q10)

    return [T_list,q10_list]



#--------------------------------------蓝方现存兵力水平--------------------------------
#1.蓝方现存兵力q1随时间T_list变化情况
def func1_1(q1,q10,q12,q30):
    BlueForceLevel1 = BlueForceLevelVariesOverTime(q1,q10,q12,q30)
    plt.rcParams["font.sans-serif"]=['SimHei']
    plt.rcParams["axes.unicode_minus"]=False
    print(BlueForceLevel1[0])
    print(BlueForceLevel1[1])

    plt.scatter(BlueForceLevel1[0],BlueForceLevel1[1])
    plt.title("蓝方现存兵力水平")
    plt.xlabel("时间(s)")
    plt.ylabel("蓝方现存兵力")
     
    plt.show()

#2.蓝方现存兵力q1随红方侦察卫星能力q23变化情况
def func1_2(q1,q10,q12,q30):
    BlueForceLevel2 = BlueForceLevelVariesOverQ23(q1,q10,q12,q30)
    plt.rcParams["font.sans-serif"]=['SimHei']
    plt.rcParams["axes.unicode_minus"]=False
    print(BlueForceLevel2[0])
    print(BlueForceLevel2[1])

    plt.scatter(BlueForceLevel2[0],BlueForceLevel2[1])
    plt.title("蓝方现存兵力水平")
    plt.xlabel("红方侦察卫星能力(0-1)")
    plt.ylabel("蓝方现存兵力")
     
    plt.show()

#--------------------------------------红方射前生存弹道导弹数--------------------------------
#红方射前生存弹道导弹数q7随时间T_list变化情况
def func2(q1,q10,q12,q30):
    survivingBallisticMissiles = survivingBallisticMissilesOverTime(q1,q10,q12,q30)
    plt.rcParams["font.sans-serif"]=['SimHei']
    plt.rcParams["axes.unicode_minus"]=False
    print(survivingBallisticMissiles[0])
    print(survivingBallisticMissiles[1])

    plt.scatter(survivingBallisticMissiles[0],survivingBallisticMissiles[1])
    plt.title("红方射前生存弹道导弹数")
    plt.xlabel("时间(s)")
    plt.ylabel("红方射前生存弹道导弹数")
     
    plt.show()

#--------------------------------------红方成爆弹量--------------------------------
#红方成爆弹量q10随时间T_list变化情况
def func3(q1,q10,q12,q30):
    ammunition = ammunitionOverTime(q1,q10,q12,q30)
    plt.rcParams["font.sans-serif"]=['SimHei']
    plt.rcParams["axes.unicode_minus"]=False
    print(ammunition[0])
    print(ammunition[1])

    plt.scatter(ammunition[0],ammunition[1])
    plt.title("红方成爆弹量")
    plt.xlabel("时间(s)")
    plt.ylabel("红方成爆弹量")
     
    plt.show()

#--------------------------------------调用函数运行--------------------------------
func1_1(q1,q10,q12,q30)
func1_2(q1,q10,q12,q30)
func2(q1,q10,q12,q30)
func3(q1,q10,q12,q30)


