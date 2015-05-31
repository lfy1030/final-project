# Japanese News Parsing Suite 

## This is a bunch of programs that I'm using to parse news articles and visualize data for my M.A. thesis

### Mini-Program 0: Html Counter

A preliminary program that counts the number of files from each source because I'm too lazy to do it by hand. 

### Mini-Program 1: Html Parser 1-4

Since there are four difference sources for each of the four newspapers I'm examining, there are four mini-programs used to parse out information from the raw html files downloaded containing the news articles. 

There are two major outputs: 

1. A csv containing the following for each html file
	* Newspaper Source
	* Title of article 
	* Date article was published
	* Article ID (the original html filename)
2. A txt file with the same filename as the original html file containing _only_ the main text body of the news article  

### Mini-Program 2: Article Lengths

Counts the article lengths, get the number of entries, mean and standard deviation. 
Output into csv.

### Mini-Program 3: Article Count by Date

Output dates of articles and count in csv

### Mini-Program 4: Analyze Words

Uses the [Yahoo! Japanese Tokenizer API](http://developer.yahoo.co.jp/webapi/jlp/ma/v1/parse.html)
Find most frequent words in each of the articles by source and total
Output into csv.

### Mini-Program 5: Sets

Using the sets module to find words that are unique to certain papers but not the others. 
Print into console