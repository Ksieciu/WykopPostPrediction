from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import re


# func for checking if the word is actually a word, not some meme face or trash
def is_polish_word(word):
    letters = " aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż"
    check = True
    for l in word:
        if l not in letters:
            check = False
    return check



def crawl_hot(urls, words_list, words_check):

    for url in urls:
        result = requests.get(url)
        # print(result.status_code)
        content = result.content
        soup = BeautifulSoup(content, 'lxml')
        hot = True

        # checking if content is in hot pages - if not changing to False
        if int(url.split('/')[-1]) > 15:
            hot = False

        # saving data to file using with - we can remove it later, just testing purpose
        with open("testData.txt", "a+", encoding='utf-8') as file:
            # looking for div class "wblock lcontrast dC" content - takes post and comments
            for n in soup.find_all(class_='wblock lcontrast dC'):
                # post has unique data-type="entry", so we remove comments by skipping
                # them. Then we save hashtags into arr and erase them and after that we remove
                # all other trash data so we have only raw post content now to work on
                if 'data-type="entry"' not in str(n):
                    continue

                # saving hashtags to array and then removing from post data
                for hashTag in n.find_all(class_='showTagSummary'):
                    print(hashTag.text)  # add tags to arr
                    hashTag.decompose()

                # removing trash data
                for link in (n.find_all('a') or n.find_all(class_='show-more')
                             or n.find_all('span', class_='')
                             or n.find_all(class_='affect')):
                    link.decompose()

                for moreTrash in n.find_all(class_='author ellipsis'):
                    moreTrash.decompose()

                for mediaContent in n.find_all(class_='media-content'):
                    mediaContent.decompose()
                    # ADD 1 or 0 to arr 'if had picture'
                # for span in n.find_all('span', class_=''):
                #     span.decompose()

                text = n.get_text()
                # text = str(n)

                rawText = ''.join([x for x in text if x.isalpha() or x.isspace()])
                # rawText = ''.join([x for x in text if is_polish_letter(x)]) #boop chuja jest błędów sporo
                # for elem in rawText:
                #     if is_polish_word(elem) is False:
                #         rawText.remove(elem)

                words = rawText.lower().split()
                # words = re.split(' \n', rawText.lower())
                for word in words:
                    if len(word) < 2:
                        continue
                    words_list.append(word)
                file.write(rawText)


# func for getting pages urls(ex. urls from pages 1-7) and returning list of urls
def get_urls(page_url, starting_page, ending_page):
    urls = []
    for i in range(starting_page, ending_page+1):
        url = page_url + str(i)
        urls.append(url)
    return urls


# urls = get_urls('https://www.wykop.pl/mikroblog/hot/ostatnie/24/strona/', 1, 5)
# crawl_hot(urls)
