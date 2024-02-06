l = [] 
n=int(input("enter number of element in list ")) 
for i in range(n):     
        num = int(input(f"Enter element {i+1}: ")) 
        l.append(num) 
 
res = list(map(lambda x: x ** 3, l))
print("normal list" , l) 
print("cube of list",res) 
