Vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
AdjVer = [[1, 2],
          [0, 3],
          [0, 3, 4],
          [1, 2, 5],
          [2, 6, 7],
          [3],
          [4, 7],
          [4, 6]]

from queue import LifoQueue
visited = [False] * len(Vertex)

def iDFS(u):
    S = LifoQueue()
    S.put(u)
    
    while not S.empty():
        u = S.get()
        S.put(u) # peek()
        
        if visited[u] == False:
            visited[u] = True
            print(Vertex[u], end = '')
            
        flag = True # 유용함, 깃발 True = 올림, False = 내림
        
        for v in AdjVer[u]:
            if visited[v] == False:
                S.put(v)
                flag = False
                break
                
            if flag == True:
                S.get()
                
if __name__ == "__main__":
    print('iDFS(A) : ')