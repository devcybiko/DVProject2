from bs4 import BeautifulSoup as bs
import requests
import time
from urllib.request import urlopen
from xml.etree.ElementTree import parse

def scrapeURL(url):
    res = requests.get(url)
    html_page = res.content
    soup = bs(html_page, 'html.parser')
    text = soup.find_all('div', {'class': 'body-content'})
    return text


def scrape_rss_feed(url):
    links = []
    var_url = urlopen(url)
    xmldoc = parse(var_url)
    for item in xmldoc.iterfind('.//link'):
        print(item.text)
        slashes = item.text.split('/');
        if (len(slashes) > 4) : links.append(item.text)

    # Return results
    return links

links = scrape_rss_feed('https://www.nrablog.com/rss')
print(len(links))
text = scrapeURL(links[0])
print(text)