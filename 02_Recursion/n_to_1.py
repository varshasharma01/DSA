def nto1(n):
    if n == 0:
        return
    print(n, end=" ")
    nto1(n-1)
    
nto1(5)