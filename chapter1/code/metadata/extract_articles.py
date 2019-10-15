#!/usr/bin/env python
# -*- coding: utf-8 -*-

import newspaper

cnn_paper = newspaper.build('http://cnn.com')

print('*****************************category urls************************************\n')
for category in cnn_paper.category_urls():
	print(category)
	
print('*****************************url articles************************************\n')

for article in cnn_paper.articles:
	print(article.url)

print('*****************************download first article************************************\n')
cnn_article = cnn_paper.articles[0]
cnn_article.download()
cnn_article.parse()

#print(cnn_article.html)
print(cnn_article.text)
print(cnn_article.keywords)
print(cnn_article.summary)
print(cnn_article.authors)
print(cnn_article.publish_date)