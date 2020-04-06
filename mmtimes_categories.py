# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 17:55:04 2019

@author: admin
"""

from bs4 import BeautifulSoup

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

def page_categories(source,url):
    category_list = set()
    if source!="":
        for ul in source.findAll("ul"):
            if "menu" in ul["class"]:
                for a in ul.findAll("a"):                    
                    category_list.add(url+a["href"])
            
    return list(category_list)

def find_categories(url,browser):
    try:
        page = browser.get(url)
        source = BeautifulSoup(page.content)
    except:
        source=""
    return page_categories(source,url),browser
    
