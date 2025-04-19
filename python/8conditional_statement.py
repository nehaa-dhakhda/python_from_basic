#simple if else
user=int(input("Enter Your AGE: "))
if (user<18):
    print("You are not eligible for vote")
else:
    print("You are eligible for voting")
#elif
user1=input("Enter Username: ")
data="admin"
data2="client"
if (user1==data):
    print("Admin Dashboard")
elif (user1==data2):
    print("Client Dashboard")
else:
    print("Guest")
