from timeit import default_timer as time
import random
import sys
import threading
from main import FordFullkerson
from main import Dinic
from main import Edge

number_of_test = 20
dinic_time = list()
ford_time = list()


class TimeCalculating:
    @staticmethod
    def time_calculating():
        given_list = [[[random.randint(0, 20) for i in range((k + 1)*20)] for j in range((k + 1)*20)]
                      for k in range(number_of_test)]
        for k in range(number_of_test):
            first_average_time = 0
            graph = given_list[k]
            start = time()
            dinic = Dinic(len(graph))
            for i in range(len(graph)):
                for j in range(len(graph)):
                    if (graph[i][j] != 0):
                        dinic.addEdge(i, j, graph[i][j])
            dinic.DinicMaxflow(0, (k + 1) * 20 - 1)
            interval = time() - start
            first_average_time += interval

            print(f"Time for Dinic solution for {len(given_list[k])} numbers",
                  first_average_time / len(given_list[k]))

            dinic_time.append(first_average_time / len(given_list[k]))

        for k in range(number_of_test):
            second_average_time = 0
            graph = given_list[k]
            start = time()
            ford = FordFullkerson(graph)
            ford.FordFulkerson(0, (k + 1) * 20 - 1)
            interval = time() - start
            second_average_time += interval

            print(f"Time for Ford Fullkerson solution for {len(given_list[k])} numbers",
                  second_average_time / len(given_list[k]))

            ford_time.append(second_average_time / len(given_list[k]))


sys.setrecursionlimit(10 ** 8)
threading.stack_size(2 ** 26)
threading.Thread(target=TimeCalculating.time_calculating()).start()