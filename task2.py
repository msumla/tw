# class task2:
skip = 1 # no of skipped chair
remove = [] # no of removed chair

	
	# def fill_chairs(chs):
chairs = []
for c in range(2, 101):
	chairs.append(c)
print(chairs)
	# return chairs
			
	# fill_chairs(101)


def game_of_chairs(chs):
	global skip
	global remove
	for num in chs:
		if not len(chs) == 1:
			index = skip+num
			del chs[index]
			skip += 1
			game_of_chairs(chs)
		elif len(chs) == 1:
			print(chs[num])
			return chs[num]


game_of_chairs(chairs)

# chairs = list(range(1,101))
# rem = 0
# skip = 1
# left = 100
#
# while left == 1:
#     for ch in chairs:
#         chairs.pop(chairs[ch])
#         print ch
#         left-=1