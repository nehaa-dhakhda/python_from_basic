#for loop
print("Example of for loop")
for i in range(1,6):
    print(i)
#while loop
print("Example of while loop")
i=1
while i<6:
    print(i)
    i+=1
#continue statement
print("Example of continue")
for i in range(1,5):
    if (i==3):
        continue
    print(i)
#break statement
print("Example of break ")
for i in range(1,10):
    if (i==8):
        break
    print(i)