import morfeusz2


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


def get_label(url):
    page = ''
    for x in url[-2:]:
        for y in x:
            if y.isdigit():
                page = page + y
    if int(page) >= 10:
        return 0
    else:
        return 1


def get_clear_text(n):
    act_post = []
    hashtags = []
    words = []
    hashtags_len = 0
    # post has unique data-type="entry", so we remove comments by skipping
    # them. Then we save hashtags into arr and erase them and after that we remove
    # all other trash data so we have only raw post content now to work on


    # saving hashtags to array and then removing from post data
    for hashTag in n.find_all(class_='showTagSummary'):
        hashtags.append(hashTag.get_text())  # add tags to arr
        hashTag.decompose()
    hashtags_len = len(hashtags)
    hashtags_str = list_to_string(hashtags)

    # removing trash data and getting data to text
    text = decomposing(n).get_text()

    # saving to raw_text prepared taxt with only words and spaces
    raw_text = ''
    raw_text = (''.join([x for x in text if x.isalpha() or x.isspace()])).strip()


    # making all letters lowercases and adding them to words list
    words = raw_text.lower().split()
    words_len = 0

    # saving to act_post only words that are at least 3 chars long
    for word in words:
        if len(word) > 2:
            act_post.append(word)

    lemmatized = lemmatize_words(act_post)
    words_len = len(act_post)
    words_str = list_to_string(lemmatized)
    return raw_text, words_str, words_len, hashtags_str, hashtags_len


def decomposing(n):
    for link in (n.find_all('a') or n.find_all(class_='show-more')
                 or n.find_all('span', class_='')
                 or n.find_all(class_='affect')):
        link.decompose()

    for moreTrash in n.find_all(class_='author ellipsis'):
        moreTrash.decompose()

    for mediaContent in n.find_all(class_='media-content'):
        mediaContent.decompose()

    return n
