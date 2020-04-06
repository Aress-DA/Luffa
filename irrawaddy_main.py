# -*- coding: utf-8 -*-
"""
Created on Thu May 30 20:18:35 2019

@author: anjali.dharmik
"""
import warnings
warnings.filterwarnings("ignore")#, category=FutureWarning)

from irrawaddy_categories import find_categories
from irrawaddy_articles import find_articles

def irrawaddy_main(browser,url,cursor,db):
    
    ###############categories extraction #####################
    category_list = find_categories(url,browser)
    category_list.extend(['https://www.irrawaddy.com/election'])    
    find_articles(category_list,browser,cursor,db)


 

