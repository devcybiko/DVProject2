from splinter import Browser
from bs4 import BeautifulSoup as bs
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    # Visit visitcostarica.herokuapp.com
    url = "https://www.nrablog.com/rss"
    browser.visit(url)

    #time.sleep(1)

    # Scrape page into Soup
    xml = browser.html
    print(xml)
    soup = bs(xml, "lxml")

    # Get the average temps
    links = soup.find_all('link')
    print([ link.text for link in links ])


    # Close the browser after scraping
    browser.quit()

    # Return results
    return links

scrape_info()