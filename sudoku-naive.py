import sys
import time

start_time = time.time()




inboard = """6,9,4,1,8,3,5,2,7
2,1,3,7,9,5,4,6,8
5,8,7,6,2,4,9,3,1
3,5,8,2,7,1,_,9,4
1,2,6,4,3,9,8,7,5
7,4,9,8,5,6,2,1,3
4,7,2,9,1,8,3,5,6
8,3,1,5,6,2,7,4,9
9,6,5,3,4,7,1,8,2"""

# "7, 6, 2"

cliques=[[0,1,2,3,4,5,6,7,8],\
[9,10,11,12,13,14,15,16,17],\
[18,19,20,21,22,23,24,25,26],\
[27,28,29,30,31,32,33,34,35],\
[36,37,38,39,40,41,42,43,44],\
[45,46,47,48,49,50,51,52,53],\
[54,55,56,57,58,59,60,61,62],\
[63,64,65,66,67,68,69,70,71],\
[72,73,74,75,76,77,78,79,80],\
[0,9,18,27,36,45,54,63,72],\
[1,10,19,28,37,46,55,64,73],\
[2,11,20,29,38,47,56,65,74],\
[3,12,21,30,39,48,57,66,75],\
[4,13,22,31,40,49,58,67,76],\
[5,14,23,32,41,50,59,68,77],\
[6,15,24,33,42,51,60,69,78],\
[7,16,25,34,43,52,61,70,79],\
[8,17,26,35,44,53,62,71,80],\
[0,1,2,9,10,11,18,19,20],\
[3,4,5,12,13,14,21,22,23],\
[6,7,8,15,16,17,24,25,26],\
[27,28,29,36,37,38,45,46,47],\
[30,31,32,39,40,41,48,49,50],\
[33,34,35,42,43,44,51,52,53],\
[54,55,56,63,64,65,72,73,74],\
[57,58,59,66,67,68,75,76,77],\
[60,61,62,69,70,71,78,79,80]\
]



class Node(object):
	"""holds a node of the sudoku Node"""

	def __init__(self, data, id):
		super(Node, self).__init__()
		self.data = data
		self.id = id

	def __repr__(self):
		return str([self.data, self.id])



allnodes = []

id = 0
for x in inboard.split("\n"):
	for z in x.split(","):
		allnodes.append(Node(z, id))
		id = id + 1;

# print(allnodes)

blanknodes = []
for x in allnodes:
	if x.data == '_':
		blanknodes.append(x)



# print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa\n\n\n")

# print(allnodes)


# blanknodes[0].data = 6
# print(blanknodes)



def isSolved(in_nodes):
	for x in cliques:
		# print(x)
		nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
		for y in x:
			if allnodes[y].data in nums:
				nums.remove(allnodes[y].data)
		if (len(nums) > 0):
			return False
	return True

# print(isSolved(allnodes))



e = ""
s = ""
for x in range(1, len(blanknodes) + 1):
	e = e + "1"
	s = s + "9"


# print(isSolved(allnodes))


for x in range(int(e), int(s) + 1):
	for n, y in enumerate(str(x)):
		blanknodes[n].data = y
		# print("\n\n\n")
		# print(allnodes)
	if isSolved(allnodes):
		print(allnodes)
		print("--- %s seconds ---" % (time.time() - start_time))
		sys.exit(1)
	# print(blanknodes)


# print(e, s)
#
# print(isSolved(allnodes))
