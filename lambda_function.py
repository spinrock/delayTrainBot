# coding: utf-8

import json, os
from User import User
from postRequests import Message 


def lambda_handler(event, context):
	# PostMessage用のURL
	postUrl = event['postUrl']
	accessToken = event['accessToken']

	# ユーザリスト
	userList = []

	# jsonからのユーザ情報の取得
	for user in event['userList']:
		urlList = []
		for url in user['urlList']:
			urlList.append(url['url'])
		userList.append(User(user['userId'], urlList))

    # ユーザごとに必要な遅延情報を付与して送信
	for user in userList:
		message = Message(postUrl, accessToken)
		message.setData(user.getUserId(),*user.getUrlList())
		message.post()

	
	
