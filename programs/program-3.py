import sys
import os
import csv
from collections import Counter
from collections import OrderedDict

path = os.path.expanduser("~/Desktop/spring-2015/COMM290/index/sankei.csv")

ls = []
c = csv.reader(open(path,"r",encoding='utf-8'))
for row in c:    
    if(row[3].startswith("Year")!= True):
    	date = row[3]+row[4]+row[5]
    	ls.append(date)
counter = Counter(ls)
od = OrderedDict(sorted(dict(counter).items()))

header = ["Source", "Date", "Count"]
c = csv.writer(open("distribution_s.csv", "w", encoding='utf-8'))
c.writerow(header)

for i, v in od.items():
	c.writerow(["Sankei", i, v])
