import json
from pprint import pprint
import operator


with open('news/newsafr.json') as news_file:
    articles = json.load(news_file)
    descriptions = ''
    articles = articles.get('rss').get('channel').get('item')

    for article in articles:
        descriptions += article.get('description').get('__cdata')
        word_list = descriptions.split()

    word_list = [x for x in word_list if (len(x) >= 6 and x.startswith('<')==False)]

    # pprint(word_list)
    #
    lsWord = {}
    for key in word_list:
        key = key.lower()
        if key in lsWord:
            value = lsWord[key]
            lsWord[key]=value+1
        else:
            lsWord[key]=1
    sorted_lsWord = sorted(lsWord.items(), key=operator.itemgetter(1))
    pprint(sorted_lsWord)
