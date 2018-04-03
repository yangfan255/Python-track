count = 3
password = '56'

while count:
	guess = input('please guess a number:')
	if guess == password:
		print('good')
		break
	elif '*' in guess:
		print('* can\'t be included, you have', count, 'chance')
		continue
	elif guess != password:
		print('that is not correct, you have', count-1, 'chance')
	count -= 1
	
