# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 19:55:39 2019

@author: anjali.dharmik
"""

#http://www.kachinlandnews.com

from selenium import webdriver
from bs4 import BeautifulSoup
from dateutil import parser
from article_db import upload_article


def kachinlandnews_main(browser,url,cursor,db):
    page = browser.get(url)
    if page.status_code==200:
        source = BeautifulSoup(page.content)
       
        category_list = [a["href"] for ul in source.findAll("ul") if ul.has_attr('id') if "menu-primary" in ul["id"] for a in ul.findAll("a") if a["href"] not in ['http://kachinlandnews.com',"http://kachinlandnews.org","http://kachinlandnews.com/?page_id=23598"]]
        category_list = list(set(category_list))        
        if len(category_list) >0:
            for cat_url in category_list:
                category = "news"#cat_url.replace(url,"").replace("/",",").replace("archives","").replace("category","")
                page = browser.get(cat_url)
                if page.status_code==200:
                    source = BeautifulSoup(page.content)
                
                    ########pagination############
                    pages =[1]
                    pages.extend([int(span.text) for span in source.findAll("a",attrs={"class","page-numbers"}) if span.text not in ["…","Next"]])
                    page_count =max(pages)
                    for i in range(page_count+1):
                        page_url = cat_url+"&paged="+str(i)
                        page = browser.get(page_url)
                        if page.status_code==200:
                            source = BeautifulSoup(page.content)
                        
                            article_lst = source.findAll("article")
                            
                            for article in article_lst:
                                article_title,date_time,author,summary,article_url,img_link ="","","","","",""
                                
                                article_title_div = article.find("h3",attrs={"class","entry-title"})
                                try:
                                    article_title = article_title_div.text.strip()
                                    article_url = article_title_div.find("a")["href"]

                                    date_time = article.find("span",attrs={"class","published"}).text.strip()
                                    author = article.find("span",attrs={"class","author"}).text.strip()
                                    _div = article.find("div",attrs={"class","entry-thumbnail"})
                                    img_link = _div.find("img")["src"]
                                                                
                                    summary_div = article.find("div",attrs={"class","entry-content"})
                                    summary = summary_div.find("p").text.strip()
                                except:
                                    pass
                                page = browser.get(article_url)
                                if page.status_code==200:
                                    source = BeautifulSoup(page.content)

                                    article = source.find("article")
                                    try:
                                        summary_div = article.find("div",attrs={"class","entry-content"})
                                        summary += "\n".join([p.text.strip() for p in summary_div.findAll("p")])
                                        date_time = article.find("span",attrs={"class","published"}).text.strip()
                                        author = article.find("span",attrs={"class","author"}).text.strip()
                                    except:
                                        pass
                                    topics = ""
                                    upload_article(article_title,date_time,author,summary,article_url,url,img_link,cursor,db,category,topics)
                        