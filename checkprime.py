starting = int(input ("Enterstarting Number: "))  
ending = int(input ("Enter the Ending Number : "))  
  
print (" Prime Numbers in the range : ")  
for number in range (starting, ending + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)
