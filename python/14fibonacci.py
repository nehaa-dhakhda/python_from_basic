n=int(input("Enter Number :"))
def fibonacci(n):
    if n<0:
        return "Nagative Number"
    elif n==1:
        return 1
    else:
        f0=0
        f1=1
        count=0
        while count < n:
            print(f0)
            f2=f1+f0
            #update value
            f0=f1
            f1=f2
            count += 1
print(fibonacci(n))