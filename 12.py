import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
df=pd.read_csv(r"C:\Users\cs\Desktop\Abubakar AIML\Iris.csv")
print(df)
print(df.tail(10))
print(df.info())
print(df.dropna(inplace=True))
df.fillna(df.mean(numeric_only=True), inplace=True)
print(df)
print(df.isnull().sum())
print(df["SepalLengthCm"])
sns.scatterplot(x=df["SepalLengthCm"],y=df["PetalLengthCm"],hue=df["Species"])
plt.title("Scatter Plot of Sepal Length Cm and Petal Length Cm")
plt.xlabel("Sepal Length Cm")
plt.ylabel("Petal Length Cm")
plt.grid()
plt.show()
sns.heatmap(df[["PetalWidthCm","SepalLengthCm","PetalLengthCm"]])
plt.title("Heat Map of Petal Width Cm, Sepal Length Cm and Petal Length Cm")
plt.xlabel("Columns")
plt.ylabel("Rows")
plt.show()
Q1=df['PetalLenghtCm'].quantile(0.90)
Q3=df['PetalWidthCm'].quantile(0.10)
IQR=Q3-Q1
UpperLimit=Q3+1.5*IQR
LowerLimit=Q1-1.5*IQR
outlier=df['PetalLengthCm']>=UpperLimit and df['PetalWidthC']