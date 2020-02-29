from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from urllib.request import urlopen
from xml.etree.ElementTree import parse

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_rss_feed():
    links = []
    var_url = urlopen('https://www.nrablog.com/rss')
    xmldoc = parse(var_url)
    for item in xmldoc.iterfind('.//link'):
        print(item.text)
        slashes = item.text.split('/');
        if (len(slashes) > 4) : links.append(item.text)

    # Return results
    return links

links = scrape_rss_feed()
print(len(links))