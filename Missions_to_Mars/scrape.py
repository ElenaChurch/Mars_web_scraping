from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

executable_path = {'executable_path': ChromeDriverManager().install()}

def scrape():
    data = {}
    browser = Browser('chrome', **executable_path, headless=True)
    title, paragraph = news(browser)
    data['title'] = title
    data['paragraph'] = paragraph
    data['image'] = image(browser)
    data['facts'] = facts()
    data['hemispheres'] = hemis(browser)
    return data

def news(browser):
    browser.visit('https://redplanetscience.com/')
    title = browser.find_by_css('div.content_title').text 
    paragraph = browser.find_by_css('div.article_teaser_body').text
    return title, paragraph

def image(browser):
    browser.visit('https://spaceimages-mars.com/')
    browser.find_by_tag('button')[1].click()
    return browser.find_by_css('img.fancybox-image')['src']

def facts():
    return pd.read_html('https://galaxyfacts-mars.com/',index_col=0,
    header=0)[0].to_html(classes='table table-striped')

def hemis(browser):
    browser.visit('https://marshemispheres.com/')

    hemispheres = []
    for i in range(4):
        hemisphere = {}
        hemisphere['title'] = browser.find_by_css('a.itemLink h3')[i].text
        browser.find_by_css('a.itemLink h3')[i].click()
        hemisphere['url'] = browser.find_by_text('Sample')['href']
        hemispheres.append(hemisphere)
        browser.back()
    browser.quit()
    return hemispheres

