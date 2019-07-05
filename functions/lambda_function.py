# coding: utf-8

import json, os
import boto3
from base64 import b64decode

from DelayInfo import DelayInfo
from PostRequest import Message

def lambda_handler(event, context):
    # TODO implement

    # 変数宣言
    postUrl = ""
    postChannel = ""
    urlList = []

    # 環境変数から情報取得(復号化)
    ENCRYPTED = os.environ['postUrl']
    postUrl = boto3.client('kms').decrypt(CiphertextBlob=b64decode(ENCRYPTED))['Plaintext']

    ENCRYPTED = os.environ['postChannel']
    postChannel = boto3.client('kms').decrypt(CiphertextBlob=b64decode(ENCRYPTED))['Plaintext']

    # jsonからの路線情報の取得
    for url in event['urlList']:
        urlList.append(url['url'])        

    # メイン処理
    # 路線ごとに遅延情報を取得し、遅延があればSlack通知
    message = Message(postUrl)
    for trainUrl in urlList:
        delayInfo = DelayInfo(trainUrl)
        if  "現在､事故･遅延に関する情報はありません。" not in delayInfo.getInfo() :
            message.setData(delayInfo.getInfo(), 'delayTrainBot', postChannel)
            message.post()

    return {
        'statusCode': 200,
        'body': json.dumps('Post Complete!')
    }