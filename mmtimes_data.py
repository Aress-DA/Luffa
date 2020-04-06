# -*- coding: utf-8 -*-
"""
Created on Thu May 30 23:46:09 2019

@author: anjali.dharmik
"""

from selenium import webdriver
from bs4 import BeautifulSoup
from dateutil import parser
from upload_data_mysql import uploaddata_mysql
from article_type import idf

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

def article_details(source):
    news_title_lst,img_link,news_date,date_time,author,summary ="",'','','','',''
    news_title_lst = "|".join(source.title.text.split("|")[0:-1])
    for div in source.findAll("div"):
        try:
            if "news-detail-bar" in div["class"]: 
                for div1 in div.findAll("div"):
                    if "news-info" in div1["class"]:
                        for span in div1.findAll("span"):
                            if "news-date" in span["class"]:
                                date_time = parser.parse(span.text)
                                news_date =  date_time.strftime("%y%m%d")
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
    entry_name=news_date+" "+news_title
    return entry_name,date_time,author,summary,img_link

def articlesourcefun(articles_lst,browser):
    url ="http://www.mmtimes.com/04jun"
    not_processed = []
    count =0
    for article_url in articles_lst:
        if "?page" not in article_url:
            try:
            
                page = browser.get(article_url)
                source = BeautifulSoup(page.content)
                entry_name,date_time,author,summary,img_link = article_details(source)
                if summary !="":
                    article_type = idf(summary)
                else:
                    article_type = 'News article'
                uploaddata_mysql(article_url,entry_name,date_time,author,summary,article_url+"\n"+img_link,article_type,url)
                count+=1
            except:
                not_processed.append(article_url)
