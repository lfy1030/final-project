import sys
import os

path = os.path.expanduser("~/Desktop/spring-2015/COMM290/raw-html")
#list containing all the files in this directory 
filenames = os.listdir(path)

count_asahi = 0
count_sankei = 0
count_mainichi = 0
count_nikkei = 0

for fn in filenames:
	if(fn.startswith('a_1407')):

print("Asahi : %s" % count_asahi) 
print("Sankei : %s" % count_sankei) 
print("Mainichi : %s" % count_mainichi) 
print("Nikkei : %s" % count_nikkei) 
total = count_asahi+count_nikkei+count_mainichi+count_sankei
print("Total: %s" % total)


