# -*- coding: utf-8 -*-
"""
Created on Thu May 30 23:02:12 2019

@author: anjali.dharmik
"""
from bs4 import BeautifulSoup

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

def page_count(source):
    a_list = []
    pages ="1"
    for a in source.findAll("a"):
        try:
            if "page" in str(a["href"]):
                a_list.append(int(str(a["href"]).split("page=")[-1]))
        except:
            pass
    try:
        pages = max(a_list)
    except:
        pass
    return pages

def data_collection_and_tagging(source,url):
    _list = set()
    for div in source.findAll("div"):
        try:
            if "region-two-66-33-first" in div["class"]:
                for div1 in div.findAll("div"):
                    for a in div1.findAll("a"):
                        if ".html" in a["href"] and "www.mmtimes.com" not in a["href"]:
                            _list.add("https://myanmar.mmtimes.com"+a["href"])
        except:
            pass
    post_link_lst = list(_list)
    return post_link_lst

def find_articles(category_list,browser):
    post_link_lst = []
    for category_url in category_list:
        try:
            page = browser.get(category_url)
            source = BeautifulSoup(page.content)
        except:
            source =""
        if source !="":
            pages = 0#page_count(source)
            for i in range(int(pages)+1):
                print("page_number = ",i)
                suburl =category_url+"?page=" +str(i)
                try:
                    page = browser.get(suburl)
                    source = BeautifulSoup(page.content)
                except:
                    source =""
                if source !="":
                    post_link_lst.extend(data_collection_and_tagging(source,category_url))
    return list(set(post_link_lst)),browser