import sys

filein = sys.argv[1]
fileout = sys.argv[2]
id = sys.argv[3]

f = open(filein, "r")

allin = f.read()

allin = allin.split("\n\n")

lookingat = ""

for x in allin:
    print("------------------------------------------")
    x = x.strip("\n")
    for z in x.split("\n")[:-9]:
        z = z.replace("\n", "")
        print(z.split(","))
        if id == z.split(",")[0]:
            print("got here")
            lookingat = x
    print("------------------------------------------\n")

print("here")
print(lookingat)




# "7, 6, 2"
class Node(object):
    """holds a node of the sudoku Node"""

    def __init__(self, data, id):
        super(Node, self).__init__()
        self.data = data
        self.id = id

    def __repr__(self):
        return str([self.data, self.id])

class Board(object):
    """holds a sudoku Board"""

    def __init__(self, arg, animation = False, delay = .1):
        super(Board, self).__init__()
        self.CURRENT_BOARD = arg
        self.animation = animation
        self.delay = delay

    steps = 0

    cliques = [[0, 1, 2, 3, 4, 5, 6, 7, 8],
               [9, 10, 11, 12, 13, 14, 15, 16, 17],
               [18, 19, 20, 21, 22, 23, 24, 25, 26],
               [27, 28, 29, 30, 31, 32, 33, 34, 35],
               [36, 37, 38, 39, 40, 41, 42, 43, 44],
               [45, 46, 47, 48, 49, 50, 51, 52, 53],
               [54, 55, 56, 57, 58, 59, 60, 61, 62],
               [63, 64, 65, 66, 67, 68, 69, 70, 71],
               [72, 73, 74, 75, 76, 77, 78, 79, 80],
               [0, 9, 18, 27, 36, 45, 54, 63, 72],
               [1, 10, 19, 28, 37, 46, 55, 64, 73],
               [2, 11, 20, 29, 38, 47, 56, 65, 74],
               [3, 12, 21, 30, 39, 48, 57, 66, 75],
               [4, 13, 22, 31, 40, 49, 58, 67, 76],
               [5, 14, 23, 32, 41, 50, 59, 68, 77],
               [6, 15, 24, 33, 42, 51, 60, 69, 78],
               [7, 16, 25, 34, 43, 52, 61, 70, 79],
               [8, 17, 26, 35, 44, 53, 62, 71, 80],
               [0, 1, 2, 9, 10, 11, 18, 19, 20],
               [3, 4, 5, 12, 13, 14, 21, 22, 23],
               [6, 7, 8, 15, 16, 17, 24, 25, 26],
               [27, 28, 29, 36, 37, 38, 45, 46, 47],
               [30, 31, 32, 39, 40, 41, 48, 49, 50],
               [33, 34, 35, 42, 43, 44, 51, 52, 53],
               [54, 55, 56, 63, 64, 65, 72, 73, 74],
               [57, 58, 59, 66, 67, 68, 75, 76, 77],
               [60, 61, 62, 69, 70, 71, 78, 79, 80]
               ]

    allnodes = []
    blanknodes = []





    def calcAllNodes(self):
        id = 0
        for x in CURRENT_BOARD.split("\n"):
            for z in x.split(","):
                self.allnodes.append(Node(z, id))
                id = id + 1

    # print(allnodes)


    def calcBlankNodes(self):
        for x in self.allnodes:
            if x.data == '_':
                self.blanknodes.append(x)

    def findSolutions(self, nodeindex):
        if (self.isSolved(self.allnodes)):
            return True
        else:
            nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            if nodeindex < len(self.blanknodes):
                relevantcliques = []
                for clique in self.cliques:
                    if self.blanknodes[nodeindex].id in clique:
                        relevantcliques.append(clique)

                for clique in relevantcliques:
                    for x in clique:
                        if self.allnodes[x].data in nums:
                            nums.remove(self.allnodes[x].data)

            for x in nums:
                if nodeindex < len(self.blanknodes):
                    if self.animation:
                        print("\033[2J")
                        self.printer()
                        time.sleep(self.delay)
                        print("\033[2J")
                    self.blanknodes[nodeindex].data = x
                    self.steps = self.steps + 1
                    if (self.findSolutions(nodeindex + 1)):
                        return True
                    else:
                        self.blanknodes[nodeindex].data = '_'
                else:
                    return False


    def isSolved(self, in_nodes):
        for x in self.cliques:
            nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            for y in x:
                if self.allnodes[y].data in nums:
                    nums.remove(self.allnodes[y].data)
            if (len(nums) > 0):
                return False
        return True

    def printer(self):
        for x in self.allnodes:
            print(x.data, end = "")

            if (x.id + 1) % 3 == 0:
                print("|", end = "")
            if (x.id + 1) % 9 == 0:
                print("")
            if (x.id + 1) % 27 == 0:
                print("############")
        print(self.steps, "iteration")

    def solve(self, printt = False):
        self.calcAllNodes()
        self.calcBlankNodes()
        self.findSolutions(0)
        if (printt):
            soard.printer()



# soard = Board(CURRENT_BOARD)
# soard.solve(printt = True)
