import itchat

itchat.auto_login(hotReload=True)


friends = itchat.get_friends(update=True)[0:]
ch = itchat.get_chatrooms(update=True)[0:]
for i in ch:
    '''if i['NickName'] == '':
       #fr = i['UserName']
       #break'''
    if i['NickName'] == '来比激光雨':
        chn = i['UserName']

#itchat.send(u'[python3]测试',toUserName=fr)
itchat.send(u'[python3]测试',toUserName=chn)