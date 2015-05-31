import sys
import os
from bs4 import BeautifulSoup
import csv

#PROGRAM VERSION ASAHI
path = os.path.expanduser("~/Desktop/spring-2015/COMM290/raw-html")
#list containing all the files in this directory 
filenames = os.listdir(path)
#opening the csv for writing
header = ["Article ID","Source","Title","Year","Date","Time"]
c = csv.writer(open("asahi.csv", "w", encoding='utf-8'))
c.writerow(header)

for fn in filenames:
	if(fn.startswith("a")):
		path = os.path.expanduser("~/Desktop/spring-2015/COMM290/raw-html/" + fn)
		soup = BeautifulSoup(open(path, "r", encoding='utf-8'))
		c_list = []

		#Get the filename ID
		article_id = fn[0:len(fn)-5]
		print(article_id)
		c_list.append(article_id)

		#Set the source
		source = "Asahi"
		c_list.append(source)

		#Get the title as a string
		title = str(soup.find_all("meta", attrs={"name":"TITLE"}))
		c_list.append(title[16:len(title)-17])
	
		#Get the date as ???
		date = str(soup.find_all("meta", attrs={"name": "RELEASE_DATE"}))
		year = date[16:20]
		month = date[21:23]
		day = date[24:26]
		c_list.extend([year, month, day])
		#print("%s %s %s" % (year, month, day))

		#add everything to the csv
		c.writerow(c_list)

		#Get the main text body
		buf = soup.find_all("div", attrs={"class": "ArticleText"})
		textfile_name = article_id + ".txt"
		textfile = open(textfile_name, "w", encoding='utf-8')
		for b in buf:
			p = b.find_all("p")
			for p_part in p:
				print(p_part.text)
				textfile.write(p_part.text)
		textfile.close()

		