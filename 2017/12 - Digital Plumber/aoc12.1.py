from collections import defaultdict

def getRoots(aNeigh):
    def findRoot(aNode,aRoot):
        while aNode != aRoot[aNode][0]:
            aNode = aRoot[aNode][0]
        return (aNode,aRoot[aNode][1])
    myRoot = {} 
    for myNode in aNeigh.keys():
        myRoot[myNode] = (myNode,0)  
    for myI in aNeigh: 
        for myJ in aNeigh[myI]: 
            (myRoot_myI,myDepthMyI) = findRoot(myI,myRoot) 
            (myRoot_myJ,myDepthMyJ) = findRoot(myJ,myRoot) 
            if myRoot_myI != myRoot_myJ: 
                myMin = myRoot_myI
                myMax = myRoot_myJ 
                if  myDepthMyI > myDepthMyJ: 
                    myMin = myRoot_myJ
                    myMax = myRoot_myI
                myRoot[myMax] = (myMax,max(myRoot[myMin][1]+1,myRoot[myMax][1]))
                myRoot[myMin] = (myRoot[myMax][0],-1) 
    myToRet = {}
    for myI in aNeigh: 
        if myRoot[myI][0] == myI:
            myToRet[myI] = []
    for myI in aNeigh: 
        myToRet[findRoot(myI,myRoot)[0]].append(myI) 
    return myToRet  

file = open("input.txt", "r")
pipes = file.readlines()
graph = defaultdict(set)
for p in pipes:
    graph[p.split()[0]].update([s.strip(',') for s in p.split()[2:]])

roots = getRoots(graph)
nConnected = 0
for r, v in roots.items():
    if '0' in v:
        print(r, v, '0' in v)
        nConnected += len(v)
print(nConnected)