import json
import operator
import re


# функция для получения отсортированного списка
def sorted_list(words_list):
    # очистка от html-тегов и лишних символов
    for num, word in enumerate(words_list):
        word = re.sub('<[^<]+?>', '', word)
        word = re.sub('[^А-Яа-яA-Za-z]', '', word)
        words_list[num] = word

    # отбор слов, размер которых не меньше 6
    words_list = [x for x in words_list if (len(x) >= 6 and not x.startswith('href'))]

    # подведение статистики
    ls_word = {}
    for key in words_list:
        key = key.lower()
        if key in ls_word:
            value = ls_word[key]
            ls_word[key] = value + 1
        else:
            ls_word[key] = 1

    # сортировка и вывод
    sorted_ls_word = sorted(ls_word.items(), key=operator.itemgetter(1), reverse=True)
    # print(sorted_ls_word)
    return sorted_ls_word


# функция для вывода результата
def print_result(word_list, i):
    i = int(i)
    print('––––––––––––')
    print('Топ-{} слов и частота их употребления:'.format(i))
    for num in range(0, i):
        print('{} - {}'.format(sorted_list(word_list)[num][0], sorted_list(word_list)[num][1]))
    print('––––––––––––')


# функция для вывода данных из указанного файла
def top_words(filename, encode, top_num):
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

# вывод необходимых списков
input1 = ''
while input1.lower() != 'q':
    input1 = input('Выберите страну:\n1 - Африка\n2 - Кипр\n3 - Франция\n4 - Италия\nq - выйти\n')
    if input1.lower() == 'q':
        break
    input2 = input('Введите количество слов в топе: ')
    if input1 == '1':
        top_words('./news/newsafr.json', 'utf-8', input2)
    if input1 == '2':
        top_words('news/newscy.json', 'koi8-r', input2)
    if input1 == '3':
        top_words('news/newsfr.json', 'iso 8859-5', input2)
    if input1 == '4':
        top_words('news/newsit.json', 'windows 1251', input2)
