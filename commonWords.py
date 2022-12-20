import requests
from string import punctuation
from bs4 import BeautifulSoup
from collections import Counter

# url requests
request = requests.get("https://en.wikipedia.org/wiki/Elizabeth_II")
goodSoup = BeautifulSoup(request.content, 'html.parser')

# count words in paragraph
textParagraph = (''.join(s.findAll(text=True))for s in goodSoup.findAll('p'))
paragraphCounter = Counter((x.rstrip(punctuation).lower() for y in textParagraph for x in y.split()))

# count words from div container
textDivs = (''.join(s.findAll(text=True))for s in goodSoup.findAll('div'))
divsCounter = Counter((x.rstrip(punctuation).lower() for y in textDivs for x in y.split()))

# add counters together
totalWords = divsCounter + paragraphCounter
mostCommon_words = totalWords.most_common()

print(mostCommon_words)
