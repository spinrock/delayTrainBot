# coding: utf-8

import urllib
from bs4 import BeautifulSoup

class DelayInfo:
	train = ''
	statement = ''
	update = ''

	def __init__(self,url):
		html = urllib.request.urlopen(url).read()
		soup = BeautifulSoup(html, 'html.parser')
		delayInfo = soup.find('div', {'id': 'mdServiceStatus'})
		labelInfo = soup.find('div', {'class': 'labelLarge'})
		self.train = labelInfo.h1.find(text=True, recursive=False)
		self.statement = delayInfo.p.find(text=True, recursive=False)
		self.update = labelInfo.find('span', {'class': 'subText'}).find(text=True, recursive=False)

	def getInfo(self):
		delayInfo = self.train + ':' + self.statement + '(' + self.update + ')'
		return delayInfo