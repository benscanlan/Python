#textarea
#html/sep9.html
#pip3 install beautifulsoup4
from urllib.request import urlopen
from bs4 import BeautifulSoup
#html = urlopen("/Users/benscanlan/Downloads/edge1.html") #web
html = open("html/sep9.html")  #local
bsObj = BeautifulSoup(html.read(),'html.parser')
print(bsObj.h1)
#findAll(tag, attributes, recursive, text, limit, keywords)
#find(tag, attributes, recursive, text, keywords)
#block--unpublished ts-layout__block ts-layout__block--accordion
test= bsObj.findAll("textarea")
print(test)


