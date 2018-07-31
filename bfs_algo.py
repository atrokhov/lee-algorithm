def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        point = queue.pop(0)
        if point not in visited:
            visited.add(point)
            queue.extend(graph[point] - visited)
    return visited

def bfs_paths(graph, start, end):
    queue = [(start, [start])]
    while queue:
        (point, path) = queue.pop(0)
        for next in graph[point] - set(path):
            if next == end:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

def shortest_path(graph, start, end):
    try:
        return next(bfs_paths(graph, start, end))
    except StopIteration:
        return None





