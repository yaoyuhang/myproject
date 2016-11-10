# -*- coding: utf-8 -*-
#!/usr/bin/env python
import MeCab
import sys
import string
import re

keyLeave1 = [u'電話番号',u'メール',u'言語',u'日本語',u'スキル',
u'勤務先',u'勤務時間',u'時期',u'単価',u'案件名',u'作業内容',u'作業場所',u'作業時期',
u'募集人数',u'商流']

keyLanguage=[u'C++',u'C#',u'ASP.net',u'java',u'iOS',u'intramart',u'javascript',u'jsp',
u'ajax',u'json',u'jquery',u'css',u'Struts', u'Hibernate',u'css',u'sql',
u'cobol',u'VB.net',u'VB',u'ruby',u'saleforce',u'Domino',u'notes',u'Delphi',
u'Android',u'Excel/Accessマクロ',u'Swift',u'Objective-C',u'Xcode',u'CoreData',
u'SQLite',u'HTML5',u'LISP',u'JSF',u'mybatis']

mailPattern = r'[\w.-]+@[\w.-]+'
phonePattern1 = r'''(\d{3})\D*(\d{3})\D*(\d{4})'''
phonePattern2 = r'''(\d{3})\D*(\d{4})\D*(\d{4})'''

key1IndexList = []
key1List = []
languageList = []
mailList = []
phoneList = []

logFile = open('chatlog2.txt', 'r')

t = MeCab.Tagger (" ".join(sys.argv))

for line in logFile:
    #mailAddress
    mailMatch = re.search(mailPattern, line)
    if mailMatch:
        mailList.append(mailMatch.group())
    #phoneNumber
    phonePattern = re.compile(phonePattern1, re.VERBOSE)
    phoneMatch = phonePattern.search(line)
    if phoneMatch:
        phoneList.append(phoneMatch.groups())
        
    phonePattern = re.compile(phonePattern2, re.VERBOSE)
    phoneMatch = phonePattern.search(line)
    if phoneMatch:
        phoneList.append(phoneMatch.groups())    
    #
    m = t.parseToNode(line)
    while m:
        key = m.surface.decode('utf-8')
        #print key
        #str = u'日本語'
        #print m.surface
        #キーワード判断
        if key in keyLeave1:
            index = line.decode('utf-8').find(key)
            key1IndexList.append(index)
            key1List.append(key)
        #開発言語判断
        if key.lower() in keyLanguage:
            languageList.append(key)
        m = m.next
    #for key in keyLeave1:
    #    index = line.decode('utf-8').find(key)
    #    if index > 0:
    #        key1IndexList.append(index)
    #        key1List.append(key)
    if len(key1IndexList) > 0:
#        print line,
        i = 0
        for k in key1List:
            start = key1IndexList[i]
            end = len(line.decode('utf-8'))
            if i+1 < len(key1IndexList):
                end = key1IndexList[i+1]
#            print k + ':' + line.decode('utf-8')[start:end]
            i = i + 1
#    if len(languageList) > 0:
#        print languageList
    if len(mailList) >0:
        print line
        print mailList[0]
    if len(phoneList) > 0:
        print line
        print phoneList[0][0] + phoneList[0][1] + phoneList[0][2]
    key1IndexList = []
    key1List = []
    languageList = []
    phoneList = []
    mailList = []
logFile.close()