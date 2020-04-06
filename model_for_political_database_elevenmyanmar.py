# -*- coding: utf-8 -*-
"""
Created on Mon May 16 14:43:00 2019

@author: anjali.dharmik
"""

from selenium import webdriver
from bs4 import BeautifulSoup
from article_db import upload_article

def page_categories(source,url):
    category_list = set()
    for ul in source.findAll("ul"):
        for a in ul.findAll("a"):
            category_list.add(a["href"])

    return list(category_list)

def page_count(source):
    a_list = [1]
    pages ="1"
    for a in source.findAll("a"):
        try:
            if "page" in str(a["href"]):
                a_list.append(int(str(a["href"]).split("page=")[-1]))
        except:
            pass
    try:
        pages = max(a_list)
    except:
        pass
    return pages

def sub_data(source1):        
    news_title,img_link,news_date,date_time,author,summary,related_news ='','','','','','',[]
    for article in source1.findAll("article"):
        try:
            news_title = source1.title.text.split("|")[0]
            
            for div in article.findAll("div"):
               if "news-detail-news-image-wrapper" in div["class"]:
                   for img in div.findAll("img"):
                       img_link = img["src"]
               if "news-detail-date-author-info-date" in div["class"]:
                   for span in div.findAll("span"):
                       date_time =span.text
               if "news-detail-date-author-info-author" in div["class"]:
                   author = div.text
               if "view-mode-full" in div["class"]:
                   summary = div.text
        except:
            pass
    for div in source1.findAll("div"):
        try:
            if "news-title" in div["class"]:
                for a in div.findAll("a"):
                    related_news.append(a["href"])
        except:
            pass
    english_summary = ""#lang_identifier_en(summary)
    burmese_summary=""#lang_identifier_mm(summary)
    entry_name=news_date+" "+news_title
    Image=img_link
    return [english_summary,summary,burmese_summary,entry_name,date_time,Image,author]

def data_collection_and_tagging(source):
    _list = set()
    for a in source.findAll("a"):
        try:
            if "news" in str(a['href']):
                if "elevenmyanmar.com/" not in str(a["href"]):
                    _list.add("https://elevenmyanmar.com"+a["href"])
                else:
                    _list.add(a["href"])
        except:
            pass
    post_link_lst = list(_list)
    return post_link_lst

##page count
def article_elevenmyanmar(browser,url,cursor,db):    
    page = browser.get(url)
    source = BeautifulSoup(page.content)
    category_list = ["https://elevenmyanmar.com/editorial","https://elevenmyanmar.com/politics",\
                     "https://elevenmyanmar.com/opinion","https://elevenmyanmar.com/crime",\
                     "https://elevenmyanmar.com/business","https://elevenmyanmar.com/interview",\
                     "https://elevenmyanmar.com/economy"]#page_categories(source,url)
    for category_url in category_list:
        category = category_url.replace(url+",","").replace("/",",").replace("archives,","").replace("category,","")

        print("category_url ------",category_url,"\n")
        page = browser.get(category_url)
        source = BeautifulSoup(page.content)
        pages = 2#page_count(source)
        print(pages,"\n")
        for i in range(int(pages)):
            print("page_number = ",i)
            suburl =category_url+"?page=" +str(i)
            page = browser.get(suburl)
            source = BeautifulSoup(page.content)
            post_link_lst = data_collection_and_tagging(source)
#            print(len(post_link_lst))
            for post_link in post_link_lst:
                try:
#                    print(post_link)
                    page = browser.get(post_link)
                    source = BeautifulSoup(page.content)
                    _sub_dict = sub_data(source)
                    article_title = _sub_dict[3]
                    publication_date = _sub_dict[4]
                    author = _sub_dict[6]
                    full_text = _sub_dict[1]
                    img_link = post_link +"\n"+ _sub_dict[5]
                    topics = ""
                    upload_article(article_title,publication_date,author,full_text,post_link,url,img_link,cursor,db,category,topics)                

                except:
                    print("\n\n not processed",post_link,"\n\n")
