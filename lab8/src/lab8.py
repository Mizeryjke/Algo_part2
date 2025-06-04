def read_graph(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    
    sources = lines[0].split(',')
    sinks = lines[1].split(',')
    edges = [line.split(',') for line in lines[2:]]

    graph = {}
    capacity = {}

    def add_edge(u, v, c):
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)
        capacity[(u, v)] = int(c)
        capacity[(v, u)] = 0

    for u, v, c in edges:
        add_edge(u, v, c)

    super_source = 'SRC'
    super_sink = 'SNK'

    graph[super_source] = []
    for s in sources:
        graph[super_source].append(s)
        graph[s].append(super_source)
        capacity[(super_source, s)] = float('inf')
        capacity[(s, super_source)] = 0

    graph[super_sink] = []
    for t in sinks:
        graph[t].append(super_sink)
        graph[super_sink].append(t)
        capacity[(t, super_sink)] = float('inf')
        capacity[(super_sink, t)] = 0

    return graph, capacity, super_source, super_sink


def dfs(graph, capacity, flow, u, t, visited, curr_flow):
    if u == t:
        return curr_flow
    visited[u] = True
    for v in graph[u]:
        residual = capacity.get((u, v), 0) - flow.get((u, v), 0)
        if not visited.get(v, False) and residual > 0:
            min_flow = min(curr_flow, residual)
            pushed = dfs(graph, capacity, flow, v, t, visited, min_flow)
            if pushed > 0:
                flow[(u, v)] = flow.get((u, v), 0) + pushed
                flow[(v, u)] = flow.get((v, u), 0) - pushed
                return pushed
    return 0


def max_flow(graph, capacity, source, sink):
    flow = {}
    total_flow = 0

    while True:
        visited = {}
        pushed = dfs(graph, capacity, flow, source, sink, visited, float('inf'))
        if pushed == 0:
            break
        total_flow += pushed
    return total_flow


def compute_max_flow(filename):
    graph, capacity, source, sink = read_graph(filename)
    return max_flow(graph, capacity, source, sink)


def main():
    result = compute_max_flow('roads.csv')
    print(result)


if __name__ == "__main__":
    main()
