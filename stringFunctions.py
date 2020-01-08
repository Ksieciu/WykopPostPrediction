import morfeusz2


# func for getting pages urls(ex. urls from pages 1-7) and returning list of urls
def get_urls(page_url, starting_page, ending_page):
    urls = []
    for i in range(starting_page, ending_page + 1):
        url = page_url + str(i)
        urls.append(url)
    return urls


# func for creating string from list
def list_to_string(lst):
    toString = ' '.join([str(elem) for elem in lst])
    return toString


def lemmatize_words(lst):
    morf = morfeusz2.Morfeusz()
    lemmatized = []
    for word in lst:
        analysis = morf.analyse(word)
        token = analysis[0][2][1].split(':')[0]
        lemmatized.append(token)
    return lemmatized
