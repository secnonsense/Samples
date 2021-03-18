from bs4 import BeautifulSoup
import requests

r=requests.get("http://www.ipchicken.com")    # request some url
data = r.text
soup = BeautifulSoup(data, features="html.parser")
for link in soup.find_all('a'):   # looks for "a" tags aka hyperlinks
    print(link.get('href'))       # pulls the href from the html
#    print(link)

#print(soup.prettify)
#print(soup.get_text())
#print(soup.title)
#print(soup.title.name)
#print(soup.title.string)
#print(soup.title.parent.name)
#print(soup.p)                    # paragraph
#print(soup.a)                    # hrefs 
#print(soup.p['class'])
#print(soup.b)                    # bold
#print(soup.b.string)              # comments
