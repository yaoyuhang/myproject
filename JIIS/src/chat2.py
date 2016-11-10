'''
Created on 2016/10/18

@author: yaoyuhang
'''
import itchat

@itchat.msg_register(itchat.content.TEXT,isGroupChat=True)
def text_reply(msg):
    itchat.send(msg['Text'], msg['FromUserName'])
    print(msg['Text'])
    infoDict = itchat.search_friends(msg['FromUserName'])
    print(infoDict.__name__)

itchat.auto_login(True)
itchat.run()