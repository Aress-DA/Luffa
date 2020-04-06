# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 10:36:28 2019

@author: anjali.dharmik
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 22:10:22 2019

@author: anjali.dharmik
"""

#https://news-eleven.com/
from selenium import webdriver
from article_db import upload_article
import pandas as pd
from dateutil import parser

from bs4 import BeautifulSoup
import re
from dateutil import parser
#from browser_setting import open_browser

import pandas as pd

def news_eleven(url,browser):
    #page = browser.get(url)
    #source = BeautifulSoup(page.content)
    category_list = ["https://news-eleven.com/news"]
    count=0
    for cat_url in category_list:
        count+=1
        val_lst =[]
        try:
            page = browser.get(cat_url)
            source = BeautifulSoup(page.content)
        except:
            source=""
        if source!="":
            ########pagination############
            pages =[1]
        #    pages.extend([int(a["href"].split("=")[-1]) for a in source.find("a") if a.has_attr('href') if "page" in a["href"]])
            page_count =1#max(pages)
            article_list =[]
            for i in range(page_count+1):
                
                page_url = cat_url+"?page="+str(i)
                try:
                    page = browser.get(page_url)
                    source = BeautifulSoup(page.content)
                except:
                    pass
                article_list.extend([a["href"] for article in source.findAll("div",attrs={"class","views-row"}) for a in article.findAll("a") if a.has_attr('href') and "/article/" not in a["href"]])
            for article_url in list(set(article_list)):
        #            try:
                
                page = browser.get(article_url)
                source = BeautifulSoup(page.content)
                article_title,date_time,author,summary,img_link ="","","","",""
                try:
                    article_title = source.find("div",attrs={"class","news-detail-title"}).text.strip()
                except:
                    pass
                try:
                    date_time = source.find("span",attrs={"class","date-display-single"}).text.strip()
                except:
                    pass
                try:
                    div_image = source.find("div",attrs={"class","news-image"})
                except:
                    pass
                try:
                    article_category = source.find("div",attrs={"class","news-detail-news-category"}).text.strip()
                except:
                    pass
                try:
                    author = source.find("div",attrs={"class","news-detail-date-author-info-author"}).text.strip()
                except:
                    pass
                
                try:
                    img_link = div_image.find("img")["src"]
                except:
                    pass
                
                try:
                    summary_div = source.find("div",attrs={"class","field-items"})
                    summary += "\n".join([p.text.strip() for p in summary_div.findAll("p")])
                except:
                    pass
                
                topics = ""
                upload_article(article_title,date_time,author,summary,article_url,url,img_link,cursor,db,article_category,topics)                
         
         
    
                