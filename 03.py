import sys 
 
def add_numbers(num1, num2): 
    return num1 + num2 
 
def main(): 
    #if len(sys.argv) != 3: 
        #print("enter only two number") 
        #sys.exit(1) 
 
    num1 = float(sys.argv[1])    
    num2 = float(sys.argv[2]) 
 
    result = add_numbers(num1, num2) 
 
    print(f"The sum is: {result}") 
main() 
