"""
Prime Detector
	by Shunkan U
v1 2023-06-06
contents:
	Detect & count primes
	Patched grotendieck prime :)
	Some debug features
"""
import math
# variables
num = 0
prime_count = 0
init_num = 0
max_num = 0
int_init_num = False
int_max_num = False
is_prime = False
grothendieck = False

debug = False
debug_order = 0
# main
try:
	while int_init_num == False or init_num < 1:
		init_num = input("initial number(>= 2): ")
		if init_num == "debug":
			debug = True
			print("debug mode activated")
		elif init_num == "57 is prime":
			grothendieck = True
			print("57 is prime :)")
		else:
			init_num = int(init_num)
			int_init_num = True if type(init_num) == int else False
	while int_max_num == False or max_num < init_num:
		max_num = int(input("max number: "))
		int_max_num = True if type(max_num) == int else False
	# find primes
	num = init_num
	print("primes between {} and {}:".format(init_num, max_num))
	while num <= max_num:
		if num == 57 and grothendieck == True: print(num)
		else:
			is_prime = True
			i = 2
			while i <= math.pow(num, 0.5) and is_prime == True:
				if num % i == 0: is_prime = False
				i += 1
				debug_order += 1
			if is_prime == True:
				prime_count += 1
				print(num)
		num += 1
	print("number of primes between {} and {}: {}".format(init_num, max_num, prime_count))
	if debug == True: print("orders: {}".format(debug_order))
except ValueError:
	print("The input must be a number.")
