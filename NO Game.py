import random as r
num=r.randrange(100)
guess =5

while guess >=0:
	your_guess = int(input("enter your guess"))

	def check(x):
		if your_guess == x:
			print('you won the game')
		elif your_guess > x:
			print('you are close, keep trying lower values')
		else:
			print('you are close, keep trying higher values')
	if guess >1:
		check(num)
	elif guess == 1:
		check(num)
		print('this is your last chance,make the most of it')
	else:
		print('you lost')
	guess = guess-1

print("The value was",num)