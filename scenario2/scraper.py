from bs4 import BeautifulSoup as bs
import requests
import time
from urllib.request import urlopen
from xml.etree.ElementTree import parse

def scrapeURL(url):
    res = requests.get(url)
    html_page = res.content
    soup = bs(html_page, 'html.parser')
    text = soup.find('div', {'class': 'body-content'})
    return text.text if text else ''


def scrape_rss_feed(url):
    links = []
    var_url = urlopen(url)
    xmldoc = parse(var_url)
    parent_map = {c:p for p in xmldoc.iter() for c in p}
    for item in xmldoc.iterfind('.//link'):
        print(item.text)
        div = parent_map
        print(div)
        byline = div.find('.//span')
        print(byline)

        slashes = item.text.split('/')
        if (len(slashes) > 4) : links.append(item.text)

    # Return results
    return links

links = scrape_rss_feed('https://www.nrablog.com/rss')
print(len(links))
for link in links:
    text = scrapeURL(link)
    print(text)
    print('-----------')
    break