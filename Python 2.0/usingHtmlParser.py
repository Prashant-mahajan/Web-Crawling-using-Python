#The output of this file has been saved in googleHtmlParser

import HTMLParser
import urllib

urlText=[]

fileName="googleHtmlParser.txt" #this is the filename where the code will be saved.

#Define HTML Parse
class parseText(HTMLParser.HTMLParser):
	def handle_data(self,data):
		if data!='\n':
			urlText.append(data)

#Create instance of HTML parser
lParser=parseText()

target=open(fileName,'a')

thisurl="https://www.google.com"
#Feed HTML file into parse
lParser.feed(urllib.urlopen(thisurl).read())
lParser.close()
for item in urlText:
	target.write(item)
	print (item)


target.close()