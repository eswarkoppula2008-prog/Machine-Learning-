import math
import sub as np
import pandas as pd
import matplotlib.pyplot as plt
import time

print("Libraries imported successfully!")


numbers=[1,2,3,4,5]
squares=[]
for n in numbers:
    squares.append(n*n)
print("Original:",numbers)
print("Squares:",squares)



arr=np.array([1,2,3,4,5])
print(arr)
print("Squares:",arr**2)



lst=list(range(1000000))
start=time.time()
[x*x for x in lst]
print("List time:",round(time.time()-start,4),"sec")

arr=np.arange(1000000)
start=time.time()
arr**2
print("NumPy time:",round(time.time()-start,4),"sec")


data={'Name':['Alice','Bob','Charlie','eswar','sai','naga sai','bhuvan','mln'],
'Age':[20,21,22,20,21,20,22,21],
'Marks':[85,90,88,79,75,76,80,95]}
df=pd.DataFrame(data)
print(df)


print(df.head())
print(df.describe())
print(df.info())

plt.plot(df['Name'],df['Marks'],marker='o')
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid(True)

plt.savefig("student.pdf")
plt.show()


from sklearn.linear_model import LinearRegression

X=df[['Age']]
y=df['Marks']

model=LinearRegression()
model.fit(X,y)

print("Coefficient:",model.coef_[0])
print("Intercept:",model.intercept_)
print("Prediction for Age=23:",model.predict([[23]])[0])
