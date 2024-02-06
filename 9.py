def listOfSets(inputSet): 
  outputList = []  
  for k in inputSet:   
        emptySet = set()      
        emptySet.add(k)       
        outputList.append(emptySet) 
        return(outputList) 
 
inputSet = {'hello', 'from', 'srm'} 
 
print("The given set is:", inputSet)
print("Breaking the input set into a list of sets:\n", listOfSets(inputSet)) 
