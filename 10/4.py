pals = set()
def ispalindrome(n):
	n_ = str(n)
	while len(n_) > 1:
		if n_[0] != n_[-1]:
			return False
		else:
			n_ = n_[1:]
			n_ = n_[0:-1]
	return True
for i in range(100,1000):
	for j in range(100,1000):
		if ispalindrome(i*j):
			pals.add(i*j)
print(max(pals))
	