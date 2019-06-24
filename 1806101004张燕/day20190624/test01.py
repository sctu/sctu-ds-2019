# 使用邻接表的方式存储图。
a, b, c, d, e, f, g, h = range(8)
N = [
    {b, c, d, e, f},
    {c, e},
    {d},
    {e},
    {f},
    {c, g, h},
    {f, h},
    {f, g}
]
#
# 使用邻接表的方式存储带权的图。
a, b, c, d, e, f, g, h = range(8)
N = [

    {b: 2, c: 1, d: 3, e: 9, f: 4},
    {c: 4, e: 4},
    {d: 8},
    {e: 7},
    {f: 5},
    {c: 2, g: 2, h: 2},
    {f: 1, h: 6},
    {f: 9, g: 8}
]

#
# 使用邻接矩阵的方式存储图。
a, b, c, d, e, f, g, h = range(8)

N = [
    [0, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0],
]
# 使用Dijkstra算法求解最短路径。
# # 图为邻接表形式
# # Dijkstra算法
# # 指定一个点到其他各顶点的路径——单源最短路径
# # 初始化图参数
G = {1: {1: 0, 2: 1, 3: 12},
     2: {2: 0, 3: 9, 4: 3},
     3: {3: 0, 5: 5},
     4: {3: 4, 4: 0, 5: 13, 6: 15},
     5: {5: 0, 6: 4},
     6: {6: 0}}


def Dijkstra(G, v0, INF=999):
    """ 使用 Dijkstra 算法计算指定点 v0 到图 G 中任意点的最短路径的距离
        INF 为设定的无限远距离值
        此方法不能解决负权值边的图
    """
    book = set()
    minv = v0  # 源顶点到其余各顶点的初始路程
    dis = dict((k, INF) for k in G.keys())
    dis[v0] = 0

    while len(book) < len(G):
        book.add(minv)  # 确定当期顶点的距离
        for w in G[minv]:  # 以当前点的中心向外扩散
            if dis[minv] + G[minv][w] < dis[w]:  # 如果从当前点扩展到某一点的距离小与已知最短距离
                dis[w] = dis[minv] + G[minv][w]  # 对已知距离进行更新
        new = INF  # 从剩下的未确定点中选择最小距离点作为新的扩散点

        for v in dis.keys():
            if v in book:
                continue
            if dis[v] < new:
                new = dis[v]
                minv = v
    return dis


dis = Dijkstra(G, v0=1)
print(dis)
