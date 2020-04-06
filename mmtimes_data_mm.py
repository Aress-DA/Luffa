# -*- coding: utf-8 -*-
"""
Created on Thu May 30 23:46:09 2019

@author: anjali.dharmik
"""

from selenium import webdriver
from bs4 import BeautifulSoup
from dateutil import parser
import re
from upload_data_mysql import uploaddata_mysql
from article_type import idf

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

def article_details(source):
    news_title_lst,img_link,date_time,author,summary ="",'','','',''
    try:
        news_title_lst = "|".join(source.title.text.split("|")[0:-1])
    except:
        pass
    for div in source.findAll("div"):
        try:
            if "view-footer" in div["class"]: 
                for div1 in div.findAll("div"):
                    if "news-info" in div1["class"]:
                        for span in div1.findAll("span"):
                            if "news-date" in span["class"]:
                                date_time = span.text
            if "pre-author" in div["class"]:
                author = div.text
            if "news-detail-bar" in div["class"]: 
                for div1 in div.findAll("div"):
                    if "news-info" in div1["class"]:
                        for span in div1.findAll("span"):
                            if "news-date" in span["class"]:
                                date_time = span.text
                            if "news-author" in span["class"]:
                                author =span.text
            if "field-name-field-news-image" in div["class"]:
                for _img in div.findAll("img"):
                    img_link += _img["src"]+"\n"
            if "node-content" in div["class"]:
#                for p in div.findAll("p"):
                summary  = div.text
        except:
            pass
    news_title = news_title_lst
    summary = BeautifulSoup(summary, "lxml").text
    summary = " ".join(summary.split())
    return news_title,date_time,author.strip(),summary.strip(),img_link.strip()

def articlesourcefun(articles_lst,browser):
    url ="https://myanmar.mmtimes.com"
    not_processed = []
    for article_url in articles_lst:
        if "?page" not in article_url:
            try:
            
                page = browser.get(article_url)
                source = BeautifulSoup(page.content)
                entry_name,date_time,author,summary,img_link = article_details(source)
            
                uploaddata_mysql(article_url,entry_name,date_time,author,summary,img_link,url)
#                count+=1
#                print(count)
            except:
                not_processed.append(article_url)
