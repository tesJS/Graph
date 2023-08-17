""" A program that can find the shortest or 
fastest route between two nodes given a graph 
that consists of nodes and edges. For practical 
map applications nodes can be taken as intersections
and roads connecting intersections as edges"""

graph = {
    'A': [('B',2,1), ('C', 19 ,4)],
    'B': [('A', 2,1), ('D',5,4),('G',5,4) ],
    'C': [('A',1,1), ('D',4,3), ('E',6,3)],
    'D': [('B',5,4), ('C', 7 ,4), ('E',9,8), ('G',5,4)],
    'E': [('C', 6 ,3), ('E',9,8)],
    'G': [('B',5,4), ('D',9,8)],
}

""" A utility function to prevent looping on same edge. It checks for uniqueness of paths. For example 
while going on route ABCD if encoutered ABCB function sees 2 B's and return true"""
def check(input_str):    
    letter_count = {}
    
    for letter in input_str:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    
    for count in letter_count.values():
        if count > 1:
            return True
    
    return False

""" Finds all possible routes from start to destination
 excluding loopings while adding distance and time on its way to destination"""
def find_paths(graph,start,end):    
    stack=[(start,0,0)]
    paths=dict()

    while stack:
        current=stack.pop()
        if check(current[0]):
            continue
        if current[0][-1]==end:
            paths[current[0]]=(current[1],current[2])
        for neigbour in graph.get(current[0][-1],[]):
            n,d,t=neigbour
            t+=current[2] 
            d+=current[1] 
            n=current[0]+n          
            stack.append((n,d,t))            
            
    return paths

""" Uses find_paths function to filter out the route that has the minimum time sum"""
def find_fastest_path(graph,start,end):
    paths=find_paths(graph,start,end) 
    print(paths)   
    fastest_path= min(paths.items(), key=lambda item: item[1][1])
    return fastest_path

""" Uses find_paths function to filter out the route that has 
the minimum distance sum"""
def find_shortest_path(graph,start,end):
    paths=find_paths(graph,start,end) 
    print(paths)   
    fastest_path= min(paths.items(), key=lambda item: item[1][0])
    return fastest_path
        
    
print(find_shortest_path(graph,'A','C'))

