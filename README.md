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
#Ford-Fulkerson Algorithm for Maximum Flow Problem
    Ford-Fulkerson Algorithm 
     The following is simple idea of Ford-Fulkerson algorithm:
        1.Start with initial flow as 0.
        2.While there is a augmenting path from source to sink. 
            -Add this path-flow to flow.
        3.Return flow.
