# coding: utf-8
# Slack の Webhookを利用してメッセージを投稿できるクラス

import requests

class Message:
    postUrl = ''
    postData = ''

    def __init__(self):
        self.postUrl = ''
        self.postData = ''

    def __init__(self, postUrl):
        self.postUrl = postUrl
        self.postData = ''

    def setUrl(self, postUrl):
        self.postUrl = postUrl
        
    def setData(self, text, userName, channelName):
        self.postData = '{"text": "' + text + \
            '", "username": "' + userName + \
            '", "channel": "' + channelName + \
            '"}'

    def getUrl(self):
        return self.postUrl

    def getData(self):
        return self.postData

    def post(self):
        requests.post(self.postUrl, data=self.postData.encode('utf-8'))

