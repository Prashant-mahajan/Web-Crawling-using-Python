#This code is python 2.0 compatible
# for python3: http://stackoverflow.com/questions/3969726/attributeerror-module-object-has-no-attribute-urlopen

#This program uses URL libraries of python to crawl and fetch the HTML code of the page.
#You may try changing the value of the url below in the code.

#The repository contains a file named "google.html", where the source code of google has been retracted using this snippet.
#Happy Coding! 
import urllib

#Creating a local file to store the output in the form of HTML.
filename='google.html'
target=open(filename,'w')

thisurl="http://www.google.com"
handle=urllib.urlopen(thisurl)
html_gunk=handle.read()

target.write(html_gunk);
target.close()