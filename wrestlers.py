#################################
#Author: Brandon Jones
#Description: The shopping spree program reads in a txt file and determines the max number of items 
#that can be carried
#Date: 10/18/19
###################################

def get_unvisited_wrestler(graph):
    for wrestler in graph:
        if not graph[wrestler]['visited']:
            return wrestler

    return ""


# Forms two teams using the assumption that all vertices with even distance are baby faces
# and all vertices with odd distance are heels
def get_teams(graph):
    babyfaces = "Babyfaces: "
    heels = "Heels: "

    for wrestler in graph:
        if graph[wrestler]['distance'] % 2 == 0:
            babyfaces = babyfaces + wrestler
            babyfaces = babyfaces + " "
        else:
            heels = heels + wrestler
            heels = heels + " "

    return [babyfaces, heels]






#Main function the program is run from
def main():
    inFile = 'input.txt'
    finalDict = {}

    with open(inFile, 'r') as f:
    #Find the number of test cases
        lines = f.readlines()
        loopNum = 0
        conC = 0
        conT = 0
        wrestlerNum = 0
        graph = {}
        

        # Store a list of connection for later usage
        connections = []

        for line in lines:
            # Remove new line characters
            line = line.strip()

            # The first line contains the number of wrestlers
            if loopNum == 0:
                wrestlerNum = int(line)

            # Fill the graph dictionary with wrestler names as keys
            if 0 < loopNum <= wrestlerNum:
                if loopNum == 1:
                    start = line

                graph[line] = {
                    'visited': False,
                    'distance': 0,
                    'connections': []
                }

            if loopNum == (wrestlerNum + 1):
                conT = int(line)

        
            if loopNum > (wrestlerNum + 1) and conC< conT:
                
                line = line.split()
                connections.append(line)
                graph[line[0]]['connections'].append(line[1])
                graph[line[1]]['connections'].append(line[0])
                conC += 1

            loopNum += 1
        finalDict["start"] = start
        finalDict["graph"] = graph
        finalDict["connections"] = connections

        while True: 
            wres = get_unvisited_wrestler(finalDict['graph'])

            if wres == "":
                break
            

    #bfs_distance(finalDict['graph'], wres)

            g = finalDict['graph']
            queue = [wres]
            g[wres]['visited'] = True

            
            while not len(queue) == 0: 
                wre = queue.pop(0)
                dist = g[wre]['distance'] + 1

                for nextW in g[wre]['connections']:
                    if not g[nextW]["visited"]:
                        g[nextW]['visited'] = True
                        g[nextW]['distance'] = dist
                        queue.append(nextW)


        #des = check_connections(finalDict)
        des = bool
        g = finalDict['graph']
        con = finalDict['connections']

        for c in con: 
            one = g[c[0]]["distance"]
            two = g[c[1]]["distance"]
            tot = two - one

            if tot % 2 == 0:
                des = False
            else: 
                des = True
        


        if des:
            print("Yes")
            team = get_teams(finalDict['graph'])
            print(team[0])
            print(team[1])
        else: 
                print("No")        

if __name__ =="__main__":
    main()




