
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 14:59:44 2019

@author: anjali.dharmik
"""
from article_db import upload_article
from selenium import webdriver
from bs4 import BeautifulSoup
import re

#########################translator###############
from translate import Translator
translator= Translator(from_lang='burmese',to_lang="en")

#################language identifier#####################
import langid
def lang_identifier_mm(text):
    if "en" == langid.classify(text)[0]:
        return False
    else:
        return True

#cat_div_lst = source.findAll("div",attrs={"class","menu"})
#category_list = [a["href"] for cat_div in cat_div_lst for a in cat_div.findAll("a") if a.has_attr('href') and (".html" in a["href"]) and (a["href"] not in ["http://java.oms.apps.opera.com/en_us/voa_news_for_java_phones.html?dm=1&multi=1&set_lang=en","http://m.burmese.voanews.com/rss.html?tab=Podcast","http://m.burmese.voanews.com/rss.html?tab=Rss","/login.html","/p/3830.html","/subscribe.html","http://m.burmese.voanews.com/subscribe.html"])]
#print(category_list)
#
#for cat_url in category_list:
#    if "burmese.voanews.com" not in cat_url:
#        cat_url = "https://burmese.voanews.com"+cat_url
#    print("category ------",cat_url)
#    page = browser.get(cat_url)
#    source = BeautifulSoup(page.content)
#    article_lst = [a["href"] for a in source.findAll("a") if a.has_attr('href') if "/a/" in a["href"]]
#    article_lst = list(set(article_lst))
#    #print(article_lst)
#    #############page count##########
#    page_lst = ["https://burmese.voanews.com"+a["href"] for a in source.findAll("a",attrs={"class","link-more"}) if a.has_attr('href') if "/z/" in a["href"]]
#    print(page_lst)
def voa_main(browser,url,cursor,db):

    count=0
    for page_url in list(set(['https://burmese.voanews.com/z/2513','https://burmese.voanews.com/z/2517', 'https://burmese.voanews.com/z/4380', 'https://burmese.voanews.com/z/4381',\
    'https://burmese.voanews.com/z/2524', 'https://burmese.voanews.com/z/2524', 'https://burmese.voanews.com/z/4381', 'https://burmese.voanews.com/z/4380',\
    'https://burmese.voanews.com/z/2512', 'https://burmese.voanews.com/z/4843','https://burmese.voanews.com/z/4251', 'https://burmese.voanews.com/z/4251',\
    'https://burmese.voanews.com/z/4843','https://burmese.voanews.com/z/2525',\
    'https://burmese.voanews.com/z/4406','https://burmese.voanews.com/z/4853', 'https://burmese.voanews.com/z/4385','https://burmese.voanews.com/z/4382',\
    'https://burmese.voanews.com/z/4863','https://burmese.voanews.com/z/4384','https://burmese.voanews.com/z/4860','https://burmese.voanews.com/z/4861', \
    'https://burmese.voanews.com/z/4862','https://burmese.voanews.com/z/5180',\
    'https://burmese.voanews.com/z/4511', 'https://burmese.voanews.com/z/4582','https://burmese.voanews.com/z/5011'])):
        val_lst =[]
        article_lst =[]
        count +=1
        for i in range(2):
            page_url = page_url+"?p="+str(i)#page_lst[0]
            try:
                page = browser.get(page_url)
                source = BeautifulSoup(page.content)
            except:
                source =""
            if source !="":
                try:
                    article_lst.extend([a["href"] for a in source.findAll("a") if a.has_attr('href') if "/a/" in a["href"]])
                    article_lst = list(set(article_lst))
                    for article_url in article_lst:
                        if "burmese.voanews.com" not in article_url:
                            article_url = "https://burmese.voanews.com"+article_url
            #                print("article ------",article_url)
                            page = browser.get(article_url)
                            source = BeautifulSoup(page.content)
                            
                            article_title = ",".join([_title.text.strip() for _title in source.findAll("h1",attrs={"class","pg-title"})])
                            date_time = ",".join([_time.text.strip() for _date_time in source.findAll("div",attrs={"class","col-publishing-details"}) for _time in _date_time.findAll("time")])
                            author = ",".join([a.text.strip() for a in source.findAll("a",attrs={"class","links__item-link"}) if a.has_attr('href') and "/author/" in a["href"]])
                            try:
                                summary = "\n".join([p.text.strip() for p in source.find("div",attrs={"class","wsw"}).findAll("p")])
                            except:
                                summary =""
                            try:
                                img_link = source.find("div",attrs={"class","thumb"}).find("img")["src"]
                            except:
                                img_link =""
                            if lang_identifier_mm(date_time) == True:
                                date_time = translator.translate(date_time)
                            topics =""
                            category ="news"
                            upload_article(article_title,date_time,author,summary,article_url,url,img_link,cursor,db,category,topics)
                except:
                    pass
                   