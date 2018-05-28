from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

url = 'http://quotes.yourdictionary.com/theme/marriage/'
response = urlopen(url).read()
soup = BeautifulSoup(response)

fivequotes = soup.findAll("p", attrs={"class": "quoteContent"}, limit=5)
for i in fivequotes:
    print(i.string + "\n")
