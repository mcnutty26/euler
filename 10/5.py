i = 0
j = 0
done = False
while not done:
	i += 2
	j = 11
	done = True
	while j <= 20:
		if i%j != 0:
			done = False
			break
		else:
			j+=1
print(i)