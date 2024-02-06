def calculate_distance(x1, y1, x2, y2): 
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5    
    return distance 
def main(): 
    x1 = float(input("Enter the x-coordinate of the first point: "))   
    y1 = float(input("Enter the y-coordinate of the first point: "))    
    x2 = float(input("Enter the x-coordinate of the second point: "))    
    y2 = float(input("Enter the y-coordinate of the second point: ")) 
 
    distance = calculate_distance(x1, y1, x2, y2) 
 
    print(f"The distance between the two points is: {distance}") 
 
main() 
