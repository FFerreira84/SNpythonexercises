from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

url = 'http://quotes.yourdictionary.com/theme/marriage/'
response = urlopen(url).read()
soup = BeautifulSoup(response)
# quotediv = soup.find("div", attrs={"class": "quoteGridContent"})

# print soup

test = soup.findAll("p", attrs={"class": "quoteContent"}, limit=5)
print test.find("p")

# for i in range(1):
#     quote = soup.find_all("p", attrs={"class": "quoteContent"}).string
#     print quote




# for link in soup.findAll("a"):
#     if link.string == "See full profile":
#         person_url = 'https://scrapebook22.appspot.com' + link['href']
#         person_html = urlopen(person_url).read()
#         person_soup = BeautifulSoup(person_html)
#         email = person_soup.find("span", attrs={"class": "email"}).string
#         name1 = person_soup.find("div", attrs={"class": "col-md-8"})
#         name = name1.h1.string
#         city = person_soup.find(text="City: ").parent.span.string