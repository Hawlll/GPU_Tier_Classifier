import pandas as pd
import os
from matplotlib import pyplot as plt

df = pd.read_csv(os.path.join("data", "2025-03.csv"))
print(df.select_dtypes(include="object").columns)

for col in df.select_dtypes(include=["float64", "int64"]):

    df[col].hist()
    plt.xlabel(col)
    plt.ylabel("count")
    plt.title(f"{col} Distribution")
    plt.show()

    