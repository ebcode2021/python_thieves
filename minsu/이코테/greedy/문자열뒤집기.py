a = input()
i = len(list(filter(None, a.split("1"))))
j = len(list(filter(None, a.split("0"))))
ref = i if i < j else j
print(ref)