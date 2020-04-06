# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 15:42:41 2019

@author: anjali.dharmik
"""

#http://www.7daydaily.com/
from daydaily_articles import find_articles
from daydaily_data import articlesourcefun
from daydaily_categories import find_categories

def daydaily_main(browser,url,cursor,db):
    category_list,browser = find_categories(url,browser)
    if len(category_list)>0:
        for category_url in category_list:
            articles_lst,browser = find_articles(category_url,browser)
            category = category_url.replace(url,"").replace("/",",").replace("archives,","").replace("category,","")
            articlesourcefun(articles_lst,browser,category,cursor,db)


