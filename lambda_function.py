# coding: utf-8

import json, os
import boto3
from base64 import b64decode

from User import User
from DelayInfo import DelayInfo
from PostRequest import Message

def lambda_handler(event, context):
    # TODO implement

    # 変数宣言
    accessToken = ""
    postUrl = ""
    userList = []
    messageList = []
    
    # 環境変数から情報取得(復号化)
    ENCRYPTED = os.environ['accessToken']
    accessToken = boto3.client('kms').decrypt(CiphertextBlob=b64decode(ENCRYPTED))['Plaintext']
    
    ENCRYPTED = os.environ['postUrl']
    postUrl = boto3.client('kms').decrypt(CiphertextBlob=b64decode(ENCRYPTED))['Plaintext']
    
    # jsonからのユーザ情報の取得
    for user in event['userList']:
        urlList = []
        print(user)
        for url in user['urlList']:
            urlList.append(url['url'])
        userList.append(User(user['userId'], urlList))
    
    # メイン処理
    # 路線ごとに遅延情報を取得し、遅延があればユーザにライン通知
    
    for user in userList:
        messageList = []
        message = Message(postUrl.decode(), accessToken.decode())
        for trainUrl in user.getUrlList():
            delayInfo = DelayInfo(trainUrl)
            if  "現在､事故･遅延に関する情報はありません。" not in delayInfo.getInfo() :
                messageList.append(delayInfo.getInfo())
        message.setData(user.getUserId(), messageList)
        message.post()
    

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }