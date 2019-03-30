def test_sum():
	assert sum([1,2,3])==6, "list sum Should be 6"

def test_sum_tuple():
	assert sum((1,2
		,3))==6, "Tuple sum Should be 6"

if __name__ == '__main__':
	test_sum()
	test_sum_tuple()
	print("Everything passed")