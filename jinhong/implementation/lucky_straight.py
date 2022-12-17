score = input()
half = len(score)//2
left = [int(i) for i in score[:half]]
right = [int(i) for i in score[half:]]
print("LUCKY") if sum(left) == sum(right) else print("READY")