import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("diabetes.csv")

df["Outcome"].value_counts().plot(kind="bar")
plt.title("Diabetes Count")
plt.xlabel("Outcome")
plt.ylabel("Count")
plt.show()
