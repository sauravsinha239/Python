str=input("Enter Value to check palindrome or not!")
rev=str[::-1]
if(rev==str):
    print("Value is Palindrome ",rev)
else:
    print("Value is Not Palindrome ",rev)