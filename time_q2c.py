# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 14:33:47 2018

@author: Administrator
"""

import matplotlib.pyplot as plt
import os,re
listfiles = os.listdir(os.getcwd())
listfiles.sort()

for t in listfiles:
	if re.search("q2c.dat$",t) :
		source_address=t
		break

x_values=[]
y_values=[]

#打开源trace文件、修改后目标存储文件
trace_f1 = open(source_address,'r')

print("begin")

#逐行读取，放入元素为5个的列表中，将第一个时间time*1000000
for line in trace_f1:
    list1 = line.split()
    list1[0] = (float)(list1[0])
    list1[1] = (float)(list1[1])
    list1[1] = list1[1]*1000
    if list1[1] > 6000:
    	continue
    x_values.append(list1[0])
    y_values.append(list1[1])    
    
#关闭文件
trace_f1.close()

print(max(y_values))
'''
scatter() 
x:横坐标 y:纵坐标 s:点的尺寸
'''
plt.scatter(x_values, y_values, c='blue', s=5, label="IO latency")
 
# 设置图表标题并给坐标轴加上标签
plt.title('Request Response Time', fontsize=14)
plt.xlabel('time(s)', fontsize=14)
plt.ylabel('response time(ms)', fontsize=14)
plt.legend(loc='best')
 
# 设置刻度标记的大小
#plt.tick_params(axis='both', which='major', labelsize=14)
 
# 设置每个坐标轴的取值范围
#plt.axis([0, 1100, 0, 1100000])
#plt.show()
savename='time_q2c.jpg'
plt.savefig(savename)

print("end")       
