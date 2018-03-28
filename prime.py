def prime(a):
	if a==2:	
		print("not a prime no")
	else:
		
		for b in range(2,a):
			if a%b==0:
				print("not a prime no")
				break
			else:
				print("prime no.")

val=int(input("enter a no."))
prime(val)


			
