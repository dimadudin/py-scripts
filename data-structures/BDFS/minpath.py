class Graph:
    def bfs_path(self, start, end):
        visited = []
        to_visit = [[start]]
        while to_visit:
            path = to_visit.pop(0)
            node = path[-1]
            if node not in visited:
                adj = list(sorted(self.graph[node]))
                for vertex in adj:
                    new_path = list(path)
                    new_path.append(vertex)
                    to_visit.append(new_path)
                    if vertex == end:
                        return new_path
                visited.append(node)
        return None

    # don't touch below this line

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    def __repr__(self):
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result
