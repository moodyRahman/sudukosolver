
inboard = """_,_,4,1,_,_,5,2,7
2,1,3,7,_,_,_,_,_
_,_,7,6,2,4,_,_,_
3,5,_,2,7,_,_,_,_
_,_,_,_,3,_,8,7,5
_,4,_,_,_,6,_,1,3
4,7,2,_,1,_,_,5,_
_,3,1,_,6,2,_,_,9
9,_,_,_,_,_,1,8,_"""


class Node(object):
	"""holds a node of the sudoku Node"""

	def __init__(self, data, id):
		super(Node, self).__init__()
		self.data = data

	def __str__(self)



allnodes = []

for x in inboard.split("\n"):
	for z in x.split(","):
		allnodes.append(Node(z, 5))

print(allnodes)
