from matplotlib import pyplot as plt
import seaborn as sb
import pandas as pd
df=pd.read_csv("diabetes.csv")
age_bp=pd.crosstab(df["Age"],df["BloodPressure"])
age_bp.plot(kind="bar")
plt.title("Age Based Blood Pressure")
plt.xlabel("Age")
plt.ylabel("Blood Pressure")
plt.show()
