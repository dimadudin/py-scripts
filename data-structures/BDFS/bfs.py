class Graph:
    def breadth_first_search(self, v):
        visited = []
        to_visit = [v]
        while to_visit:
            visited.append(to_visit.pop(0))
            adj = list(sorted(self.graph[visited[-1]]))
            for vertex in adj:
                if vertex not in visited and vertex not in to_visit:
                    to_visit.append(vertex)
        return visited

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
