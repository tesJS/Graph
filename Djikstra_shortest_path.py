#undirected graph each letter represent nodes and their respective costs
""" graph = {
    'A': [('B',4), ('C',19 )],
    'B': [('A',2), ('D',5),('C',5) ],
    'C': [('A',10), ('B',2),('D',4), ('E',16)],
    'D': [('B',5), ('C',7 ), ('E',1)],
    'E': [('C',6), ('D',9)],
    
} """



#directed graph each letter represent nodes and their respective costs
""" graph = {
    'A': [('B',10)],
    'B': [('C',5),('G',90) ],
    'C': [('D',4), ('E',1)],
    'D': [('F',5),('H',9)],  
} """

""" DIAMOND shaped directed test graph
graph = {
    'A': [('B',5)],
    'B': [('C',10), ('R',10)],
    'C': [('E',0)],    
    'R': [('E',10)],
    
} """

class PriorityQueue:
    def __init__(self) -> None:
        self.queue=[]
        self.sort()
    def add_item(self,node,parent,cost):
        queue_has_node=False
        
        for item in self.queue:
            if item[0]==node:                
                queue_has_node=True
                break
        if queue_has_node:
            element=list(filter(lambda item:item[0]==node,self.queue))
            element=element[0]
            if cost<element[2]:
                element[2]=cost
                element[1]=parent
                #queue2.append(element)
        else:
            self.queue.append([node,parent,cost])
            #queue2.append([node,parent,cost])
        self.sort()

    def remove_item(self,node):
        self.queue[:]=filter(lambda item:item[0]!=node,self.queue)

    def get_node(self,node):
        return list(filter(lambda item:item[0]==node,self.queue))

    def sort(self):
        self.queue=sorted(self.queue,key=lambda item:item[2])

    def get_queue(self):
        return self.queue
    
    def pop(self):
        return self.queue.pop(0)


queue2=[]

def find_paths(graph,start,end):    
    queue=PriorityQueue()
    queue.add_item(start,start,0)
    path=dict()
    visited=set()

    while queue:
        current=queue.pop()
        print(current) 
        parent=current[1]
        visited.add(current[0]) 
              
        if current[0]==end:
            path[current[0]]=current
            break
        for neigbour in graph.get(current[0],[]):
            if neigbour[0] not in visited:
                node,cost=neigbour                
                pt=parent+node
                cost+=current[2]
                queue.add_item(node,pt,cost)
    [node,path,dist]=path[end]
    return {'Shortest Path':path,'Cost ':dist}

print(find_paths(graph,'A','E'))
