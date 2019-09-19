# 关系图
'''********************************************
   **   我：爸，妈，同学                     **
   **   爸：父亲，母亲                       **
   **   妈：父亲_，母亲_                     **
   **   同学：啊爸，啊妈，主人公             **
   ********************************************'''

# 用到队列，即collection类的queue

from collections import deque


graph = {}
graph['me'] = ['爸', '妈', '同学']
graph['爸'] = ['父亲', '母亲']
graph['妈'] = ['父亲_', '母亲_']
graph['同学'] = ['啊爸', '啊妈', 'me']
graph['父亲'] = []
graph['母亲'] = []
graph['父亲_'] = []
graph['母亲_'] = []
graph['啊爸'] = []
graph['啊妈'] = []  # 关系图构建完毕


def near_friend_get(me):
    # 创建空队列
    search_queue = deque()
    search_queue += graph[me]
    while search_queue:
        person = search_queue.popleft()  # 第一个人
        if person in graph[me]:
            search_queue += graph[person]
        else:
            print('{}{}'.format('你可能认识的人:', person))

while 1:
    me = input('请输入人物：')
    near_friend_get(me)