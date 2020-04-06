# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 18:59:39 2019

@author: anjali.dharmik
"""

#http://www.narinjara.com/burmese/  

from selenium import webdriver
from bs4 import BeautifulSoup
from article_db import upload_article

def narinjara_main(browser,url,cursor,db):
    page = browser.get(url)
    if page.status_code==200:
        source = BeautifulSoup(page.content)
        category = "news"
        ########pagination############
        pages =[1]
        pages.extend([int(span.text.split("of ")[-1]) for span in source.findAll("span",attrs={"class","pages"})])
        page_count = max(pages)
        for i in range(page_count+1):
            page_url = url+"?page="+str(i)
            page = browser.get(page_url)
            if page.status_code==200:
                source = BeautifulSoup(page.content)
                article_lst = source.findAll("article",attrs={"class","entry-item"})            
                for article in article_lst:
                    article_title,date_time,author,summary,article_url,img_link ="","","","","",""
                    try:
                        article_title_div = article.find("h2",attrs={"class","entry-title"})
                        article_title = article_title_div.text.strip()
                        article_url = "https://burmese.narinjara.com"+article_title_div.find("a")["href"]
                    except:
                        pass
                    try:
                        p_div = article.find("ul",attrs={"class","entry-meta"})
                        date_time = p_div.find("li",attrs={"class","entry-date"}).text.strip()
                        author = p_div.find("li",attrs={"class","entry-author"}).text.strip()
                    except:
                        pass
                    try:
                        _div = article.find("div",attrs={"class","entry-img"})
                        img_link = "https://burmese.narinjara.com"+_div.find("img")["src"]
                    except:
                        pass
                    try:
                        summary_div = article.find("div",attrs={"class","entry-content"})
                        summary = summary_div.find("p").text.strip()
                    except:
                        pass
                    page = browser.get(article_url)
                    if page.status_code==200:
                        source = BeautifulSoup(page.content)
                        try:
                            article = source.find("article")#,attrs={"class","item-list"})
                            summary_div = article.find("div",attrs={"class","entry"})
                            summary += "\n".join([p.text.strip() for p in summary_div.findAll("p")])
                        except:
                            pass
                    topics = ""
                    upload_article(article_title,date_time,author,summary,article_url,url,img_link,cursor,db,category,topics)
                    