
v=int(input())
e=int(input())
s=int(input())
d=int(input())
graph=dict()
for i in range(e):
    a,b=map(int,input().split())
    if a not in graph:
        graph[a]=[b]
        if b not in graph:
            graph[b]=[a]
        else:
            graph[b].append(a)
    else:
        graph[a].append(b)
        if b not in graph:
            graph[b]=[a]
        else:
            graph[b].append(a)
def bfs(graph,s,d):
    visited=[False]*v
    queue=[]
    queue.append(s)
    visited[s]=True
    while queue:
        s=queue.pop(0)
        for i in graph[s]:
            if visited[i]==False:
                queue.append(i)
                print(s)
                visited[i]=True

                if i==d:
                    print(s)
                    return True

    print(queue)
    return False

if bfs(graph,s,d):
    print("Yes, its possible")



 

       
