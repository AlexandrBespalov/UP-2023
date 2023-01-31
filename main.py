import feedparser
import csv
import pandas as pd
import re

our_feeds = {'RBC': 'https://rssexport.rbc.ru/rbcnews/news/30/full.rss'}

f_all_news = 'allnews23march.csv' 
f_certain_news = 'certainnews23march.csv'

vector1 = 'ДолЛАР|РубЛ|ЕвРО' #таргеты по ключевым словам
vector2 = 'ЦБ|СбЕРбАНК|курс'



def check_url(url_feed): #функция получает линк на rss ленту, возвращает распаршенную ленту с помощью feedpaeser
    return feedparser.parse(url_feed)  
    
def getHeadlines(url_feed): #функция для получения заголовков новости
    category = []
    lenta = check_url (url_feed)
    for item_of_news in lenta['items']:
        category.append(item_of_news ['category'])
    return category

def getLinks(url_feed): #функция для получения ссылки на источник новости
    link = []
    lenta = check_url(url_feed)
    for item_of_news in lenta['items']:
        link.append(item_of_news ['link'])
    return link

def getDates(url_feed): #функция для получения даты публикации новости
    pubDate = []
    lenta = check_url(url_feed)
    for item_of_news in lenta['items']:
        pubDate.append(item_of_news ['pubDate'])
    return pubDate



allheadlines = []
alllinks = []
alldates = []

# Прогоняем наши URL и добавляем их в пустые списки
for key,url in our_feeds.items():
    allheadlines.extend( getHeadlines(url) )
    
for key,url in our_feeds.items():
    alllinks.extend( getLinks(url) )
    
for key,url in our_feeds.items():
    alldates.extend( getDates(url) )



def write_all_news(all_news_filepath): #функция для записи всех новостей в .csv, возвращает нам этот датасет
    header = ['Title','Description','Links','Publication Date'] 

    with open(all_news_filepath, 'w', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')

        writer.writerow(i for i in header) 

        for a,b,c,d  in zip(allheadlines, alllinks, alldates):
            writer.writerow((a,b,c,d))

        df = pd.read_csv(all_news_filepath)
            
    return df



#функция для поиска, а затем записи определенных новостей по таргету, затем возвращает этот датасет
def looking_for_certain_news(all_news_filepath, certain_news_filepath, target1, target2):
    df = pd.read_csv(all_news_filepath)
    
    result = df.apply(lambda x: x.str.contains(target1, na=False,
                                    flags = re.IGNORECASE, regex=True)).any(axis=1)
    result2 = df.apply(lambda x: x.str.contains(target2, na=False,
                                    flags = re.IGNORECASE, regex=True)).any(axis=1)
    new_df = df[result&result2]
        
    new_df.to_csv(certain_news_filepath
                     ,sep = '\t', encoding='utf-8-sig')
        
    return new_df



write_all_news(f_all_news) #все новости