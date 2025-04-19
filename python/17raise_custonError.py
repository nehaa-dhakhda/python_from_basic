user=int(input("Enter any number between 0 and 10 : "))
if(user>0 and user<10):
    print(user)
else:
    raise ValueError("This entered value is invalid")
