import numpy as np
import pandas as pd

data={
   "A":[1,2,3,4.,5],
   "B":[101,102,103,104,105],
   "C":[2,5,1,3,2],
   "D":[1600,100,800,1500,100]
}
#df is your dataframe
df=pd.DataFrame(data)

def sum(D):
   return sum
df["D"] = df["D"].apply(sum)
print(df)


#df is your dataframe
#example function is applicable for all INT dataframe


