def task_graph(filename):
    graph = {}
    with open(filename, 'r') as f:
        for line in f:
            if ':' in line:
                parts = line.strip().split(':')
                node = int(parts[0])
                if parts[1].strip():
                    neighbors = list(map(int, parts[1].strip().split()))
                    graph[node] = neighbors
                else:
                    graph[node] = []
    return graph

def breath_first_search(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)

    while queue:
        current = queue.pop(0)
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited

def find_root(graph):
    for node in graph:
        visited = breath_first_search(graph, node)
        if len(visited) == len(graph):
            return node
    return -1

def main():
    graph = task_graph('input.txt')
    root = find_root(graph)
    with open('output.txt', 'w', encoding='utf-8') as f:
        if root != -1:
            f.write(f"Вершина {root} може дійти до всіх інших")
        else:
            f.write("Немає вершини, з якої можна дійти до всіх інших")

if __name__ == "__main__":
    main()
