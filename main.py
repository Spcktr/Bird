import random
import time


from lxml.html import fromstring
import nltk
nltk.download('punkt')
import requests

from twitter import OAuth, Twitter


import creds

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

oauth = OAuth(
        creds.ACCESS_TOKEN,
        creds.ACCESS_SECRET,
        creds.CONSUMER_KEY,
        creds.CONSUMER_SECRET
    )
t = Twitter(auth=oauth)

HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0)'
                      ' Gecko/20100101 Firefox/66.0'
        }


def extract_paratext(paras):
    """Extracts text from <p> elements and returns a clean, tokenized random
    paragraph."""

    paras = [para.text_content() for para in paras if para.text_content()]
    para = random.choice(paras)
    return tokenizer.tokenize(para)


def extract_text(para):
    """Returns a sufficiently-large random text from a tokenized paragraph,
    if such text exists. Otherwise, returns None."""

    for _ in range(10):
        text = random.choice(para)
        if text and 60 < len(text) < 210:
            return text

    return None


def scrape_coursera():
    """Scrapes content from the Coursera blog."""
    url = 'https://blog.coursera.org'
    r = requests.get(url, headers=HEADERS)
    tree = fromstring(r.content)
    links = tree.xpath('//div[@class="recent"]//div[@class="title"]/a/@href')

    for link in links:
        r = requests.get(link, headers=HEADERS)
        blog_tree = fromstring(r.content)
        paras = blog_tree.xpath('//div[@class="entry-content"]/p')
        para = extract_paratext(paras)
        text = extract_text(para)
        if not text:
            continue

        yield '"%s" %s' % (text, link)


def scrape_thenewstack():
    """Scrapes news from thenewstack.io"""

    r = requests.get('https://thenewstack.io', verify=False)

    tree = fromstring(r.content)
    links = tree.xpath('//div[@class="normalstory-box"]/header/h2/a/@href')

    for link in links:
        r = requests.get(link, verify=False)
        tree = fromstring(r.content)
        paras = tree.xpath('//div[@class="post-content"]/p')
        para = extract_paratext(paras)
        text = extract_text(para)
        if not text:
            continue

        yield '"%s" %s' % (text, link)


def main():
    """Encompasses the main loop of the bot."""
    print('Bot started.')
    news_funcs = ['scrape_coursera', 'scrape_thenewstack']
    news_iterators = []
    for func in news_funcs:
        news_iterators.append(globals()[func]())
    while True:
        for i, iterator in enumerate(news_iterators):
            try:
                tweet = next(iterator)
                t.statuses.update(status=tweet)
                print(tweet, end='\n')
                time.sleep(600)
            except StopIteration:
                news_iterators[i] = globals()[newsfuncs[i]]()


if __name__ == "__main__":
    main()
