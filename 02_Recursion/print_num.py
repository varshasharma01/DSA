# let's say we want to print number from 1 to N  there are two methods one is head and another is tail

# using head recursion

def print_num(i,n):
    
    if i>n:
        return
    else:
        print(i)
        return  (print_num(i+1, n))
       
    
print(print_num(1,5))
        
        
# using tail recursion

def rev_num(n):
    if n ==0:
        return
    else:
        rev_num(n-1)
        print(n, end=" ")
        
print(rev_num(5))
