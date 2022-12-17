def compress(s, slice):
	new_string = ''
	str_len = len(s)
	words = [s[i:i+slice] for i in range(0, str_len, slice)]
	count = 1
	for i in range(len(words) - 1):
		if words[i] == words[i + 1]:
			count += 1
		else:
			if count > 1:
				new_string += str(count)
			new_string += words[i]
			count = 1
	if count > 1:
		new_string += str(count)
	new_string += words[-1]
	return (len(new_string))
	
def solution(s):
	compressed = []
	max_slice = len(s) // 2
	for slice in range(1, max_slice + 1):
		compressed.append(compress(s, slice))
	return(min(compressed))