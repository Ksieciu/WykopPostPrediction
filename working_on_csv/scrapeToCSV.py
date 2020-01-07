from bs4 import BeautifulSoup
import requests
import csv
import morfeusz2


# https://www.wykop.pl/mikroblog/hot/ostatnie/24/strona/
# getting content from pages
def crawl_hot(urls, file_name):
    for url in urls:
        result = requests.get(url)
        # print(result.status_code)
        content = result.content
        soup = BeautifulSoup(content, 'lxml')
        label = 1
        page = ''
        for x in url[-2:]:
            for y in x:
                if y.isdigit():
                    page = page + y

        if int(page) >= 10:
            label = 0
        else:
            label = 1

        # saving data to file using with - we can remove it later, just testing purpose
        # klasa do otwierania i pracowania na otwartym tekście
        with open(file_name, "a+", encoding='utf-8', newline='') as file:
            # looking for div class "wblock lcontrast dC" content - takes post and comments
            writer = csv.writer(file)
            writer.writerow(["post", "words", "words_count", "hashtags",
                             "hashtags_count", "label"])

            for n in soup.find_all(class_='wblock lcontrast dC'):
                act_post = []
                hashtags = []
                words = []
                hashtags_len = 0
                # post has unique data-type="entry", so we remove comments by skipping
                # them. Then we save hashtags into arr and erase them and after that we remove
                # all other trash data so we have only raw post content now to work on
                if 'data-type="entry"' not in str(n):
                    continue

                # saving hashtags to array and then removing from post data
                for hashTag in n.find_all(class_='showTagSummary'):
                    hashtags.append(hashTag.get_text())  # add tags to arr
                    hashTag.decompose()
                hashtags_len = len(hashtags)
                hashtags_str = list_to_string(hashtags)

                # removing trash data
                for link in (n.find_all('a') or n.find_all(class_='show-more')
                             or n.find_all('span', class_='')
                             or n.find_all(class_='affect')):
                    link.decompose()

                for moreTrash in n.find_all(class_='author ellipsis'):
                    moreTrash.decompose()

                for mediaContent in n.find_all(class_='media-content'):
                    mediaContent.decompose()

                # for span in n.find_all('span', class_=''):
                #     span.decompose()

                text = n.get_text()

                raw_text = ''
                raw_text = ''.join([x for x in text if x.isalpha() or x.isspace()])

                words = raw_text.lower().split()
                words_len = 0

                for word in words:
                    if len(word) > 2:
                        act_post.append(word)

                words_len = len(act_post)
                words_str = list_to_string(act_post)

                writer.writerow([raw_text, words_str, words_len, hashtags_str, hashtags_len, label])


# func for getting pages urls(ex. urls from pages 1-7) and returning list of urls
def get_urls(page_url, starting_page, ending_page):
    urls = []
    for i in range(starting_page, ending_page + 1):
        url = page_url + str(i)
        urls.append(url)
    return urls


def list_to_string(lst):
    toString = ' '.join([str(elem) for elem in lst])
    return toString





urls = get_urls('https://www.wykop.pl/mikroblog/hot/ostatnie/24/strona/', 1, 20)
crawl_hot(urls, "csvData.csv")
