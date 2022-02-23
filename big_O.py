# This is the Heap's algorithm, which is used for generating all possible permutation of n objects
# Another example could be the Travelling Salesman Problem

def Permutation(data,n):
    if n == 1:
        print(data)
        return
    for i in range(n):
        Permutation(data, n - 1)
        if n % 2 == 0:
            data[i], data[n-1] = data[n-1], data[i]
        else:
            data[0], data[n-1] = data[n-1], data[0]
data = [1,2]
Permutation(data,len(data))
