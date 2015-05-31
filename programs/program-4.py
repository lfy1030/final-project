import sys
import os
import csv
import requests
from bs4 import BeautifulSoup

appid = "dj0zaiZpPWtPR0lJWW9wY293SSZzPWNvbnN1bWVyc2VjcmV0Jng9YWM-"  
query_url = "http://jlp.yahooapis.jp/MAService/V1/parse"

path = os.path.expanduser("~/Desktop/spring-2015/COMM290/text")
filenames = os.listdir(path)

theDictionary = {}

for fn in filenames:
	#Var 1
	#if(fn.startswith('s')):
		pathname = os.path.expanduser("~/Desktop/spring-2015/COMM290/text/" + fn)
		with open (pathname, "r", encoding='utf-8') as f:
			sentence = f.read()
			soup = BeautifulSoup(requests.get(query_url, params={'appid': appid, 'results':'uniq', 'uniq_filter': "9|10", 'sentence':sentence}).text)
		f.close()
		words = soup.findAll("word")
		for w in words:
			key = w.surface.text
			count = w.count.text
			pos = w.pos.text
			print("Word: %s, count: %s, pos: %s" % (key, count, pos))
			if key in theDictionary:
				buf = theDictionary[key]
				buf[0] = str(int(buf[0])+int(count))
			else:
				buf = [count, pos]
			theDictionary.update({key:buf})
		print("Processed File: %s" % fn)

header = ["Source", "Word", "Count", "Type"]
#Var 2
c = csv.writer(open("words_all.csv", "w", encoding='utf-8'))
c.writerow(header)
for k, v in theDictionary.items():
	#Var 3
	c.writerow(["All", k, v[0], v[1]])