
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
		self.id = id

	def __repr__(self):
		return str([self.data, self.id])



allnodes = []

id = 0
for x in inboard.split("\n"):
	for z in x.split(","):
		allnodes.append(Node(z, id))
		id = id + 1;


blanknodes = []
for x in allnodes:
	if x.data == '_':
		blanknodes.append(x)






# private boolean betaPlacer(int x, int y){
# 	if (maze[x][y] == 'E'){
# 		return true;
# 	}
# 	for (int c = 0; c < 4; c++){
# 		if (maze[x][y] == ' ' || maze[x][y] == '.'|| maze[x][y] == 'S'){
# 			maze[x][y] = '@';
# 			steps++;
# 			if (animated) debug();
# 			// debug();
# 			if (betaPlacer(x+moves[c][0], y+moves[c][1])){
# 				if (animated) debug();
# 				return true;
# 			}
# 			// debug();
# 			maze[x][y] = '.';
# 			steps--;
# 		}
# 		else if (maze[x][y] == 'S') {
# 		}
# 	}
# 	return false;
# }




print(blanknodes)
