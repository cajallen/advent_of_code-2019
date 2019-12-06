import timeit

mycode = """def count_nums(_min, _max): 
	sum = 0
	#nondecreasing order rule also applies to the min and max
	#these two methods find the smallest number larger than min that abides by the rules, and the largest number smaller than min that also abides by the rules
	_min = [int(x) for x in str(_min)]
	_max = [int(x) for x in str(_max)]
	_min = find_real_min(_min)
	_max = find_real_max(_max)

	# first digit, clamps loop to min and max
	for x1 in range(_min[0], _max[0] + 1):
		# second digit, clamps loop to min or max if prevous digits are clamped to min or max, otherwise it does all non-decreasing numbers
		for x2 in range(_min[1] if [x1] == _min[:1] else x1,  _max[1] + 1 if [x1] == _max[:1] else 10):
			for x3 in range(_min[2] if [x1,x2] == _min[:2] else x2,  _max[2] + 1 if [x1,x2] == _max[:2] else 10):
				for x4 in range(_min[3] if [x1,x2,x3] == _min[:3] else x3, _max[3] + 1 if [x1,x2,x3] == _max[:3] else 10):
					for x5 in range(_min[4] if [x1,x2,x3,x4] == _min[:4] else x4, _max[4] + 1 if [x1,x2,x3,x4] == _max[:4] else 10):
						for x6 in range(_min[5] if [x1,x2,x3,x4,x5] == _min[:4] else x5, _max[5] + 1 if [x1,x2,x3,x4,x5] == _max[:5] else 10):
							if (check_dupe([x1,x2,x3,x4,x5,x6])):
								sum += 1
	return sum

def check_dupe(num):
	num = [0] + num + [0]
	for i in range(0, len(num) - 3):
		# num will be like [0, 1, 2, 3, 4, 5, 6, 0], 0 will never be equal to any of the items in num
		# we add the two numbers on the outside so we always have two numbers outside the pair to check inequality to
		if (num[i] != num[i+1] and num[i+1] == num[i+2] and num[i+2] != num[i+3]):
			return True
	return False

def find_real_min(_min):
	for i in range(len(_min)):
		_min[i] = max(_min[:i+1])
	return _min

def find_real_max(_max):
	for i in range(len(_max) - 1):
		if (_max[i] > _max[i + 1]):
			_max[i] -= 1
			return _max[:i+1] + [9] * (5 - i)

count_nums(372304,847060)"""

print (timeit.timeit(stmt = mycode, number = 1000))