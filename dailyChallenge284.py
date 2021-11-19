

def generate(n, k):
	list = {}					# später große Liste

	sub_list = []				# Liste bei der die einzelnen Zahlen inkrementiert werden
	end_list = []

	for i in range(n):
		sub_list.append(1)
		end_list.append(k)

	basic_list = sub_list
	print(basic_list)

	list.add(tuple(sub_list))

	index = 0

	while sub_list != end_list:
		space_found = False
		sub_list_space_search = 0
		while not space_found:
			if sub_list[sub_list_space_search] != k:
				sub_list[sub_list_space_search] = sub_list[sub_list_space_search] + 1
				for j in range(sub_list_space_search):
					sub_list[j] = 1
				space_found = True
			else:
				sub_list_space_search += 1
		list.add(tuple(sub_list))

	return list

x = generate(3,4)

print(x)
