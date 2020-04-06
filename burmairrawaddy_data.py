# -*- coding: utf-8 -*-
"""
Created on Thu May 30 20:43:32 2019

@author: anjali.dharmik
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
from article_db import upload_article
import pandas as pd
from dateutil import parser

def articlesourcefun(articles_lst,browser,category,cursor,db):
    url = "https://burma.irrawaddy.com/"
    for article_url in articles_lst:
        try:
            page = browser.get(article_url)
            source = BeautifulSoup(page.content)
        except:
            source =""
        if source!="":
            article = articlefun(source)
            entry_name,date_time,author,summary,img_link = article_details(article)
            topics = source.find("p",attrs={"class","article-tags"}).text.strip()
            upload_article(entry_name,date_time,author,summary,article_url,url,img_link,cursor,db,category,topics)                
    
def articlefun(source):
    lst = [article for article in source.findAll("article") if article.has_attr('class') if "article" in article["class"]]
    return lst[0]

def article_details(article):
    img_link =''
    try:
        for h1 in article.findAll("h1"):
            news_title = h1.text
    except:
        pass
    for fig in article.findAll("figure"):
        try:
            img_link_prev = (str(fig).split("url(")[-1]).split(');')[0]
            if "figure" not in img_link_prev:
                img_link +=img_link_prev+"\n"
        except:
            pass
    
    author_lst = [span.text for div in article.findAll("div") if div.has_attr('class') if "article-byline" in div["class"] for span in div.findAll("span")]
    date_lst = [" ".join(div.text.strip().split(" ")[-3:]) for div in article.findAll("div") if div.has_attr('class') if "article-byline" in div["class"]]
    p_lst = [p.text.strip() for div in article.findAll("div") if div.has_attr('class') if "article-entry" in div["class"] for p in div.findAll("p")]
#    print("\n",author_lst,"\n",date_lst)
    try:
        date_time = date_lst[0]
    except:
        date_time = ""
    try:
        author = author_lst[0]
    except:
        author = ""
    summary = "\n".join(p_lst)
    return news_title,date_time,author,summary,img_link
