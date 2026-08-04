import numpy as np
print("NumPy version:", np.__version__)


a=np.array([10,20,30,40,50])
print(a)
print(type(a))


print("First:", a[0])
print("Third:", a[2])
print("Last:", a[-1])

print(a[1:4])
print(a[:3])
print(a[2:])
print(a[::-1])


b=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b)
print("Element:", b[1,2])
print("Second column:", b[:,1])
print("First row:", b[0,:])


x=np.arange(12)
print(x)
print(x.reshape(3,4))
print(x.reshape(2,6))
print(x.reshape(4,3))


np.random.seed(42)
print("Random floats")
print(np.random.rand(3,3))

print("\nRandom integers")
print(np.random.randint(1,101,10))

print("\nRandom normal distribution")
print(np.random.randn(5))

arr=np.array([5,10,15,20,25])
print("Sum:",np.sum(arr))
print("Mean:",np.mean(arr))
print("Max:",np.max(arr))
print("Min:",np.min(arr))
print("Std:",np.std(arr))