#################################
#Author: Brandon Jones
#Description: Program using BFS
#Date: 11/5/19
###################################


#Main function the program is run from
def main():
    inFile = 'input.txt'

    #wrestlers are added to this dictionary 
    finalDict = {}
    

    with open(inFile, 'r') as f:
    #Find the number of wrestlers 
        lines = f.readlines()

        #variables used throughout
        loopNum = 0
        conC = 0
        conT = 0
        wrestlerNum = 0
        wres = ""
        graph = {}
        connection = []
        des = bool

        #loops through each line and extracts 
        for line in lines:
            
            line = line.strip()

            #when zero, it will pull the first line
            if loopNum == 0:

                #how many wrestlers
                wrestlerNum = int(line)

            #begins adding wreslters to dictionary
            if 0 < loopNum <= wrestlerNum:

                #for the first one
                if loopNum == 1:
                    first = line


                #each line with wrestler name is added to the dictionary
                #visited keys are initialized
                graph[line] = {
                    'visited': False,
                    'distance': 0,
                    'connections': []
                }

            #looks for match in values
            if loopNum == wrestlerNum + 1:

                #if match, pulls value from line
                conT = int(line)

            #checks for connections between wrestlers to account for rivalries
            if (loopNum > (wrestlerNum + 1)) and (conC < conT):
                
                line = line.split()

                #if connection, it's added to list
                connection.append(line)

                #adds to dictionary
                graph[line[0]]['connections'].append(line[1])
                graph[line[1]]['connections'].append(line[0])

                conC += 1

            loopNum += 1

        #Everything is added to final dictionary
        finalDict["start"] = first
        finalDict["graph"] = graph
        finalDict["connections"] = connection

    
        while True: 
            
            #used to target sectoin of dictoinary
            gr = finalDict['graph']
            
            #loop through all names
            for w in gr:

                #if it hasn't been visited, that name equals wres
                if not gr[w]['visited']:
                    wres = w
                #has been visited
                else:
                    wres = ""

            #used to exit loop 
            if wres == "":
                break
            

            g = finalDict['graph']

            queue = [wres]

            #initializes to true
            g[wres]['visited'] = True

            #beginning of BFS creates starting point
            #source: https://www.geeksforgeeks.org/best-first-search-informed-search/
            while not len(queue) == 0: 
                wre = queue.pop(0)
                dist = g[wre]['distance'] + 1

                for nextW in g[wre]['connections']:
                    if not g[nextW]["visited"]:
                        g[nextW]['visited'] = True
                        g[nextW]['distance'] = dist
                        queue.append(nextW)
       
       #targets sectoin of dictoinary
        g = finalDict['graph']
        con = finalDict['connections']

        for c in con: 
            #calculates total for each 
            one = g[c[0]]["distance"]
            two = g[c[1]]["distance"]
            tot = two - one

            #determins if even or odd based on number 
            if tot % 2 == 0:
                des = False
            else: 
                des = True
        
        #If possible 
        if des:
            print("Yes")


            #Array for final output
            babyF = []
            heels = []
            
            str1 = ", "
            str2 = ", "
            for w in finalDict['graph']: 
                if finalDict['graph'][w]["distance"] % 2 == 0: 
                    
                    heels.append(w)
                else: 
                    babyF.append(w)
            
            #output string
            print("Babyfaces: " + str1.join(babyF[::-1]))
            print("Heels: " + str2.join(heels[::-1]))
           
        #not possible
        else: 
                print("No")        

if __name__ =="__main__":
    main()




