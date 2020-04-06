# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 12:05:26 2019

@author: anjali.dharmik
"""

from bs4 import BeautifulSoup

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
from browser_setting import open_browser

def find_articles(category_url,browser):
    post_link_lst =[]
    source = BeautifulSoup(page.content)
    _list = ["https://burmese.voanews.com"+a["href"] for a in source.findAll("a") if a.has_attr('href') if "/a/" in a["href"]]

    post_link_lst.extend(list(set(_list)))
    return list(set(post_link_lst)),browser