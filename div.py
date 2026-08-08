import numpy as np
import pandas as pd
from scipy import stats
print("Libraries imported successfully!")


arr=np.array([10,20,30,40,50])
print(arr)
print(type(arr))


print(arr[0]);print(arr[-1]);print(arr[2])


print(arr[1:4])
print(arr[:3])
print(arr[2:])
print(arr[::-1])


x=np.arange(12)
print(x.reshape(3,4))
print(x.reshape(2,6))
print(x.reshape(4,3))


np.random.seed(42)
print(np.random.rand(3,3))
print(np.random.randint(1,100,10))
print(np.random.randn(5))


a=np.array([10,20,30,40,50])
print("Sum:",np.sum(a))
print("Mean:",np.mean(a))
print("Median:",np.median(a))
print("Std:",np.std(a))
print("Variance:",np.var(a))
print("Min:",np.min(a))
print("Max:",np.max(a))
print("ArgMin:",np.argmin(a))
print("ArgMax:",np.argmax(a))


data=[10,20,20,30,40,40,40]
print(stats.mode(data,keepdims=True))


data=np.array([10,20,np.nan,40,50,np.nan])
print(data)
print(np.isnan(data))
print("Missing:",np.isnan(data).sum())


print("Mean:",np.nanmean(data))
print("Median:",np.nanmedian(data))
print("Std:",np.nanstd(data))


mean=np.nanmean(data)
filled=np.where(np.isnan(data),mean,data)
print(filled)


df = pd.DataFrame({
    'Age': [20,22,np.nan,25,30],
    'Salary': [20000,np.nan,35000,40000,50000]
})

print(df)
print(df.isnull())
print(df.isnull().sum())
print(df.fillna(df.mean(numeric_only=True)))
print(df.dropna())


arr=np.array([5,2,3,2,5,5,1])
print(np.unique(arr))
v,c=np.unique(arr,return_counts=True)
print(v)
print(c)
print(np.sort(arr))
print(arr[arr>2])