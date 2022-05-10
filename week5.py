#리스트

array = [1, 2, 3, 4, 5]
arr1 = ["afaf", "afaf", "asdfaf", "afafsdf"]
print(arr1[0][2])
print(len(arr1))

arr1.insert(2, "hello")

print(arr1)

arr1.pop(1)
del arr1[:2]

arr2 = []
arr2.clear()

"afaf" in arr1
"afaf" not in arr1

for x in range(1, 10):
    print(x)

for factor in arr1:
    print(factor)

for a in "afafasdfasdfa":
    print(a)