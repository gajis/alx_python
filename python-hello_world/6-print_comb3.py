for x in range(10):
	for i in range(x + 1, 10):
		end= ", " if x < 8 else "\n"
		print("{:02d}".format(x * 10 + i), end=end) 
