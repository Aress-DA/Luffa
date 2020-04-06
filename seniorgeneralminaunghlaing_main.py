# -*- coding: utf-8 -*-
"""
Created on Fri May 31 12:09:28 2019

@author: admin
"""

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
from bs4 import BeautifulSoup
from article_db import upload_article
from dateutil import parser
                
def date_change(str_):
    date_time =""
    from translate import Translator
    translator= Translator(from_lang='burmese',to_lang="en")
    
    import langid
    def lang_identifier_mm(text):
        if "en" == langid.classify(text)[0]:
            return False
        else:
            return True
    
    import nltk,datetime
    current_month = datetime.datetime.now().date().month
    from dateutil import parser
    keywords = ["naypyidaw","naypyitaw","nay","daw","pyi","taw"]
    for _line in nltk.line_tokenize(str_):
        if lang_identifier_mm(_line) == True:
            _line = translator.translate(_line)
            _line = _line.lower()
            for _key in keywords:
                if _key in nltk.word_tokenize(_line):
                    date_time = "2019 "+_line.replace(_key,"").replace(" on ","")
                    date_month = parser.parse(date_time).month
                    if date_month < current_month:
                        date_time = "2018 "+_line.replace(_key,"").replace(" on ","")
    return date_time

def sub_data(source1):        
    news_title,img_link,date_time,author,summary ='',[],'','',''
    for article in source1.findAll("article"):
        for div in article.findAll("div"):
            try:
                if "figure-cat-wrap" in div["class"]:
                    for img in div.findAll("img"):
                        img_link.append(img["src"])
                if "below-entry-meta" in div["class"]:
                    for span in div.findAll("span"):
                        if "byline" in span["class"]:
                            author = span.text
                if "entry-content" in div["class"]:
                    summary = div.text
                    for a in div.findAll("a"):
                        img_link.append(a["href"])
            except:
                pass
        for span in article.findAll("span"):
            try:
                if "posted-on" in span["class"]:
                    for time in span.findAll("time"):
                        if "entry-date" in time["class"]:
                            date_time =time.text
                        else:
                            date_time = date_change(summary)
            except:
                pass
        for header in article.findAll("header"):
            news_title = header.text

    Image="\n".join(img_link)
    return summary,news_title,date_time,Image,author

def se_main(browser,url,cursor,db):
    pages =2
    for i in range(pages+1):
        try:
            page = browser.get(url+"/page/"+str(i))
            source = BeautifulSoup(page.content)
        except:
            source =""
        if source !="":            
            articles_lst = [a["href"] for article in source.findAll("article") for h2 in article.findAll("h2",attrs={"class": "entry-title"}) for a in h2.findAll("a")]
            not_processed_articles =[]
            for article in articles_lst:
                try:
                    page = browser.get(article)
                    source = BeautifulSoup(page.content)
                    summary,entry_name,date_time,Image,author = sub_data(source)
                    topics = ""
                    upload_article(entry_name,date_time,author,summary,article,url,Image,cursor,db,"news",topics)                
                except:
                    not_processed_articles.append(article)
