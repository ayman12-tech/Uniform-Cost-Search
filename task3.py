from queue import Queue, PriorityQueue
graph = {
    'A': ['O', 'S', 'C'],
    'O': ['A', 'S'],
    'C': ['A', 'R','P'],
    'S': ['A', 'R','F'],
    'R': ['C', 'S', 'P'],
    'P': ['C', 'R', 'B'],
    'F': ['S', 'B'],
    'B': ['P', 'F']
}

cost = {
    ('A', 'O'): 146, #tuple
    ('A', 'S'): 140,
    ('A', 'C'): 494,

    ('O', 'A'): 146,
    ('O', 'S'): 151,

    ('C', 'A'): 494,
    ('C', 'R'): 146,
    ('C', 'P'): 138,

    ('S', 'A'): 140,
    ('S', 'R'): 80,
    ('S', 'F'): 99,

    ('R', 'S'): 80,
    ('R', 'C'): 146,
    ('R', 'P'): 97,

    ('P', 'C'): 138,
    ('P', 'R'): 97,
    ('P', 'B'): 101,

    ('F', 'S'): 99,
    ('F', 'B'): 211,

    ('B', 'P'): 101,
    ('B', 'F'): 211,
}

def ucsCost(from_node, to_node, weights=None):
    return weights.get((from_node, to_node), 10e100) #func. for adding the cost(from Python book)


def ucs(graph, start, goal, weights=None):

    fringe = PriorityQueue()    #setting my fringe as a priority queue
    fringe.put((0, start))  # (priority, node)  #giving zero cost to the root node
    explored = []   #for explored node

    while fringe:
        ucs_C, current_node = fringe.get()
        explored.append(current_node)

        if current_node == goal: #goal test
            return explored

        for node in graph[current_node]: #generate child
            if node not in explored:    #always check the node, beacuse we dont explored the node again in UCS
                fringe.put((ucs_C + ucsCost(current_node, node, weights),node))

print(ucs(graph, 'A', 'B', cost))