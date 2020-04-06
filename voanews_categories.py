# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 11:48:39 2019

@author: anjali.dharmik
"""

from browser_setting import open_browser
from bs4 import BeautifulSoup

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

def page_categories(source):
    category_list = set()
    if source!="":
        for div in source.findAll("div"):
            try:
                if "menu" in div["class"]:
                    for a in div.findAll("a"):
                        if (".html" in a["href"]) and (a["href"] not in ["http://java.oms.apps.opera.com/en_us/voa_news_for_java_phones.html?dm=1&multi=1&set_lang=en","http://m.burmese.voanews.com/rss.html?tab=Podcast","http://m.burmese.voanews.com/rss.html?tab=Rss","/login.html","/p/3830.html","/subscribe.html","http://m.burmese.voanews.com/subscribe.html"]):
                            category_list.add("https://burmese.voanews.com"+a["href"])
            except:
                pass
            
    return list(category_list)

def find_categories(url):
    browser = open_browser()
    try:
        page = browser.get(url)
        source = BeautifulSoup(page.content)
    except:
        source =""
    return page_categories(source),browser
    
