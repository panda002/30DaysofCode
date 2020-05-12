arr1 = [1, 2, 3, 4, 5]
arr2 = [0, 0, 0, 10, 10]

# median of arr1 and arr2

arrFinal = []
if len(arr1) > len(arr2):
    maxLen = len(arr1)
else:
    maxLen = len(arr2)

for i in range(maxLen):
    for j in range(maxLen):
        if arr1[i] < arr2[j]:
            arrFinal.append(arr1[i])
            arr1.pop(i)
            print(arr1)
            break
        else:
            arrFinal.append(arr2[j])
            arr1.pop(j)
            print(arr2)
            break

print(arrFinal)

