#Dinic’s algorithm for Maximum Flow

1) Initialize residual graph G as given graph.
2) Do BFS of G to construct a level graph (or
   assign levels to vertices) and also check if 
   more flow is possible.
    a) If more flow is not possible, then return.
    b) Send multiple flows in G using level graph 
       until blocking flow is reached. Here using 
       level graph means, in every flow,
       levels of path nodes should be 0, 1, 2...
       (in order) from s to t.
       
Time Complexity : O(EV2). 
Doing a BFS to construct level graph takes O(E) time. Sending multiple more flows until a blocking flow is reached takes O(VE) time. The outer loop runs at-most O(V) time. In each iteration, we construct new level graph and find blocking flow. It can be proved that the number of levels increase at least by one in every iteration (Refer the below reference video for the proof). So the outer loop runs at most O(V) times. Therefore overall time complexity is O(EV2). 

#Ford-Fulkerson Algorithm for Maximum Flow Problem

The following is simple idea of Ford-Fulkerson algorithm:
1)Start with initial flow as 0.
2)While there is a augmenting path from source to sink. 
-Add this path-flow to flow.
3)Return flow.

Time Complexity : The idea of Edmonds-Karp is to use BFS in Ford Fulkerson implementation as BFS always picks a path with minimum number of edges. When BFS is used, the worst case time complexity can be reduced to O(VE2). The above implementation uses adjacency matrix representation though where BFS takes O(V2) time, the time complexity of the above implementation is O(EV3)
