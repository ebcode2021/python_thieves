array1 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result1 = sorted(array1)
print("result1 : ", result1)

#######

array2 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

array2.sort()
print("result2 : ", array2)

#######

array3 = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data) :
	return data[1]
result3 = sorted(array3, key=setting)
print(result3)