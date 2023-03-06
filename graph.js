let edges = {
  AD: { distance: 13, time: 5 },
  AB: { distance: 10, time: 5 },
  CB: { distance: 4, time: 1 },
  CD: { distance: 8, time: 3 },
  ED: { distance: 10, time: 3 },
  EA: { distance: 14, time: 5 },
};

let graph = {};

edgesToGraph = (edges) => {
  for (let edge in edges) {
    if (!graph[`${edge[0]}`]) {
      graph[`${edge[0]}`] = {};
    }
    if (!graph[`${edge[0]}`][`${edge[1]}`]) {
      graph[`${edge[0]}`][`${edge[1]}`] = {};
    }

    graph[`${edge[0]}`][`${edge[1]}`] = edges[edge];

    if (!graph[`${edge[1]}`]) {
      graph[`${edge[1]}`] = {};
    }
    if (!graph[`${edge[1]}`][`${edge[0]}`]) {
      graph[`${edge[1]}`][`${edge[0]}`] = {};
    }

    graph[`${edge[1]}`][`${edge[0]}`] = edges[edge];
  }
};

edgesToGraph(edges);

const shortestDistance = (graph, src, dest) => {
  /* set global adistance var to infinity 
    loop through A neighbours
     
    if neighbour equals dest check if neighbour distance less tahn global distance 
       if so set distance = neghbour distance and continue traversing
    */
  let minDistance = Infinity;
  let distance = 0;
  let path = [0];
  let pathObj = [];
  let start = [src, 0];
  let visited = new Set();
  visited.add("A");
  for (neighbour in graph[src]) {
    path = ["A"];
    path = explore(
      path,
      graph,
      dest,
      [neighbour, graph[src][neighbour]["time"]],
      visited
    );
    if (minDistance > path[1]) minDistance = path[1];
    pathObj.push(path.slice());
  }

  let minPath=pathObj.filter(el=>el[1]==minDistance)

  return minPath;
};

const explore = (path, graph, dest, payload, visited) => {
  src = payload[0];
  path.push(src);
  if (payload[0] == dest) return [path, payload[1]];
  visited.add(src);
  for (neighbour in graph[src]) {
    if (!visited.has(neighbour))
      return explore(
        path,
        graph,
        dest,
        [neighbour, graph[src][neighbour]["time"] + payload[1]],
        visited
      );
  }
};

console.log(graph);
console.log(shortestDistance(graph, "A", "D"));
