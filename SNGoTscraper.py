from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

url = 'https://en.wikipedia.org/wiki/Game_of_Thrones'
response = urlopen(url).read()
soup = BeautifulSoup(response)
seasontable = soup.find("table", attrs={"class": "wikitable plainrowheaders"})
total = 0

for link in seasontable.findAll("a"):
    if "Season " in link.text:
        season_url = "https://en.wikipedia.org" + link['href']
        season_html = urlopen(season_url).read()
        season_soup = BeautifulSoup(season_html)
        table_soup = season_soup.find("table", attrs={"class": "wikitable plainrowheaders wikiepisodetable"})
        if "Season 8" not in link.text:
            for sup in table_soup.findAll("sup"):
                viewers_soup = sup.previousSibling
                total += float(viewers_soup)

print "Game of Thrones has had a total of " + str(total) + " million viewers."
