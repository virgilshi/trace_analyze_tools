# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 19:25:36 2018

@author: Administrator
"""

import matplotlib.pyplot as plt
import os,re

listfiles = os.listdir(os.getcwd())
listfiles.sort()

source_address=[]
for t in listfiles:
	if re.search("[r]\.dat$",t) :
		source_address.append(t)

print("begin")
for t in source_address :
	dataset=[]
	trace_f0 = open(t,'r')
	#逐行读取，放入元素为5个的列表中，将第一个时间time*1000000
	for line in trace_f0:
	    list1 = line.split()
	    list1[0] = (float)(list1[0])
	    list1[1] = (int)(list1[1])
	    list1[2] = (int)(list1[2])
	    
	    dataset.append(list1[2]-list1[1])
	    
	#关闭文件
	trace_f0.close()
	more_than_1024_cnt=0
	for i in range(len(dataset)) :
		if 1024 < dataset[i] :
			more_than_1024_cnt=more_than_1024_cnt+1
	
	more_rate=more_than_1024_cnt/len(dataset)
	dataset.sort()

	plotDataset = [[],[]]
	count = len(dataset)
	#count1=0
	for i in range(count):
	    plotDataset[0].append(dataset[i])
	    plotDataset[1].append(((float)(i+1))/count)
	#    if dataset[i]==1024:
	#        count1=count1+1
	plotDataset[0].append(300)
	plotDataset[1].append(1)

	if "r.dat" in t:
		labelname="Read"
		colorname="red"
	else :
		labelname="Write"
		colorname="green"
	plt.plot(plotDataset[0], plotDataset[1], '-', linewidth=2, label=labelname,color=colorname)
	plt.annotate('(%d, 1)' % max(dataset), xy=(max(dataset), 1), xytext=(max(dataset)-50, 0.8), arrowprops=dict(facecolor=colorname, shrink=0.1, width=0.5, headwidth=5))
	if more_than_1024_cnt != 0:
		plt.annotate('>1024 : %.6f%%' % (more_rate*100), xy=(1024, 1), xytext=(1024+200, 0.8), arrowprops=dict(facecolor=colorname, shrink=0.1, width=0.5, headwidth=5))
plt.title('Request Size CDF', fontsize=14)
plt.xlabel('size(sectors)', fontsize=14)
plt.ylabel('CDF', fontsize=14)
plt.legend(loc='best')

#print(count, count1)
savename='size_cdf.jpg'
plt.savefig(savename)

print("end")
