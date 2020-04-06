# -*- coding: utf-8 -*-
"""
Created on Thu May 30 20:34:46 2019

@author: anjali.dharmik
"""
from bs4 import BeautifulSoup
import requests
import warnings
warnings.filterwarnings("ignore")#, category=FutureWarning)

from article_db import upload_article
from dateutil import parser

def find_articles(category_list,browser,cursor,db):
    for category_url in category_list:
        articles = []
        try:
            page = requests.get(category_url)
            source = BeautifulSoup(page.content)
        except:
            source =""
        if source !="":
            try:
                pages = 2#[math.ceil(int(re.findall('\d+',span.text)[0])/15) for span in source.findAll("span",attrs={"class","count"}) if "Found" in span.text][0]
                for i in range(pages+1):
                    page = requests.get(category_url+"/page/"+str(i))
                    source = BeautifulSoup(page.content)
                    articles.extend(source.findAll("article"))
            except:
                pass
        count=0
        for article in list(set(articles)):
            count+=1
            try:
                news_title = [h.text.strip() for h in article.findAll("header",attrs={"class","article-header"})][0]
            except:
                news_title =""
            try:
                author = [h.text.strip() for h in article.findAll("span",attrs={"class","reporter"})][0]
            except:
                author =""
            try:
                news_category = [h.text.strip() for h in article.findAll("span",attrs={"class","category"})][0]
            except:
                news_category =""
            try:
                summary = [h.text.strip() for h in article.findAll("div",attrs={"class","entry"})][0]
            except:
                summary =""
            try:
                image_link = [h["data-src"] for h in article.findAll("figure")][0]
            except:
                image_link =""
            try:
                article_link = [a["href"] for h in article.findAll("header",attrs={"class","article-header"}) for a in h.findAll("a")][0]
            except:
                article_link =""
            try:
                page = requests.get(article_link)
                source = BeautifulSoup(page.content)
                article = source.find("article")
                full_text = "\n".join([p.text.strip() for h in article.findAll("div",attrs={"class","article-entry"}) for p in h.findAll("p") if not p.has_attr('class')])
            except:
                full_text =""
            try:
                date_time = parser.parse([" ".join(h.text.strip().split(" ")[-3:]) for h in article.findAll("div",attrs={"class","article-entry"})][0],fuzzy=True)
            except:
                date_time = "\n".join([" ".join(p.text.strip().split(" ")[-3:]) for h in article.findAll("div",attrs={"class","article-entry"}) for p in h.findAll("p",attrs={"class","date"})])
            try:
                related_articles ="\n".join(list(set([a["href"] for h in article.findAll("div",attrs={"class","article-entry"}) for p in h.findAll("p") for a in p.findAll("a")])))
            except:
                related_articles =""
            try:
                topics =[p.text.strip() for p in article.findAll("p",attrs={"class","article-tags"})][0].replace("Topics: ","")
            except:
                topics =""
            upload_article(news_title,date_time,author,full_text,article_link,"https://www.irrawaddy.com/",image_link,cursor,db,news_category,topics)                

#         