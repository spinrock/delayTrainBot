# encoding: utf-8

class User:
    userId = ''
    urlList = []

    def __init__(self, userId, urlList):
        self.userId = userId
        self.urlList = urlList

    def getUserId(self):
        return self.userId

    def getUrlList(self):
        return self.urlList


