def perm(s):
    if len(s)==1:
        return [s]
    else :
        pr=[]
        for i in s:

            remin=[x for x in s if x!=i]
            recall=perm(remin)
            for j in recall:
                pr.append[[i]+j]
        return pr
st=input("Enter String ")
print(perm(st))