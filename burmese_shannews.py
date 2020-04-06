# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 12:05:04 2019

@author: admin
"""

#https://burmese.shannews.org/ 
from selenium import webdriver
from bs4 import BeautifulSoup
from article_db import upload_article

def shannews_main(browser,url,cursor,db):
    page = browser.get(url)
    if page.status_code==200:
        source = BeautifulSoup(page.content)
    
        category_list = [a["href"] for ul in source.findAll("ul") if ul.has_attr('id') if "menu-td-demo-header-menu-1" in ul["id"] for a in ul.findAll("a")]# if a["href"] !="/" and a["href"] !="#"]
        if len(category_list)>0:
            category_list = list(set(category_list))
            for cat_url in category_list:
                category = cat_url.replace(url,"").replace("/",",").replace("archives,","").replace("category,","")
        
                page = browser.get(cat_url)
                if page.status_code==200:
                    source = BeautifulSoup(page.content)
            
                    ########pagination############
                    pages =[1]
                    pages.extend([int(span.text.split("of ")[-1]) for span in source.findAll("span",attrs={"class","pages"})])
                    page_count =max(pages)
                
                    for i in range(page_count+1):
                        page_url = cat_url+"/page/"+str(i)
                        page = browser.get(page_url)
                        if page.status_code==200:
                            source = BeautifulSoup(page.content)
                        
                            article_lst = source.findAll("div",attrs={"class","td_module_10"})
                            
                            for article in article_lst:
            
                                article_title,date_time,author,summary,article_url,img_link ="","","","","",""
                                
                                try:
                                    article_title_div = article.find("h3",attrs={"class","td-module-title"})
                                    article_title = article_title_div.text.strip()
                                    article_url = article_title_div.find("a")["href"]
                                except:
                                    pass
                                try:
                                    p_div = article.find("div",attrs={"class","td-module-meta-info"})
                                    author = p_div.find("span",attrs={"class","td-post-author-name"}).text.strip()
    
                                    date_time = p_div.find("span",attrs={"class","td-post-date"}).text.strip()
                                except:
                                    pass

                                try:
                                    _div = article.find("div",attrs={"class","td-module-thumb"})
                                    img_link = _div.find("img")["src"]
                                except:
                                    pass
                                try:
                                    summary = article.find("div",attrs={"class","td-excerpt"}).text.strip()
                                except:
                                    pass
                                
                                page = browser.get(article_url)
                                if page.status_code==200:
                                    source = BeautifulSoup(page.content)
                                
                                    article = source.find("article")
                                    try:
                                        summary_div = article.find("div",attrs={"class","td-post-content"})
                                        summary += "\n".join([p.text.strip() for p in summary_div.findAll("p")])
                                    except:
                                        pass
                                    topics = ""
                                    
                                    upload_article(article_title,date_time,author,summary,article_url,url,img_link,cursor,db,category,topics)                
              