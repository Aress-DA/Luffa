# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 18:34:24 2019

@author: anjali.dharmik
"""

from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
from article_db import upload_article
from dateutil import parser

def article_details(source1):        
    news_title,img_link,news_date,date_time,author,summary ='','','','','',''
    for div in source1.findAll("div"):
        try:
            for h1  in div.findAll("h1"):
                if "title" in h1["class"]:
                    news_title = h1.text
            if "story-detail-date" in div["class"]:
                date_time =div.text
            if "story-photo-wrapper" in div["class"]:
                for img in div.findAll("img"):
                    img_link += img["src"]+"\n"
            if "field-type-text-with-summary" in div["class"]:
                for p in div.findAll("p"):
                    summary += p.text+"\n"
            if "field-name-field-author" in div["class"]:
                author = div.text
        except:
            pass
    
    if news_title !="":
        entry_name=news_date+" "+news_title
    else:
        entry_name =news_title
#    print(entry_name,date_time,author,summary,img_link)
    return entry_name,date_time,author,summary,img_link


def articlesourcefun(articles_lst,browser,category,cursor,db):
    url = "http://www.7daydaily.com/"
    not_processed =[]
    count = 0
    for article_url in articles_lst:
        count+=1
        try:
            page = browser.get(article_url)
            source = BeautifulSoup(page.content)
            entry_name,date_time,author,summary,img_link = article_details(source)
            topics = ""
            upload_article(entry_name,date_time,author,summary,article_url,url,img_link,cursor,db,category,topics)                

        except:
            not_processed.append(article_url)
