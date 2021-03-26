# brooleen true/false
x = 5
print(x == 5) # '==' make sure if left is equal to right
print(x != 5)
print(x > 4)
print(x < 4)

# if 
rain = input('is there raining today:')
if rain == 'yes': #true, "if" should be followed by a question, ":"is a start of a list
	print('bring umbrella')
	print('buy cookies')
	print('watch moive at home')
	if x > 3:
		print('x  is larger than 3')

age = input('please input your age:') #str
age = int(age) #casting from str to int that origin value can be replaced
if age >= 20: # then # can be compared
	print('Congradulation, you can vote!')

# test: set up a formula from C to F
c = input('please enter temperature in celsius:')
c = float(c) #compared to int, float can output decimal value
f = c * 9 / 5 + 32
print('temperature in fahrenheit:', f)
