# 1
import datetime as DT
def busyHolidays(shoppers, orders, leadTime):
    tformat = '%H:%M'
    d=dict() # {customer: (shoppers)}
    for x,customer in enumerate(orders):
        d[x]=list()
        customerEarliest = DT.datetime.strptime(customer[0],tformat)+DT.timedelta(minutes=leadTime[x])
        customerLatest = DT.datetime.strptime(customer[1],tformat)
        shpCount=0
        for shopper in shoppers:
            shopperEarliest = DT.datetime.strptime(shopper[0],tformat)+DT.timedelta(minutes=leadTime[x])
            shopperLatest = DT.datetime.strptime(shopper[1],tformat)
            #determine delivery window
            windowStart = max(customerEarliest,shopperEarliest)
            windowEnd = min(customerLatest,shopperLatest)
            #determine if can be delivered or not
            if windowEnd<windowStart:
                continue #cannot be delivered
            else:
                d[x].append(shopper)
                shpCount+=1
        #if 1:1 match remove shopper from customer pool
        if shpCount==1:
            shoppers.remove(d[x][0])
            del d[x]
        # if no valid shoppers return false
        elif shpCount==0:
            return False
    #match remaining shoppers and customers
    return dfs(shoppers,d)

def dfs(shopperList,d):
    if len(d)==0:
        return True
    for ok,ov in d.items(): #gets first item
        #dfs possible rem shoppers
        #pass updated dictionary, and updated list
        f=False
        updCustomerList=dict(d)
        del updCustomerList[ok]
        for shop in ov: #gets possible shoppers
            if shop in shopperList:
                updShopperList = list(shopperList)
                updShopperList.remove(shop)
                f=dfs(updShopperList,updCustomerList)
                if f:
                    break
        return f
    
# 2
# Flow maximization through bipartite graph
# https://en.wikipedia.org/wiki/Maximum_cardinality_matching
# https://www.youtube.com/watch?v=LdOnanfc5TM&list=PLDV1Zeh2NRsDj3NzHbbFIC58etjZhiGcG

X, Y, T = eval(dir()[0])
e = enumerate
n = lambda s: int(s[:2]) * 60 + int(s[3:])
S = len(X)
O = len(Y)
N = S + O + 2
y = N-2
z = N-1
A = [ [0] * N for _ in X * N ]

for i, (a, b) in e(X):
    A[y][i] = 1

    for j, (c, d) in e(Y, S):
        A[j][z] = 1
        A[i][j] = max(n(a), n(c)) + T[j-S] <= min(n(d), n(b))

def f(P, h, v):
    for t, w in e(A[h]):
        if w and {t} - v:
            P[t] = h
            v.add(t)
            f(P, t, v)

    return z in v
    
def g(t, l):
    if t != y:
        h = P[t]
        l = g(h, min(l, A[h][t]))
        A[h][t] -= l
        A[t][h] += l
    
    return l

P = {}
while f(P, y, {y}):
    O -= g(z, 99)

return O < 1


# import collections

# def busyHolidays(shoppers, orders, leadTime):
#     s_to_mn = lambda s: int(s[:2]) * 60 + int(s[3:]) # time to minutes
#     S = len(shoppers)
#     O = len(orders)
#     N = S + O + 2 # bipartite graph + source + sync
#     source = N-2
#     sync = N-1

#     A = [
#         [0] * N
#         for _ in range(N)
#     ]

#     # start shopper indeces at 0
#     for si, (sh_start, sh_end) in enumerate(shoppers):
#         # All shoppers have an edge from source to shopper with weight 1
#         A[source][si] = 1

#         # Start order indeces at `S`
#         for oi, (ord_start, ord_end) in enumerate(orders, S):
#             end_mn = max(s_to_mn(sh_start), s_to_mn(ord_start)) + leadTime[oi-S]
#             # All orders have an edge from order to sync with weight 1
#             A[oi][sync] = 1

#             # If this shopper can service this order, add an edge with a weight of 1
#             if end_mn <= s_to_mn(ord_end) and end_mn <= s_to_mn(sh_end):
#                 A[si][oi] = 1

#     def bfs(source, sync, parent, A):
#         parent[source] = -1
#         seen = {source}
#         q = collections.deque([source])

#         while q:
#             head = q.popleft()

#             for tail, val in enumerate(A[head]):
#                 if val > 0 and tail not in seen:
#                     parent[tail] = head
#                     seen.add(tail)
#                     q.append(tail)

#         return sync in seen

#     def edmonds_karp():
#         parent = [-1] * N
#         max_flow = 0

#         while bfs(source, sync, parent, A):
#             path_flow = math.inf

#             # Find bottleneck flow
#             tail = sync
#             while tail != source:
#                 head = parent[tail]
#                 path_flow = min(path_flow, A[head][tail])
#                 tail = head

#             # Update graph per Ford–Fulkerson algorithm
#             tail = sync
#             while tail != source:
#                 head = parent[tail]
#                 A[head][tail] -= path_flow
#                 A[tail][head] += path_flow
#                 tail = head

#             max_flow += path_flow

#         return max_flow

#     max_flow = edmonds_karp()

#     # If all orders "flow" through the graph, then there are enough shoppers to service them
#     return max_flow == len(orders)
