#邻接表
G = {1: {1: 0, 2: 1, 3: 12},
     2: {2: 0, 3: 9, 4: 3},
     3: {3: 0, 5: 5},
     4: {3: 4, 4: 0, 5: 13, 6: 15},
     5: {5: 0, 6: 4},
     6: {6: 0}}

def Djkstra(G,vo,INF=999):
    """
    使用Dijkstra算法计算指定点vo到图G中任意点的最短路径的距离
    此方法不能解决负权值的图
    :param G:
    :param vo:
    :param INF: 设定的无限远距离值
    :return:
    """
    book=set()
    minv=vo   #源顶点到其余各顶点的初始路程
    dis=dict((k,INF) for k in G.keys())
    dis[vo]=0

    while len(book)<len(G):
        book.add(minv)   #确定当期顶点的距离
        for w in G[minv]: #以当前的中心向外扩散
            if dis[minv]+G[minv][w]<dis[w]:    #如果从当前点扩展到某一点的距离小于已知最短距离
                dis[w]=dis[minv]+G[minv][w]   #对已知距离进行更新
        new=INF   #从剩下的未确定点中选择最小距离点作为新的扩散点

        for v in dis.keys():
            if v in book:
                continue
            if dis[v]<new:
                new=dis[v]
                minv=v
        return dis

dis=Djkstra(G,vo=1)
print(dis)














