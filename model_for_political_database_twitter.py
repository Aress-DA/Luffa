# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 13:28:59 2019

@author: anjali.dharmik
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import re,time
from article_db import upload_article
import pandas as pd
from dateutil import parser

def twitter_wrapper(browser,url,cursor,db):
    page = browser.get(url)
    
    
    #scrolling down...
    pause = 3
    
    lastHeight = browser.execute_script("return document.body.scrollHeight")
    #print(lastHeight)
    
    sub_url_lst =[]
    i = 0
    source =""
    
    browser.get_screenshot_as_file("test03_1_"+str(i)+".jpg")
    while True:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(pause)
        newHeight = browser.execute_script("return document.body.scrollHeight")
        #print(newHeight)
        if newHeight == lastHeight:
            break
        lastHeight = newHeight
        i += 1
    
        #extract JSON from web pages...
        source = BeautifulSoup(page.content)
        
        for st in source.findAll('div'):
            try:
                
                if "content" in st["class"]:
                    sub_url_lst.append(st)
            except:
                pass
        
        for d in sub_url_lst:
            name,author,post,_datetime,img_link =[],'','','',''
            for d1 in d.findAll('strong'):
                name.append(d1.get_text())
            for d4 in d.findAll('span'):
                try:
                    if "username" in d4["class"]:
                        author =d4.get_text()
                except:
                    pass
            for d2 in d.findAll('p'):
                post = d2.get_text()
            for d3 in d.findAll('small'):
                for d4 in d3.findAll('span'):
                    _datetime = d4.text
            for d5 in d.findAll('div'):
                try:                        
                    for img in d5.findAll('img'):
                        
                        img_link = str(img["src"])+"\n"
                        print(img_link)
                except:
                    pass
            
            _name =name[0]
            if _datetime !='' and post !="":
                topics = ""
                upload_article(_name,_datetime,author,post,url,url,img_link,cursor,db,"news",topics)                
    return ""




