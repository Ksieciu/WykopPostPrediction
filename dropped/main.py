from funcBackup import get_urls, crawl_hot

words = []
check = []


urls = get_urls('https://www.wykop.pl/mikroblog/hot/ostatnie/24/strona/', 1, 5)
crawl_hot(urls, words, check)

print(words)
