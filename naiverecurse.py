
import os
import time
start_time = time.time()


inboard = """_,_,4,1,_,_,5,2,7
2,1,3,7,_,_,_,_,_
_,_,7,6,2,4,_,_,_
3,5,_,2,7,_,_,_,_
_,_,_,_,3,_,8,7,5
_,4,_,_,_,6,_,1,3
4,7,2,_,1,_,_,5,_
_,3,1,_,6,2,_,_,9
9,_,_,_,_,_,1,8,_"""


inboards = """_,_,4,1,8,3,5,2,7
2,1,3,7,9,5,4,6,8
5,8,7,6,2,4,9,3,1
3,5,8,2,7,1,6,9,4
1,2,6,4,3,9,8,7,5
7,4,9,8,5,6,2,1,3
4,7,2,9,1,8,3,5,6
8,3,1,5,6,2,7,4,9
9,6,5,3,4,7,1,8,2"""

medboard = """2,_,_,6,_,_,_,_,_
6,_,_,_,5,1,_,4,_
_,7,_,_,_,_,_,_,_
_,_,_,_,3,_,_,1,4
_,_,5,_,6,_,_,_,_
_,1,9,_,4,_,_,5,_
_,_,6,_,_,_,_,2,5
_,_,_,9,_,_,_,8,_
8,9,_,_,_,_,4,_,_"""

hardboard = """_,_,6,_,9,_,_,_,_
1,7,_,_,_,3,_,9,_
_,_,_,7,_,_,_,_,5
_,_,_,5,_,_,6,_,_
_,9,_,_,3,_,2,_,_
_,_,4,_,_,2,1,_,_
_,_,_,9,7,8,_,_,_
_,4,_,_,_,5,_,8,_
_,_,_,_,_,6,_,_,_"""


a8 = """_,_,_,_,3,_,9,_,4
_,_,_,_,_,_,_,_,6
8,_,_,_,_,5,_,_,_
_,_,_,9,_,_,_,_,_
7,_,_,_,_,_,_,8,_
_,_,_,6,_,8,_,_,_
_,1,6,_,_,_,_,_,_
4,_,9,_,_,_,_,_,_
_,_,_,_,7,_,_,3,_"""

a5 = """_,_,_,1,_,_,_,9,3
1,_,4,_,6,_,_,_,_
5,3,_,_,7,_,_,_,_
2,7,_,_,_,6,_,_,_
_,1,_,_,_,_,_,5,_
_,_,_,9,_,_,_,4,7
_,_,_,_,3,_,_,6,2
_,_,_,_,4,_,8,_,9
7,6,_,_,_,1,_,_,_"""

a6 = """8,_,_,_,_,_,_,_,_
_,_,3,6,_,_,_,_,_
_,7,_,_,9,_,2,_,_
_,5,_,_,_,7,_,_,_
_,_,_,_,4,5,7,_,_
_,_,_,1,_,_,_,3,_
_,_,1,_,_,_,_,6,8
_,_,8,5,_,_,_,1,_
_,9,_,_,_,_,4,_,_"""


a7 = """_,_,_,2,_,_,_,_,_
_,_,_,_,9,_,5,_,_
1,_,6,_,_,_,_,4,_
_,_,_,_,_,_,_,8,_
4,_,_,_,_,6,_,_,_
_,9,_,3,_,_,2,_,_
_,_,7,_,_,_,_,_,_
_,8,_,_,_,4,_,6,_
_,2,_,_,_,_,_,_,_"""

CURRENT_BOARD = a5

# "7, 6, 2"

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

class Node(object):
    """holds a node of the sudoku Node"""

    def __init__(self, data, id):
        super(Node, self).__init__()
        self.data = data
        self.id = id

    def __repr__(self):
        return str([self.data, self.id])



def calcAllNodes():
    id = 0
    for x in CURRENT_BOARD.split("\n"):
        for z in x.split(","):
            allnodes.append(Node(z, id))
            id = id + 1

# print(allnodes)


def calcBlankNodes():
    for x in allnodes:
        if x.data == '_':
            blanknodes.append(x)

calcAllNodes()
calcBlankNodes()

# void findSolutions(n, other params) :
#     if (found a solution) :
#         solutionsFound = solutionsFound + 1;
#         displaySolution();
#         if (solutionsFound >= solutionTarget) :
#             System.exit(0);
#         return
#
#     for (val = first to last) :
#         if (isValid(val, n)) :
#             applyValue(val, n);
#             findSolutions(n+1, other params);
#             removeValue(val, n);


def findSolutions(nodeindex):
    if (isSolved(allnodes)):
        return True
    else:
        nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        if nodeindex < len(blanknodes):
            relevantcliques = []
            for clique in cliques:
                if blanknodes[nodeindex].id in clique:
                    relevantcliques.append(clique)
            # print()
            # print("I AM NODE", blanknodes[nodeindex].id)
            # print(relevantcliques)

            for clique in relevantcliques:
                for x in clique:
                    if allnodes[x].data in nums:
                        nums.remove(allnodes[x].data)

        # print(nums)

        for x in nums:
            if nodeindex < len(blanknodes):
                blanknodes[nodeindex].data = x
                if (findSolutions(nodeindex + 1)):
                    return True
                else:
                    blanknodes[nodeindex].data = '_'
            else:
                return False


def isSolved(in_nodes):
    for x in cliques:
        nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for y in x:
            if allnodes[y].data in nums:
                nums.remove(allnodes[y].data)
        if (len(nums) > 0):
            return False
    return True


findSolutions(0)
print("--- %s seconds ---" % (time.time() - start_time))

def printer():
    for x in allnodes:
        print(x.data, end = "")
        if (x.id + 1) % 9 == 0:
            print()


printer()