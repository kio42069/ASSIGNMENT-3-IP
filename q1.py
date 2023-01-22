n = int(input("Enter n: "))
def printer(n,t):
    print("*"*t+" "*(n-t)+" "*(n-t)+"*"*t)
    printer(n,t-1) if t != 1 else print("",end = "")
def printout(n,t):
    print("*"*t+" "*(n-t)+" "*(n-t)+"*"*t)
    printout(n,t+1) if t!= n else print("",end = "")
printer(n,n)
printout(n,1)