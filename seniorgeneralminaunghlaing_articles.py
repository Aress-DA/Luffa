# -*- coding: utf-8 -*-
"""
Created on Fri May 31 12:15:30 2019

@author: admin
"""

from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

def article_url_fun(article):
    for header in article.findAll("header"):
        for a in header.findAll("a"):
            if ("https://vk.com" not in str(a["href"]))  and ("https://twitter.com"  not in str(a["href"]))\
               and  ("https://plus.google.com"  not in str(a["href"]))  and  ("https://www.linkedin.com"  not in str(a["href"]))\
                and ("/#"  not in str(a["href"]))  and ("www.facebook.com"  not in str(a["href"]))\
                and ("https://www.seniorgeneralminaunghlaing.com.mm/en/Home/news/" not in str(a["href"]))\
                and (".jpg" not in str(a["href"])) and ("seniorgeneralminaunghlaing.com.mm/en/" in str(a["href"])):
                    print(a["href"])
                    return a["href"]
                     
def data_collection_and_tagging(source):
    _list = set()
    for div in source.findAll("div"):
        try:
            if "main-content-section" in div["id"]:
                for article in div.findAll("article"): 
                    _list.add(article)
                    print(article_url_fun(article))
        except:
            pass
    post_link_lst = list(_list)
    print(len(post_link_lst))
    return post_link_lst

def find_articles(url,browser):
    page = browser.get(url)
    source = BeautifulSoup(page.content)
    pages = 94
    post_link_lst =[]
    for i in range(int(pages)+1):
        sub_url = "https://www.seniorgeneralminaunghlaing.com.mm/en/Home/news/page/"+str(i) 
        page = browser.get(sub_url)
        source = BeautifulSoup(page.content)
        articles_lst = data_collection_and_tagging(source)
        for article in articles_lst:
            post_link_lst.append(article_url_fun(article))
    f = open("senior_articles.txt","w",encoding="utf-8")
    f.write(str(post_link_lst))
    f.close()
    return list(set(post_link_lst)),browser
    