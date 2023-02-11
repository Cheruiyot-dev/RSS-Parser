import feedparser

url = input('enter url link:')
# url = 'https://www.standardmedia.co.ke/rss/headlines.php'

# print(url)

d = feedparser.parse(url)
title = d['feed']['title']

try:
    print(title)

except:
    print('There is no source title')

for item in d['entries']:
    print(item['title'] + '\n' + item['description'] + '\n' + item['link'])
