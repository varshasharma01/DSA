def sumOfSeries(n):
    #normal approach
    # n = int(n)
    # sumofN = int((n*(n+1))/2)
    
    # return int(sumofN*sumofN)
    
    if n==0:
        return 0
    print(str(n)+"^3+",end=' ')
    return n**3 + sumOfSeries(n-1)
    
print(sumOfSeries(5))