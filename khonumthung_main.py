# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 14:57:18 2019

@author: admin
"""

#https://khonumthung.org/?cat=1
from bs4 import BeautifulSoup
from dateutil import parser
from article_db import upload_article

def khonumthung(browser,url,cursor,db):
    page = browser.get(url)
    if page.status_code==200:
        source = BeautifulSoup(page.content)
        for j in range(1,5):
            cat_url = url+"?cat="+str(j)
            
            page = browser.get(cat_url)
            if page.status_code==200:
                source = BeautifulSoup(page.content)
                #######pagination############
                pages =[1]
                pages.extend([int(a.text) for a in source.findAll("a",attrs={"class","page-numbers"}) if a.text != "Next"])
                page_count =0#max(pages)
                
                for i in range(page_count+1):
                    page_url = "https://khonumthung.org/?paged="+str(i)+"&cat="+str(j)
                    page = browser.get(page_url)
                    if page.status_code==200:
                        source = BeautifulSoup(page.content)
                    
                        article_lst = source.findAll("div",attrs={"class","column half b-col"})
                        for article in article_lst:
                            article_title,date_time,author,summary,article_url,img_link ="","","","","",""
                                
                            article_title_div = article.find("h2",attrs={"class","post-title"})
                            article_title = article_title_div.text.strip()
                            article_url = article_title_div.find("a")["href"]
                            
                            date_time = article.find("time").text.strip()
                            try:
                                _div = article.find("a",attrs={"class","image-link"})
                                img_link = _div.find("img")["src"]
                            except:
                                pass
                            try:
                                summary_div = article.find("div",attrs={"class","excerpt"})
                                summary = summary_div.find("p").text.strip()
            
                            except:
                                pass
                            try:
                                page = browser.get(article_url)
                                if page.status_code==200:
                                    source = BeautifulSoup(page.content)
                                    article = source.find("article")#,attrs={"class","item-list"})
                            except:
                                pass
                            try:
                                author = article.find("span",attrs={"class","reviewer"}).text.strip()
                                summary_div = article.find("div",attrs={"class","post-content description"})
                                summary += "\n".join([p.text.strip() for p in summary_div.findAll("p")])
                            except:
                                pass
                            from dateutil import parser as dparser
                            date_time = dparser.parse(date_time,fuzzy=True)

                            upload_article(article_title,date_time,author,summary,article_url,url,img_link,cursor,db,"news","")
#                    except:
#                        pass
                   