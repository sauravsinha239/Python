def is_even(number):  
    return number % 2 == 0 
def is_prime(number):   
      if number < 2:        
         return False     
      for i in range(2, int(number**0.5) + 1):     
            if number % i == 0: return False 
            return True 
def main(): 
        number = int(input("Enter a number: "))   
        if is_even(number): 
            print(f"{number} is even.")
        else: 
            print(f"{number} is odd.") 
        if is_prime(number): 
                    print(f"{number} is prime.")  
        else: 
                 print(f"{number} is not prime.") 
main() 
