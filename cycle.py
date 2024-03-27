

def dfs(graph, start, end):
    fringe = [(start, [])]
    while fringe:
        state, path = fringe.pop()
        if path and state == end:
            yield path
            continue
        for next_state in graph[state]:
            if next_state in path:
                continue
            fringe.append((next_state, path+[next_state]))
            

x=int(input())
l=[]
for i in range(x):
    l.append(int(input()))
d={}
for i in range(len(l)):
    d[i]=[l[i]]

cycles = [[node]+path  for node in d for path in dfs(d, node, node)]

print(len(cycles))
