# coding: utf-8

import requests

class Message:
    postUrl = ''
    postHeaders = {}
    postData = ''

    def __init__(self, postUrl, accessToken):
        self.postUrl = postUrl
        self.postHeaders = {'Content-Type': 'application/json',
                        'Authorization': 'Bearer {' + accessToken + '}'}
        self.postData = ''

    def setData(self, to, texts):
        self.postData = '{"to": "' + to + '", "messages":[' 
        for text in texts:
            self.postData = self.postData + '{"type":"text","text":"' + text + '"},' 
        self.postData = self.postData[:-1] + ']}'
        self.postData = self.postData


    def getData(self):
        return self.postData

    def post(self):
        requests.post(self.postUrl, data=self.postData.encode('utf-8'), headers=self.postHeaders)

