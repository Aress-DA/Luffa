# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 12:44:59 2019

@author: anjali.dharmik
"""

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
print("started---------")
from mmtimes_categories import find_categories
from mmtimes_articles import find_articles
from mmtimes_data import articlesourcefun


def main():
#    print("started---------find_categories")
    url = "https://myanmar.mmtimes.com"
    category_list,browser = find_categories(url,browser)
    print(category_list,"\nlog-number of categories: ",len(category_list))
    
    print("started---------find_articles")
    articles_lst,browser = find_articles(category_list,browser)
    print(articles_lst)                        
    print("log-number of articles: ",len(articles_lst))
