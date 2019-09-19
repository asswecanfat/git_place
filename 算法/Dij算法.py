# 需要三个字典
# 第一个字典，实现图
graph = {}

graph['start'] = {}
graph['start']['a'] = 5
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['c'] = 4
graph['a']['d'] = 2

graph['b'] = {}
graph['b']['a'] = 8
graph['b']['d'] = 7

graph['c'] = {}
graph['c']['d'] = 6
graph['c']['fin'] = 3

graph['d'] = {}
graph['d']['fin'] = 1

graph['fin'] = {}
# 第二个字典,储存每个节点开销
infinity = float('inf')
costs = {}
costs['a'] = 5
costs['b'] = 2
costs['c'] = infinity
costs['d'] = infinity
costs['fin'] = infinity
# 第三个字典,储存父节点
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['c'] = None
parents['d'] = None
parents['fin'] = None

check_list = []


def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for n in costs:
        cost = costs[n]
        if cost < lowest_cost and n not in check_list:
            lowest_cost = cost
            lowest_cost_node = n
    return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors:
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    check_list.append(node)
    node = find_lowest_cost_node(costs)

print(costs['fin'])
print(parents)

def catch_road():
    tong = []
    for i in parents:
        if i == 'fin':
            e = i
            next_ = parents[e]
            tong.append(e)
            tong.append(next_)
            while next_ != 'start':
                e = parents[next_]
                next_ = parents[e]
                tong.append(e)
                tong.append(next_)
    return tong
tong = catch_road()
i = 1
while 1:
    if tong[-i] == 'fin':
        print('fin')
        break
    else:
        print('{}{}'.format(tong.pop(), '-->'), end='')
