#excaption in python
#print table of inputed value by user
def exception_handling():
    try:
        user=int(input("Enter any value : "))
        for i in range(1,11):
            print(f"{user} * {i} = ",user*i)
            # return 1
    except Exception as e:
        print(e)
        # return 0
    finally:
        print("i\'m always execute")
    print("some imp code")
exception_handling()