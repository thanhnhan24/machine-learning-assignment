# %%
network = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['F'],
    'D': ['G'],
    'E': [],
    'F': ['H', 'I'],
    'G': ['J', 'K'],
    'H': [],
    'I': [],
    'J': [],
    'K': []
}

# %%
def print_table(loop, current_node, gamma, open_list, close_list):
    if loop == 0:
        print(f"{'Loop':<6} | {'Current Node':<13} | {'Gamma':<20} | {'Open':<30} | {'Close':<30}")
        print('-' * 110)
    
    print(f"{loop:<6} | {str(current_node):<13} | {str(gamma):<20} | {str(open_list):<30} | {str(close_list):<30}")


# %%
def trace(parent, start, end):
    path = []
    current_node = end
    while current_node != start:
        path.append(current_node)
        if current_node not in parent:
            print("No path found")
            return []
        current_node = parent[current_node]
    path.append(start)
    path.reverse()
    return path

# %%
def BFS(network, start, end):
    open = []
    gamma = []
    close = []
    parent = {}
    loop = 0
    print_table(loop, '', '', start, '')
    currrent_node = start #n
    if currrent_node == end:
        return True
    while currrent_node !=  end:
        loop += 1
        if currrent_node in close:
            if open:
                currrent_node = open.pop(0)
                continue
            else:
                print("No more nodes to explore, ending search.")
                return False
        if network[currrent_node] != []:
            gamma = network[currrent_node]
        else:  
            gamma = []
        open += gamma
        close[:0] = [currrent_node]
        for child in gamma:
            if child not in parent:
                parent[child] = currrent_node
        print_table(loop, currrent_node, gamma, open, close)
        currrent_node = open.pop(0)
        if currrent_node == end:
            print_table(loop, currrent_node, gamma, open, close)
            print("Found the end node, begin backtracking")
            print(f"Path from {start} to {end}: {trace(parent, start, end)}")
            return True
        if loop > 50:
            print("Loop limit exceeded")
            return False



# %%
def DFS(network, start, end):
    open = []
    gamma = []
    close = []
    parent = {}
    loop = 0
    print_table(loop, '', '', start, '')
    currrent_node = start #n
    if currrent_node == end:
        return True
    while currrent_node !=  end:
        loop += 1
        if currrent_node in close:
            if open:
                currrent_node = open.pop(0)
                continue
            else:
                print("No more nodes to explore, ending search.")
                return False
        if network[currrent_node] != []:
            gamma = network[currrent_node]
        else:  
            gamma = []
        open[:0] = gamma
        close[:0] = [currrent_node]
        for child in gamma:
            if child not in parent:
                parent[child] = currrent_node
        print_table(loop, currrent_node, gamma, open, close)
        currrent_node = open.pop(0)
        if currrent_node == end:
            print_table(loop, currrent_node, gamma, open, close)
            print("Found the end node, begin backtracking")
            print(f"Path from {start} to {end}: {trace(parent, start, end)}")
            return True
        if loop > 50:
            print("Loop limit exceeded")
            return False



# %%
BFS(network, 'A', 'K')
DFS(network, 'A', 'K')


