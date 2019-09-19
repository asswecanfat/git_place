from collections import deque
import random


graph = {}
graph['开始'] = ['起床']
graph['起床'] = ['洗澡', '刷牙']
graph['刷牙'] = ['吃早餐', '洗澡']
graph['洗澡'] = ['吃早餐']
graph['吃早餐'] = ['洗澡']

need_to_do = deque()
need_to_do += graph['开始']
check_thing = []
update = 0
while need_to_do:
    one_thing = need_to_do.popleft()
    if one_thing not in check_thing:
        need_to_do += random.sample(graph[one_thing], len(graph[one_thing]))
        check_thing.append(one_thing)
    elif update != 1:
        check_thing.remove(one_thing)
        check_thing.append(one_thing)
        update = 1
print(check_thing)