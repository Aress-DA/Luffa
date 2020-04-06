# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 16:08:58 2019

@author: anjali.dharmik
"""

from bs4 import BeautifulSoup
import warnings,time
warnings.filterwarnings("ignore", category=FutureWarning)

def page_categories(source):
    category_list = set()
    for div in source.findAll("div"):
        try:
            if "responsive-menus" in div["class"]:
                for a in div.findAll("a"):
                    if ("http://" not in a["href"] ):
                        category_list.add("http://www.7daydaily.com"+a["href"])
                    else:
                        category_list.add(a["href"])
        except:
            pass
            
    return list(category_list)

def find_categories(url,browser):
    try:
        page = browser.get(url)
        time.sleep(5)
        source = BeautifulSoup(page.content)
    except:
        source =""
    return page_categories(source),browser
    
