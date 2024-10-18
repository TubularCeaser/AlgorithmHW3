#problem 2
def fibo(n):
    if n<0 or n>=50:
        return "incorrect"
    elif n==1:
        return 1
    elif n==2:
        return 1
    else:
        return(fibo(n-1)+fibo(n-2))

print(fibo(7))