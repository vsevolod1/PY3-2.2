import json
from pprint import pprint
import operator

#функция для получения отсортированного списка
def sorted_list(word_list):
    word_list = [x for x in word_list if (len(x) >= 6
        and x.startswith('<')==False and x.startswith('href')==False)]

    lsWord = {}
    for key in word_list:
        key = key.lower()
        if key in lsWord:
            value = lsWord[key]
            lsWord[key]=value+1
        else:
            lsWord[key]=1

    sorted_lsWord = sorted(lsWord.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_lsWord;

#функция для вывода результата
def print_result (word_list, i):
    i=int(i)
    j = 0
    print('––––––––––––')
    print('Топ-{} слов и частота их употребления:'.format(i))
    while j < i:
        print('{} - {}'.format(sorted_list(word_list)[j][0], sorted_list(word_list)[j][1]))
        j += 1
    print('––––––––––––')

#функция для вывода данных из указанного файла
def top_words (filename, encode, top_num):
    with open(filename, encoding=encode) as news_file:
        articles = json.load(news_file)
        descriptions = ''
        if type(articles.get('rss').get('channel').get('item')[0].get('description')) is dict:
            articles = articles.get('rss').get('channel').get('item')

            for article in articles:
                descriptions += article.get('description').get('__cdata')
                word_list = descriptions.split()

            print_result(word_list, top_num)

        elif type(articles.get('rss').get('channel').get('item')[0].get('description')) is str:

            articles = articles.get('rss').get('channel').get('item')

            for article in articles:
                descriptions += article.get('description')
                word_list = descriptions.split()

            print_result(word_list, top_num)

#вывод необходимых списков
input1 = ''
while input1.lower() != 'q':
    input1 = input('Выберите страну:\n1 - Африка\n2 - Кипр\n3 - Франция\n4 - Италия\nq - выйти\n')
    if input1.lower() == 'q':
        break
    input2 = input('Введите количество слов в топе: ')
    if input1 == '1':
        top_words('news/newsafr.json', 'utf-8', input2)
    if input1 == '2':
        top_words('news/newscy.json', 'koi8-r', input2)
    if input1 == '3':
        top_words('news/newsfr.json', 'iso 8859-5', input2)
    if input1 == '4':
        top_words('news/newsit.json', 'windows 1251', input2)
