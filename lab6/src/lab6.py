def possible_pairs(n, pairs):
    def is_boy(x):
        return x % 2 == 1

    def is_girl(x):
        return x % 2 == 0

    graph = {}
    all_people = set()
    for u, v in pairs:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)
        all_people.add(u)
        all_people.add(v)

    visited = set()

    def bfs(start):
        queue = [start]
        tribe = []
        while queue:
            current = queue.pop(0)
            if current not in visited:
                visited.add(current)
                tribe.append(current)
                for neighbor in graph.get(current, []):
                    if neighbor not in visited:
                        queue.append(neighbor)
        return tribe

    tribes = []
    for person in all_people:
        if person not in visited:
            tribes.append(bfs(person))

    total_boys = 0
    total_girls = 0
    internal_pairs = 0

    for tribe in tribes:
        boys = sum(1 for p in tribe if is_boy(p))
        girls = sum(1 for p in tribe if is_girl(p))
        total_boys += boys
        total_girls += girls
        internal_pairs += boys * girls

    total_pairs = total_boys * total_girls
    cross_tribe_pairs = total_pairs - internal_pairs

    return cross_tribe_pairs


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    n = int(lines[0].strip())
    pairs = [list(map(int, line.strip().split())) for line in lines[1:n+1]]

    result = possible_pairs(n, pairs)

    with open("output.txt", "w") as f:
        f.write(str(result) + "\n")


if __name__ == "__main__":
    main()
