import sys
import os
import numpy
import csv

path = os.path.expanduser("~/Desktop/spring-2015/COMM290/text")
#list containing all the files in this directory 
filenames = os.listdir(path)

count_asahi = []
count_sankei = []
count_mainichi = []
count_nikkei = []

#opening the csv for writing
header = ["Source", "Mean", "N", "SD"]
c = csv.writer(open("lengths.csv", "w", encoding='utf-8'))
c.writerow(header)

for fn in filenames:
	pathname = path + "/" + fn
	with open(pathname, "r", encoding='utf-8') as f:
		data = f.read().replace('\n', if(fn.startswith('a')):'')
		if(fn.startswith('a')):
			count_asahi.append(len(data))
		if(fn.startswith('s')):
			count_sankei.append(len(data))
		if(fn.startswith('m')):
			count_mainichi.append(len(data))
		if(fn.startswith('n')):
			count_nikkei.append(len(data))
		f.close();
c1 = ["Nikkei", numpy.mean(count_nikkei), len(count_nikkei), numpy.std(count_nikkei)]
c2 = ["Sankei", numpy.mean(count_sankei), len(count_sankei), numpy.std(count_sankei)]
c3 = ["Mainichi", numpy.mean(count_mainichi), len(count_mainichi), numpy.std(count_mainichi)]
c4 = ["Asahi", numpy.mean(count_asahi), len(count_asahi), numpy.std(count_asahi)]
c.writerow(c1)
c.writerow(c2)
c.writerow(c3)
c.writerow(c4)





