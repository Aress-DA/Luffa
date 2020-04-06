# -*- coding: utf-8 -*-
"""
Created on May 16 14:43:00 2019

@author: anjali.dharmik
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import re
from dateutil import parser
from article_db import upload_article

def page_categories(source,url):
    category_list,category_list1 = set(),set()
    for a in source.findAll("a"):
        try:
            if "category" in str(a["href"]):
                if url not in str(a["href"]):
                    category_list.add(url+a["href"])
                else:
                    category_list.add(a["href"])
            elif url in str(a["href"]):
                category_list1.add(a["href"])
        except:
            pass
    if len(list(category_list)) <1:
        category_list = category_list1
    return list(category_list)

def page_count(source):
    a_list = []
    pages =""
    for a in source.findAll("a"):
        try:
            if "page" in str(a["href"]):
                a_list.append(int(str(a["href"]).split("page/")[-1]))
            else:
                pages = max([int(i) for i in re.findall(r'\d+',str(source.title))])
        except:
            pass
    try:
        pages = max(a_list)
    except:
        pass
    return pages

def article_globalnewlightofmyanmar(browser,url,cursor,db):
#    page = browser.get(url)
#    source = BeautifulSoup(page.content)
#    category_list = page_categories(source,url)
    category_list = ['http://www.globalnewlightofmyanmar.com/category/editors-choice/',
                    'http://www.globalnewlightofmyanmar.com/category/regional-new/',
                    'http://www.globalnewlightofmyanmar.com/category/business/', 
                    'http://www.globalnewlightofmyanmar.com/category/local-news/',
                    'http://www.globalnewlightofmyanmar.com/category/opinion/', 
                    'http://www.globalnewlightofmyanmar.com/category/national/']
    for category_url in category_list:
        try:
            page = browser.get(category_url+"page/2")
            source = BeautifulSoup(page.content)
        except:
            source=""
        if source !="":
            pages = 0#page_count(source)
            for i in range(pages+1):
                suburl =category_url+"page/" +str(i)
                try:
                    page = browser.get(suburl)
                    source = BeautifulSoup(page.content)
                except:
                    source=""
                if source !="":
                    article_lst = source.findAll("li",attrs={"class": "post"})
        #            print(len(post_link_lst))
                    for article in article_lst:
                        article_url = article.find("h2",attrs={"class": "cat-grid-title"}).find("a")["href"]
                        article_title = article.find("h2",attrs={"class": "cat-grid-title"}).text.strip()
                        
                        author = article.find("a",attrs={"itemprop": "author"}).text.strip()
                        img_link = article.find("figure",attrs={"class": "post-thumbnail"}).find("img")["src"]
                        full_text = article.find("div",attrs={"class": "entry-content"}).text.strip()
                        try:
                            page = browser.get(article_url)
                            source = BeautifulSoup(page.content)
                            category = source.find("div",attrs={"class": "entry-cat"}).text.strip()
                            full_text = "\n".join([p.text.strip() for p in source.find("div",attrs={"class": "entry-content"}).findAll("p")])
                            publication_date = source.find("time",attrs={"class": "entry-date"}).text.strip()
                        except:
                            publication_date =""
                        topics =""
                        upload_article(article_title,publication_date,author,full_text,article_url,url,img_link,cursor,db,category,topics)
