# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 16:30:51 2019

@author: anjali.dharmik
"""

from bs4 import BeautifulSoup

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

def page_count(source):
    a_list = []
    pages =[1]
    for a in source.findAll("a"):
        try:
            if "page" in str(a["href"]):
                a_list.extend(int(str(a["href"]).split("page=")[-1]))
        except:
            pass
    pages = max(a_list)

    return pages

def data_collection_and_tagging(source):
    _list,_list1 = set(),[]
    for div in source.findAll("div"):
        try:
            if "story-list" in div["class"]:
                for div1 in div.findAll("div"):
                    if "taxonomy_title" in div1["class"]:
                        for a in div1.findAll("a"):
                            if "http://" not in a["href"]:
                                _list.add("http://www.7daydaily.com"+a["href"])
                                _list1.append("http://www.7daydaily.com"+a["href"])
                            else:
                                _list.add(a["href"])
                                _list1.append(a["href"])
        except:
            pass
    post_link_lst = list(_list)
    return post_link_lst,_list1

def find_articles(url,browser):
    post_link_lst,post_link_lst1 = [],[]
#    for url in category_url:
    try:
        page = browser.get(url)
        source = BeautifulSoup(page.content)
    except:
        source =""
    if source !="":
        pages = 2#page_count(source)
        for i in range(int(pages)+1):
            suburl =url+"?page=" +str(i)
            try:
                page = browser.get(suburl)
                source = BeautifulSoup(page.content)
            except:
                source =""
            if source !="":
                _list,_list1 = data_collection_and_tagging(source)
                post_link_lst.extend(_list)
                post_link_lst1.extend(_list1)
    return list(set(post_link_lst)),browser