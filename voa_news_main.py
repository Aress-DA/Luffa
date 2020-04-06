# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 11:45:42 2019

@author: anjali.dharmik
"""
from bs4 import BeautifulSoup
from article_db import upload_article

def voa_main(browser,url,cursor,db):   
    try:
        page = browser.get(url)
        source = BeautifulSoup(page.content)
    except:
        source =""
    if source !="":
        category = "news"
        
        articles_lst = source.findAll("div",attrs={"class": "vertical-list__item"})
        
        for article in articles_lst:
            try:
                entry_name = article.find("h2",attrs={"class": "teaser__title"}).text.strip()
                article_url = "https://www.voanews.com/"+article.find("a",attrs={"class": "teaser__title-link"})["href"]
                date_time = article.find("div",attrs={"class": "teaser__date"}).text.strip()
            except:
                pass
            try:
                img_link = "https://www.voanews.com/"+article.find("img")["src"]
            except:
                img_link =""
            author =""
            try:
                page = browser.get(article_url)
                source = BeautifulSoup(page.content)
            except:
                source=""
            if source!="":
                try:
                    summary =  "\n".join([p.text.strip() for p in source.find("div",attrs={"class": "episode__body"}).findAll("p")])
                except:
                    summary ="\n".join([p.text.strip() for p in source.find("div",attrs={"class": "article__body"}).findAll("p")])
                try:
                    author = source.find("div",attrs={"class": "page-header__meta-item"}).findAll("span")[1].text.strip()
                except:
                    pass
                topics =""
                upload_article(entry_name,date_time,author,summary,article_url,url,img_link,cursor,db,category,topics)
