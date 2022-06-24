import matplotlib.pyplot as graph

from benchmark import dinic_time, ford_time

size = [1000*(i + 1) for i in range(20)]
graph.plot(size, dinic_time, label="Dinic Solution")
graph.plot(size, ford_time, label="Ford Fullkerson Solution")
graph.legend()
graph.show()