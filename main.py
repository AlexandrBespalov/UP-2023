import feedparser
import csv
import pandas as pd
import re

from tkinter import *

our_feeds = {'RBC': 'https://rssexport.rbc.ru/rbcnews/news/30/full.rss'}

f_all_news = 'allnews.csv' 


def check_url(url_feed): #функция получает линк на rss ленту, возвращает распаршенную ленту с помощью feedpaeser
    return feedparser.parse(url_feed)  
    
def getHeadlines(url_feed): #функция для получения заголовков новости
    category = []
    lenta = check_url (url_feed)
    for item_of_news in lenta['items']:
        category.append(item_of_news ['category'])
    return category

def getTitles(url_feed): #функция для получения ссылки на источник новости
    link = []
    lenta = check_url(url_feed)
    for item_of_news in lenta['items']:
        link.append(item_of_news ['title'])
    return link

def getDates(url_feed): #функция для получения даты публикации новости
    pubDate = []
    lenta = check_url(url_feed)

    for item_of_news in lenta['items']:
        pubDate.append(item_of_news ['published'])
    return pubDate



allheadlines = []
alltitles = []
alldates = []

#Прогоняем наши URL и добавляем их в пустые списки
for key,url in our_feeds.items():
    allheadlines.extend( getHeadlines(url) )
    
for key,url in our_feeds.items():
    alltitles.extend( getTitles(url) )
    
for key,url in our_feeds.items():
    alldates.extend( getDates(url) )



def write_all_news(all_news_filepath): #функция для записи всех новостей в .csv, возвращает нам этот датасет
    header = ['Category',' Title',' Publication Date'] 

    with open(all_news_filepath, 'w', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')

        writer.writerow(i for i in header)

        for a,b,c  in zip(allheadlines, alltitles, alldates):
            writer.writerow((a,b,c))
        print(all_news_filepath)

        # df = pd.read_csv(all_news_filepath) #рудиментарная штука


    with open(all_news_filepath, 'r', encoding='utf-8-sig') as csv_file:
        df = pd.read_csv(csv_file, na_filter=False)

        return df

# #функция для поиска, а затем записи определенных новостей по таргету, затем возвращает этот датасет
# def looking_for_certain_news(all_news_filepath, certain_news_filepath, target1, target2):
#     df = pd.read_csv(all_news_filepath)
    
#     result = df.apply(lambda x: x.str.contains(target1, na=False,
#                                     flags = re.IGNORECASE, regex=True)).any(axis=1)
#     result2 = df.apply(lambda x: x.str.contains(target2, na=False,
#                                     flags = re.IGNORECASE, regex=True)).any(axis=1)
#     new_df = df[result&result2]
        
#     new_df.to_csv(certain_news_filepath
#                      ,sep = '\t', encoding='utf-8-sig')
        
#     return new_df

write_all_news(f_all_news) #все новости


#GUI
root = Tk()

def btn_click():
    k = Input.get()
    error = True
 
    with open('allnews.csv', 'r', encoding='utf-8-sig') as csvfile:
        for i in csvfile.readlines():
            if k in i:
                print(i)
                error = False
        if error:
            print('Ошибка, новости не найдены.')


root.title('Get news from')
root.geometry('300x250')

root.resizable(width=False, height=False)

Canvas = Canvas(root, height=300, width=250)
Canvas.pack()

frame = Frame(root)
frame.place(relx = 0.15, rely = 0.15, relwidth = 0.7, relheight = 0.7)

title = Label(frame, text='Ввод темы', font='18')
title.pack(anchor=N)

Input = Entry(frame, bg='white')
Input.pack(anchor=CENTER)

btn = Button(frame, text = 'Запросить', bg='#5991ff', command=btn_click)
btn.pack(anchor=S)
 
root.mainloop()