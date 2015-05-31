import sys
import os
import csv

path = os.path.expanduser("~/Desktop/spring-2015/COMM290/csvs/words_all.csv")



cr = csv.reader(open(path,"r", encoding='utf-8'))
buf_a = []
buf_m = []
buf_n = []
buf_s = []

for row in cr:
	if(len(row)>0):
		if(row[0] == "Asahi"): 
			buf_a.append(row[1])
		if(row[0] == "Mainichi"):
			buf_m.append(row[1])
		if(row[0] == "Nikkei"):
			buf_n.append(row[1])
		if(row[0] == "Sankei"):
			buf_s.append(row[1])

asahi = set(buf_a)
mainichi = set(buf_m)
nikkei = set(buf_n)
sankei = set(buf_s)

a = asahi-mainichi-nikkei-sankei
m = mainichi-asahi-nikkei-sankei
n = nikkei-asahi-mainichi-sankei
s = sankei-mainichi-nikkei-asahi

header = ["Source", "Word"]
c = csv.writer(open("unique_words.csv", "w", encoding='utf-8'))
c.writerow(header)
for i in a:
	c.writerow(["Asahi", i])
for i in m:
	c.writerow(["Mainichi", i])
for i in n:
	c.writerow(["Nikkei", i])
for i in s:
	c.writerow(["Sankei", i])