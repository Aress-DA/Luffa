# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 13:23:02 2019

@author: anjali.dharmik
"""

from bs4 import BeautifulSoup
from upload_data_mysql import uploaddata_mysql
from article_type import idf

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

from translate import Translator
translator= Translator(from_lang='burmese',to_lang="en")

import langid
def lang_identifier_mm(text):
    if "en" == langid.classify(text)[0]:
        return False
    else:
        return True

def article_details(source1,url):        
    ##tags and releted news,mediaContainer(audio,video) relatedstories
    news_title,img_link,date_time,author,summary ='','','','',''
    author = [span.text for div in source1.findAll("div") if div.has_attr('class') if 'page-header__meta-item' in  div["class"] for span in div.findAll("span")]
    date_time = [div.text for div in source1.findAll("div") if div.has_attr('class') if 'page-header__meta-item' in div["class"]]
    news_title = [h1.text for div in source1.findAll("div") if div.has_attr('class') if "page-header" in div["class"] for h1 in div.findAll("h1")]
    summary = [div.text for div in source1.findAll("div") if div.has_attr('class') if "article__content" in div["class"]]
    img_link = [a["href"] for div in source1.findAll("div") if div.has_attr('class') if "article__featured-media" in div["class"] for a in div.findAll("a")]

    news_title = ("\n".join(news_title)).strip("\n")
    date_time = date_time[-1]
    author = author[-1]
    summary =("\n".join(summary)).strip("\n")
    img_link = ",".join(img_link)
    
    return news_title,date_time,author,summary,img_link


def articlesourcefun(articles_lst,browser):
    url = "https://burmese.voanews.com/"
    not_processed = []
    for article_url in articles_lst:
        if "https://burmese.voanews.comhttps://burmese.voanews.com" in article_url:
            article_url =article_url.replace("https://burmese.voanews.comhttps://burmese.voanews.com","https://burmese.voanews.com")
        try:
            page = browser.get(article_url)
            source = BeautifulSoup(page.content)
            entry_name,date_time,author,summary,img_link = article_details(source,article_url)
            uploaddata_mysql(article_url,entry_name,date_time,author,summary,img_link,url)
        except:
            not_processed.append(article_url)
