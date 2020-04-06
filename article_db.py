
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 22:28:06 2019

@author: anjali.dharmik
"""
import datetime
from dateutil import parser

def upload_article(article_title,date_time,author,summary,article_url,url,img_link,cursor,db,category,topics):
    if date_time != "": 
        try:
            news_date = date_time.strftime("%y%m%d")
        except:
            date_time,news_date =datetime.datetime.now(),datetime.datetime.now().strftime("%y%m%d") 
    else:  
        date_time,news_date =datetime.datetime.now(),datetime.datetime.now().strftime("%y%m%d")
    
    try:
        article_title = news_date +" "+article_title
    except:
        article_title = article_title        
    try:
        sql = "INSERT INTO articles_database_unique1(article_title, publication_date, author, full_text, weblink, source, news_category, media_links, input_time, media_topic_tag) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = [(article_title, date_time, author,summary,article_url,url,category,img_link,datetime.datetime.utcnow(),topics)]
        
        cursor.executemany(sql, val)
        db.commit()
        print(cursor.rowcount, "record inserted.\n")

                        
    except:
        print("Duplicate Record.\n")