# -*- coding: utf-8 -*-
'''
Created on 2016/10/18

@author: yaoyuhang
'''

#import re
import itchat
#import codecs
#from distutils.tests.setuptools_build_ext import if_dl

@itchat.msg_register(itchat.content.TEXT,isGroupChat=True)
def text_reply(msg):
#    itchat.send(msg['Text'], msg['FromUserName'])
#    print(msg['Text'])
    infoDict = itchat.search_friends(msg['ActualNickName'])
    print(infoDict)
    print(msg['FromUserName'])
    j = itchat.get_batch_contract(msg['FromUserName'])
    chatlog =j['NickName'] + '@' + msg['ActualNickName'] + '---' + msg['Text'] + '\n'
    print(chatlog)
    # Test user
    if msg['ActualNickName'] in ['ITJapan' , 'youkou']:
        itchat.send(msg['Text'], msg['FromUserName'])
    elif j['NickName'] in [u'（测试）IT直接案件群',u'日本IT直接案件平台']:
        logFile = open('chatlog.txt','a')
        logFile.write(chatlog.encode("utf-8"))
        print('save file is ok')        

itchat.auto_login()
itchat.run()