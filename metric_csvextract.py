import pandas as pd

methist = pd.read_csv(r'C:\Users\mj004210\Desktop\Metrics\2018_Jan\assembly.csv', names=['Tiles passed km^2','Tiles marginal km^2'])

df1 = pd.DataFrame(methist)

df2 = df1.set_index("date")