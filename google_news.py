# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 11:09:03 2019

@author: admin
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import re
from dateutil import parser

import datetime
import pandas as pd
from dateutil import parser
from article_db import upload_article
import pandas as pd

def google_news(browser,url,cursor,db,category):
    try:
        page = browser.get(url)
        source = BeautifulSoup(page.content)
    except:
        source =""
    if source !="":
        article_lst = source.findAll("div",attrs={"class","NiLAwe"})
        for article in article_lst:
            try:
                article_div = article.find("h3")
                article_title = article_div.text
                weblink = "https://news.google.com"+article_div.find("a")["href"]
                summary = article.find("div",attrs={"class","Da10Tb"}).text
                date_time = article.find("time")["datetime"].split("T")[0]
            except:
                article_title,weblink,summary,date_time ="","","",""
            try:
                img_link = article.find("img")["src"]
            except:
                img_link=""
                        
            topics = ""
            upload_article(article_title,date_time,"",summary,weblink,"https://news.google.com",img_link,cursor,db,category,topics)                

    
