import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns# type: ignore

data = pd.read_csv("C:/Users/Hassan/Documents/Programming/diabetes.csv")

a = data.head(20)
gl = a['Glucose']
plt.plot(gl)

b = data.head(20)
Bp = b['BloodPressure']
plt.plot(Bp)

c = data.head(20)
Pr = c['Pregnancies']
plt.plot(Pr)

d = data.head(20)
St = d['SkinThickness']
plt.plot(St)

e = data.head(20)
Ins = e['Insulin']
plt.plot(Ins)

f = data.head(20)
Bmi = f['BMI']
plt.plot(Bmi)

g = data.head(20)
Dpf = g['DiabetesPedigreeFunction']
plt.plot(Dpf)

h = data.head(20)
Age = h['Age']
plt.plot(Age)

i = data.head(20)
Oc = i['Outcome']
plt.plot(Oc)
plt.title("Diabetes")
plt.show()
