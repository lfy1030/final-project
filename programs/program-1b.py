import sys
import os
from bs4 import BeautifulSoup
import csv

#PROGRAM VERSION MAINICHI
path = os.path.expanduser("~/Desktop/spring-2015/COMM290/raw-html")
#list containing all the files in this directory 
filenames = os.listdir(path)
#opening the csv for writing
header = ["Article ID","Source","Title","Year","Date","Time"]
c = csv.writer(open("mainichi.csv", "w", encoding='utf-8'))
c.writerow(header)

for fn in filenames:
	if(fn.startswith("m")):
		path = os.path.expanduser("~/Desktop/spring-2015/COMM290/raw-html/" + fn)
		soup = BeautifulSoup(open(path, "r", encoding='utf-8'))
		c_list = []

		#Get the filename ID
		article_id = fn[0:len(fn)-5]
		print(article_id)
		c_list.append(article_id)

		#Set the source
		source = "Mainichi"
		c_list.append(source)

		#Get the title as a string
		title = soup.find_all("title")[0].text
		c_list.append(title[0:len(title)-7])
	
		#Get the date as ???
		date = str(soup.find_all("meta", attrs={"name": "firstcreate"}))
		year = date[16:20]
		month = date[21:23]
		day = date[24:26]
		c_list.extend([year, month, day])

		#add everything to the csv
		c.writerow(c_list)

		#Get the main text body
		buf = soup.find_all("div", attrs={"class": "NewsBody clr"})
		textfile_name = article_id + ".txt"
		textfile = open(textfile_name, "w", encoding='utf-8')
		for b in buf:
			p = b.find_all("p")
			for p_part in p:
				print(p_part.text)
				textfile.write(p_part.text)
		textfile.close()

		