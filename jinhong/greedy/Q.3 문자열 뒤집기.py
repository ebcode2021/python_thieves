answer = 0
string = input()
for i in range(len(string) - 1):
	if string[i] == string[0] and string[i] != string[i+1]:
		answer += 1
print(answer)