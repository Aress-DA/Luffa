# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 22:46:40 2019

@author: anjali.dharmik
"""

print("-------------------------Webscraping-------------------------")
print("------------Connecting to MySQL Database --------------------")

import mysql.connector as mysql
db = mysql.connect(host="localhost",user="root1",passwd="1234",database="political_database")
cursor = db.cursor()

import requests

print("-------------------------open browser-------------------------")
browser = requests

#print("-------------------------khonumthung running-------------------------")
#from khonumthung_main import khonumthung
#url ="https://khonumthung.org/"
#khonumthung(browser,url,cursor,db)
#print("-------------------------khonumthung completed-------------------------")

#print("-------------------------bbc running-------------------------")
####################1#########################
#from bbc_main import bbc_main
#url = "https://www.bbc.com/burmese/"
#bbc_main(browser,url,cursor,db)
#print("-------------------------bbc completed-------------------------")
#
#
#print("-------------------------bnionline running-------------------------")
###################2#########################
#from bnionline_main import bnionline_main
#url = "https://www.bnionline.net/en/news"
#bnionline_main(browser,url,cursor,db)
#print("-------------------------bnionline completed-------------------------")
#
#print("-------------------------burmese.dvb running-------------------------")
###################3#########################
#from burmese_dvb import burmese_dvd_main
#url = "http://burmese.dvb.no/"
#burmese_dvd_main(browser,url,cursor,db)
#print("-------------------------burmese.dvb completed-------------------------")
#
#print("-------------------------burmese.monnews running-------------------------")
###################4#########################
#from burmese_monnews import burmese_monnews_main
#url = "http://burmese.monnews.org/"
#burmese_monnews_main(browser,url,cursor,db)
#print("-------------------------burmese.monnews completed-------------------------")
#'''
#print("-------------------------burmese.narinjara running-------------------------")
#
###################5#########################
#from burmese_narinjara import narinjara_main
#url = "https://burmese.narinjara.com/news/"#"http://www.narinjara.com/burmese/"
#narinjara_main(browser,url,cursor,db)
#print("-------------------------burmese.narinjara completed-------------------------")
#
#print("-------------------------kachinlandnews running-------------------------")
###################6#########################
#from kachinlandnews import kachinlandnews_main
#url = "http://www.kachinlandnews.com"#http://www.kachinnews.com/ 
#kachinlandnews_main(browser,url,cursor,db)
#print("-------------------------kachinlandnews completed-------------------------")
#print("-------------------------burmese.shannews running-------------------------")
###################7#########################
#from burmese_shannews import shannews_main
#url = "https://burmese.shannews.org/"
#shannews_main(browser,url,cursor,db)
#print("-------------------------burmese.shannews completed-------------------------")
#'''
#print("-------------------------facebook running-------------------------")
#print("-------------------------facebook TaiFreedomBurmese running-------------------------")
####################8#########################
#url = "https://www.facebook.com/TaiFreedomBurmese/"
#from fb_TaiFreedomBurmese import fb_TaiFreedomBurmese
#try:
#    fb_TaiFreedomBurmese(browser,url,cursor,db)
#except:
#    pass
#
#print("-------------------------facebook TaiFreedomBurmese completed-------------------------")
#print("-------------------------facebook hlamaung.shwe running-------------------------")
#
####################10#########################
#url = "https://www.facebook.com/hlamaung.shwe"
#from fb_hlamaung import fb_hlamaung
#try:
#    fb_hlamaung(browser,url,cursor,db)
#except:
#    pass
#print("-------------------------facebook hlamaung.shwe completed-------------------------")
#print("-------------------------facebook JointCeasefireMonitoringCommittee running-------------------------")
#
####################11#########################
#url = "https://www.facebook.com/JointCeasefireMonitoringCommittee/"
#from fb_JointCeasefireMonitoringCommittee import fb_JointCeasefireMonitoringCommittee
#try:
#    fb_JointCeasefireMonitoringCommittee(browser,url,cursor,db)
#except:
#    pass
#print("-------------------------facebook JointCeasefireMonitoringCommittee completed-------------------------")
#print("-------------------------facebook mba.gov running-------------------------")
#
####################12#########################
#url = "https://www.facebook.com/www.mba.gov.mm/"
#from fb_mba import fb_mba
#try:
#    fb_mba(browser,url,cursor,db)
#except:
#    pass
#
#print("-------------------------facebook mba.gov completed-------------------------")
#print("-------------------------facebook Ministry-of-Ethnic-Affairs-Myanmar running-------------------------")
#
####################13#########################
#url ="https://www.facebook.com/pages/category/Government-Organization/Ministry-of-Ethnic-Affairs-Myanmar-822764397855686/"
#from fb_ministry import fb_ministry
#try:
#    fb_ministry(browser,url,cursor,db)
#except:
#    pass
#print("-------------------------facebook Ministry-of-Ethnic-Affairs-Myanmar completed-------------------------")
#print("-------------------------facebook myanmarpresidentoffice running-------------------------")
#
####################14#########################
#url = "https://www.facebook.com/myanmarpresidentoffice.gov.mm/"
#from fb_myanmarpresidentoffice import fb_myanmarpresidentoffice
#try:
#    fb_myanmarpresidentoffice(browser,url,cursor,db)
#except:
#    pass
#print("-------------------------facebook myanmarpresidentoffice completed-------------------------")
#print("-------------------------facebook ncasignatoryeaoofficial running-------------------------")
#
####################15#########################
#url = "https://www.facebook.com/ncasignatoryeaoofficial/"
#from fb_nca_s_eao import fb_nca_s_eao
#try:
#    fb_nca_s_eao(browser,url,cursor,db)
#except:
#    pass
#
#print("-------------------------facebook ncasignatoryeaoofficial completed-------------------------")
#print("-------------------------facebook nrpc.myanmar running-------------------------")

####################16#########################
#url = "https://www.facebook.com/nrpc.myanmar/"
#from fb_nrpc import fb_nrpc
#try:
#    fb_nrpc(browser,url,cursor,db)
#except:
#    pass
#print("-------------------------facebook nrpc.myanmar completed-------------------------")
#
#print("-------------------------facebook state.counsellor running-------------------------")
#
####################17########################
#url = "https://www.facebook.com/state.counsellor/"
#from fb_state_cousellor import fb_state_counsellor
#try:
#    fb_state_counsellor(browser,url,cursor,db)
#except:
#    pass
#print("-------------------------facebook state.counsellor completed-------------------------")
#
#print("-------------------------cincds running-------------------------") 
###################18#########################
#from cincds_main import cincds_main
#url = "http://cincds.gov.mm/recentest-news"
#cincds_main(browser,url,cursor,db)
#print("-------------------------cincds completed-------------------------")

#print("-------------------------frontiermyanmar running-------------------------")
####################19#########################
#from frontiermyanmar_main import frontiermyanmar_main
#url = "https://frontiermyanmar.net/en/"
#frontiermyanmar_main(browser,url,cursor,db)
#print("-------------------------frontiermyanmar completed-------------------------")
#
#print("-------------------------hintharmedia running-------------------------")
####################20#########################
#from hintharmedia import hintharmedia
#url = "https://hintharmedia.com"
#hintharmedia(browser,url,cursor,db)
#print("-------------------------hintharmedia completed-------------------------")

#print("-------------------------kantarawaddytimes running-------------------------")
####################21#########################
#from kantarawaddytimes import kantarawaddytimes
#url = "http://www.kantarawaddytimes.org/"
#kantarawaddytimes(browser,url,cursor,db)
#print("-------------------------kantarawaddytimes completed-------------------------")

#print("-------------------------kicnews running-------------------------")
####################22#########################
#from kicnews_main import kicnews_main
#url = "http://kicnews.org/"  
#kicnews_main(browser,url,cursor,db)
#print("-------------------------kicnews completed-------------------------")

#print("-------------------------mizzima running-------------------------")
####################23#########################
#from mizzima_main import mizzima_main
#url = "http://www.mizzima.com/"
#mizzima_main(browser,url,cursor,db)
#print("-------------------------mizzima completed-------------------------")

#print("-------------------------mizzimaburmese running-------------------------")
####################24#########################
#from myanmar_mizzima_main import myanmar_mizzima_main
#url = "http://www.mizzimaburmese.com/"
#myanmar_mizzima_main(browser,url,cursor,db)
#print("-------------------------mizzimaburmese completed-------------------------")

#print("-------------------------nmg-news running-------------------------")
####################25#########################
#from nmg_main import nmg_main
#url = "http://www.nmg-news.com/"
#nmg_main(browser,url,cursor,db)
#print("-------------------------nmg-news completed-------------------------")

#print("-------------------------burmese rfa running-------------------------")
####################26#########################
#from rfa_main import rfa_main
#url = "https://www.rfa.org/burmese/"
#category_url = "https://www.rfa.org/burmese/news/story_archive?b_start:int="
#rfa_main(browser,url,cursor,db,category_url)
#print("-------------------------burmese rfa completed-------------------------")

#print("-------------------------rfa running-------------------------")
####################27########################
#from rfa_main import rfa_main
#url = 'https://www.rfa.org/english/news/myanmar'
#category_url = "https://www.rfa.org/english/news/myanmar/story_archive?b_start:int="
#rfa_main(browser,url,cursor,db,category_url)
#print("-------------------------rfa completed-------------------------")

print("-------------------------thanlwintimes running-------------------------")
####################28#########################
from thanlwintimes import thanlwintimes
url = "http://thanlwintimes.com/"
thanlwintimes(browser,url,cursor,db)
print("-------------------------thanlwintimes completed-------------------------")

#print("-------------------------twitter running-------------------------")
#####################29#########################
#from model_for_political_database_twitter import twitter_wrapper
#url ="https://twitter.com/arsa_official?lang=en"
#try:
#    twitter_wrapper(browser,url,cursor,db)
#except:
#    pass
#print("-------------------------twitter completed-------------------------")

#print("-------------------------google running-------------------------")
######################30#########################
#from google_news import google_news
#url = "https://news.google.com/search?q=BURMA&hl=en-IN&gl=IN&ceid=IN:en"
#google_news(browser,url,cursor,db,"BURMA")
#
#url = "https://news.google.com/search?q=myanmar&hl=en-IN&gl=IN&ceid=IN%3Aen"
#google_news(browser,url,cursor,db,"myanmar")
#
#url = "https://news.google.com/search?for=rohingya&hl=en-IN&gl=IN&ceid=IN%3Aen"
#google_news(browser,url,cursor,db,"rohingya")
#print("-------------------------google completed-------------------------")



#print("-------------------------myanmar.mmtimes running-------------------------")
######################27#########################
#url = "https://myanmar.mmtimes.com"
#from mmtimes_main import mmtimes_main
#mmtimes_main(browser,url,cursor,db)
#print("-------------------------myanmar.mmtimes completed-------------------------")

#print("-------------------------seniorgeneralminaunghlaing running-------------------------")
#
#####################29#########################
#from seniorgeneralminaunghlaing_main import se_main
#url = "https://www.seniorgeneralminaunghlaing.com.mm/en/Home/news/"
#se_main(browser,url,cursor,db)
#
#####################30#########################
#url = "https://www.seniorgeneralminaunghlaing.com.mm/Home/news/"
#se_main(browser,url,cursor,db)
#print("-------------------------seniorgeneralminaunghlaing completed-------------------------")


#print("-------------------------voanews running-------------------------")
#
#####################33#########################
#from voa_news_burmese_main import voa_main
#url = "https://burmese.voanews.com/"
#voa_main(browser,url,cursor,db)
#
######################34#########################
#from voa_news_main import voa_main
#url = "https://www.voanews.com/search?search_api_fulltext=burma"
#voa_main(browser,url,cursor,db)
#
######################35#########################
#from voa_news_main import voa_main
#url = "https://www.voanews.com/search?search_api_fulltext=myanmar"
#voa_main(browser,url,cursor,db)
#print("-------------------------voanews completed-------------------------")
#print("-------------------------news-eleven running-------------------------")
#
######################36#########################
#from news_eleven import news_eleven
#url = "https://news-eleven.com/"
#news_eleven(browser,url,cursor,db)
#print("-------------------------news-eleven completed-------------------------")
#print("-------------------------burma.irrawaddy running-------------------------")
#
######################37#########################
#from burmairrawaddy_main import burmairrawaddy_main
#url = "https://burma.irrawaddy.com/"
#burmairrawaddy_main(browser,url,cursor,db)
#print("-------------------------burma.irrawaddy completed-------------------------")
#print("-------------------------irrawaddy running-------------------------")
#
######################38#########################
#from irrawaddy_main import irrawaddy_main
#url = "https://www.irrawaddy.com/"
#irrawaddy_main(browser,url,cursor,db)
#print("-------------------------irrawaddy completed-------------------------")

#print("-------------------------7daydaily running-------------------------")
#
######################40######################### 
#from daydaily_main import daydaily_main
#url = "http://7daydaily.com/"
#daydaily_main(browser,url,cursor,db)
#print("-------------------------7daydaily completed-------------------------")
#print("-------------------------elevenmyanmar running-------------------------")
#
######################41#########################
#from model_for_political_database_elevenmyanmar import article_elevenmyanmar
#url = "https://elevenmyanmar.com"
#article_elevenmyanmar(browser,url,cursor,db)
#print("-------------------------elevenmyanmar completed-------------------------")
#print("-------------------------globalnewlightofmyanmar running-------------------------")
#
######################42#########################
#url = "http://www.globalnewlightofmyanmar.com"
#from model_for_political_database_globalnewlightofmynamar import article_globalnewlightofmyanmar
#article_globalnewlightofmyanmar(browser,url,cursor,db)
#print("-------------------------globalnewlightofmyanmar completed-------------------------")
#print("-------------------------mmtimes running-------------------------")
#
######################43#########################
#url = "http://www.mmtimes.com/"
#from mmtimes_main import mmtimes_main
#mmtimes_main(browser,url,cursor,db)
#print("-------------------------mmtimes completed-------------------------")
#
#########################visuals#################################
#from visualization_model import visuals
#visuals(cursor,db)
#
###################others_database (analysis models)#####################
#from upload_data_others import other_db
#other_db(cursor,db)'''