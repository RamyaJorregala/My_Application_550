from matplotlib import pyplot as plt
import seaborn as sb
import pandas as pd
df=pd.read_csv("diabetes.csv")
plt.figure()
plt.scatter(df["Pregnancies"],df["Outcome"])
plt.title("Pregnancies vs Diabetes")
plt.xlabel("Pregnancies")
plt.ylabel("Outcome")
plt.show()
