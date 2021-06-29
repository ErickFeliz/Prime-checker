while True:

	givennum = int(input("Enter a number: "))
	

	for i in range(2, givennum):
		if (givennum % i) == 0:
			print(givennum , "Is not a prime number")
			break
	else:
		print(givennum , "Is a prime number")

