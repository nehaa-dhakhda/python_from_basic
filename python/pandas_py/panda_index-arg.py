import pandas as pd
a = [10,"raj",30.50]
myvar = pd.Series(a, index = ["rno", "nm", "avg"])
print(myvar)