def permutation(s):
   if len(s) == 1:
     return [s]

   perm_list = [] 
   for i in s:
     remaining_elements = [x for x in s if x != i]
     z = permutation(remaining_elements) 

     for t in z:
       perm_list.append([i] + t)

   return perm_list
st=input("Enter String ")
print(permutation(st))