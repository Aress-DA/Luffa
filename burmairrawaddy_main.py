# -*- coding: utf-8 -*-
"""
Created on Thu May 30 20:18:35 2019

@author: anjali.dharmik
"""
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

from burmairrawaddy_categories import find_categories
from burmairrawaddy_articles import find_articles
from burmairrawaddy_data import articlesourcefun

def burmairrawaddy_main(browser,url,cursor,db):
    category_list,browser = find_categories(url,browser) 
    if len(category_list) >0:
        for category_url in category_list:
            category = category_url.replace(url,"").replace("/",",").replace("archives,","").replace("category,","")
            article_lst,browser = find_articles(category_url,browser)
            articlesourcefun(article_lst,browser,category,cursor,db)

        
    


 