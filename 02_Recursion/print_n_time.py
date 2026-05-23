n = int(input())

# Code here

def print_string(n):
   
    if n == 0:
        return
    print("GFG", end = ' ')
    print_string(n-1)
    
print_string(n)