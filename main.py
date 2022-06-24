import time

class Edge:
    def __init__(self, v, flow, C, rev):
        self.v = v
        self.flow = flow
        self.C = C
        self.rev = rev

class Dinic:
    def __init__(self, V):
        self.adj = [[] for i in range(V)]
        self.V = V
        self.level = [0 for i in range(V)]

    def addEdge(self, u, v, C):
        a = Edge(v, 0, C, len(self.adj[v]))
        b = Edge(u, 0, 0, len(self.adj[u]))
        self.adj[u].append(a)
        self.adj[v].append(b)

    def BFS(self, s, t):
        for i in range(self.V):
            self.level[i] = -1
        self.level[s] = 0
        q = []
        q.append(s)
        while q:
            u = q.pop(0)
            for i in range(len(self.adj[u])):
                e = self.adj[u][i]
                if self.level[e.v] < 0 and e.flow < e.C:
                    self.level[e.v] = self.level[u] + 1
                    q.append(e.v)
        return False if self.level[t] < 0 else True

    def sendFlow(self, u, flow, t, start):
        if u == t:
            return flow
        while start[u] < len(self.adj[u]):
            e = self.adj[u][start[u]]
            if self.level[e.v] == self.level[u] + 1 and e.flow < e.C:
                curr_flow = min(flow, e.C - e.flow)
                temp_flow = self.sendFlow(e.v, curr_flow, t, start)
                if temp_flow and temp_flow > 0:
                    e.flow += temp_flow
                    self.adj[e.v][e.rev].flow -= temp_flow
                    return temp_flow
            start[u] += 1

    def DinicMaxflow(self, s, t):
        if s == t:
            return -1
        total = 0
        while self.BFS(s, t) == True:
            start = [0 for i in range(self.V + 1)]
            while True:
                flow = self.sendFlow(s, float('inf'), t, start)
                if not flow:
                    break
                total += flow
        return total


class FordFullkerson:
    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)
        # self.COL = len(gr[0])

    def BFS(self, s, t, parent):
        visited = [False] * (self.ROW)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True
        return False

    def FordFulkerson(self, source, sink):
        parent = [-1] * (self.ROW)
        max_flow = 0
        while self.BFS(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while (s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
            max_flow += path_flow
            v = sink
            while (v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
        return max_flow

class TimeCalculating:
    def __init__(self, graph):
        self.graph = graph

    def time_calculating(self, s, t):
        first_time = 0
        start = time.time()

        dinic = Dinic(len(self.graph))
        for i in range(len(self.graph)):
            for j in range(len(self.graph)):
                if (graph[i][j] != 0):
                    dinic.addEdge(i, j, graph[i][j])
        dinic.DinicMaxflow(s, t)
        end = time.time()
        first_time += (end - start)
        print("Time for Dinic solution:", first_time)

        second_time = 0
        start = time.time()
        fordfull = FordFullkerson(self.graph)
        fordfull.FordFulkerson(s, t)
        end = time.time()
        second_time += (end - start)
        print("Time for Ford Fullkerson:", second_time)

graph = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]