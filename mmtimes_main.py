# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 12:44:59 2019

@author: anjali.dharmik
"""

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

from article_db import upload_article
from mmtimes_categories import find_categories
from mmtimes_articles import find_articles
#from mmtimes_data import articlesourcefun
from bs4 import BeautifulSoup

def mmtimes_main(browser,url,cursor,db):
#    print("started---------find_categories")
    category_list,browser = find_categories(url,browser)
    
    for category_url in category_list:
        try:
            page = browser.get(category_url)
            source = BeautifulSoup(page.content)
        except:
            source =""
        if source!="":
            article_lst = source.findAll("div",attrs={"class": "views-row"})
            for article in article_lst:
                try:
                    img_link = source.find("div",attrs={"class": "latest-news-top"}).find("img")["src"]
                except:
                    img_link =""
                try:
                    article_title = source.find("div",attrs={"class": "news-title"}).text.strip()
                    article_url = url+source.find("div",attrs={"class": "news-title"}).find("a")["href"]
                except:
                    article_title,article_url ="",""
                try:
                    category = source.find("span",attrs={"class": "news-category"}).text.strip()
                except:
                    category =""
                try:
                    date_time = source.find("span",attrs={"class": "news-date"}).text.strip()
                except:
                    date_time =""
        #            print(article_url)
                try:
                    page = browser.get(article_url)
                    source = BeautifulSoup(page.content)
                    summary = "\n".join([p.text.strip() for p in source.find("div",attrs={"class": "field-item"}).findAll("p")])
                    author = source.find("span",attrs={"class": "news-author"}).text.strip()
                except:
                    summary =""
                    author =""
                topics =""
                upload_article(article_title,date_time,author,summary,article_url,url,img_link,cursor,db,category,topics)
                