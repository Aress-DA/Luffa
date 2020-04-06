# -*- coding: utf-8 -*-
"""
Created on Thu Thus 16 20:19:01 2019

@author: anjali.dharmik
"""
from bs4 import BeautifulSoup

import warnings
warnings.filterwarnings("ignore")#, category=FutureWarning)

import requests

def page_categories(source):
    category_list = set()
    if source !="":
        for div in source.findAll("div"):
            try:
                if "mastnav" in div["id"]:
                    for a in source.findAll("a"):
                        if "category" in str(a["href"]):
                            category_list.add(a["href"])
            except:
                pass
    return list(category_list)

def find_categories(url,browser):
    try:
        page = requests.get(url)
        source = BeautifulSoup(page.content)
    except:
        source =""
    return page_categories(source)
    
