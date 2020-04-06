# -*- coding: utf-8 -*-
"""
Created on Thu May 30 20:34:46 2019

@author: anjali.dharmik
"""
from bs4 import BeautifulSoup

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

def data_collection_and_tagging1(source):
    _list = set()
    for div in source.findAll("div"):
        try:
            if "articles" in div["id"]:
                for a in div.findAll("a"):
                    if ".html" in a["href"]:
                        _list.add(a["href"])
        except:
            pass
    post_link_lst = list(_list)
    return post_link_lst

def next_page_fun(source,category_url):
    next_page = category_url
    for link in source.findAll("link"):
        try:
            if "next" in link["rel"]:
                next_page = link["href"]
        except:
            next_page = category_url
    return next_page

def find_articles(category_url,browser):
    total_lst = []
    try:
        page = browser.get(category_url)
        source = BeautifulSoup(page.content)
    
        for i in range(2):
            curr_page = category_url+"/page/"+str(i)
            page = browser.get(curr_page)
            source = BeautifulSoup(page.content)
            post_link_lst = data_collection_and_tagging1(source)
            total_lst.extend(post_link_lst)
    except:
        pass
#        print(category_url)

    return list(set(total_lst)),browser
