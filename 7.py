def get_median(t):  
       ls = sorted(t)    
       if len(ls) % 2 != 0:  
        m = int((len(ls)+1)/2 - 1)     
        return ls[m]    
       else: 
        m1 = int(len(ls)/2 - 1)    
        m2 = int(len(ls)/2)      
        return (ls[m1]+ls[m2])/2 
t = (5, 2, 6, 3, 4) 
print("median of list " , sorted(t) ,"is")
print(get_median(t)) 
 
