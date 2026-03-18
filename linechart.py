import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("diabetes.csv")
outcome_counts = df["Outcome"].value_counts()
plt.plot(outcome_counts.index,outcome_counts.values)
plt.xlabel("Outcome")
plt.ylabel("Count")
plt.title("Diabetes Distribution")
plt.show()