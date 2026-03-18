import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("diabetes.csv")

outcome_counts = df["Outcome"].value_counts()
explode=(0.1,0)

plt.figure(figsize=(6,6))
plt.pie(outcome_counts,explode=explode,shadow=True,
        labels=["No Diabetes", "Diabetes"],
        autopct="%1.1f%%")
plt.title("Diabetes Distribution")
plt.show()