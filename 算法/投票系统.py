def check_vote(hash_list, name):
    if hash_list.get(name):
        print('此人已投票')
    else:
        hash_list[name] = True
        print('{}{}'.format(name, '投票成功'))


hash_list = {}
check_vote(hash_list, 'Tim')