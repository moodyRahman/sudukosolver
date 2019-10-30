#! /usr/bin/python3
import sys

finp = open(sys.argv[1], "r").read()
print(finp)
# finp = """B1-1,Bad,incorrect
# 9,6,4,1,8,3,5,2,7
# 2,1,3,7,9,5,4,6,8
# 5,8,7,6,2,4,9,3,1
# 3,5,8,2,7,1,6,9,4
# 1,2,6,4,3,9,8,7,5
# 7,4,9,8,5,6,2,1,3
# 4,7,2,9,1,8,3,5,6
# 8,3,1,5,6,2,7,4,9
# 9,6,5,3,4,7,1,8,2
#
# B3-1,UGLY!,incorrect
# 3,5,6,2,9,4,8,7,1
# 1,7,8,6,5,3,4,9,5
# 4,2,9,7,8,1,3,6,5
# 8,1,2,5,4,9,6,3,7
# 6,9,5,1,3,7,2,4,8
# 7,3,4,8,6,2,1,5,9
# 2,6,3,9,7,8,5,1,4
# 9,4,1,3,2,5,7,8,6
# 2,8,7,4,1,6,9,2,3"""


allboards = finp.split("\n\n")[:-1]

#
# print("#############\n\n\n")

class Node(object):
    """holds a node of the sudoku Node"""

    def __init__(self, data, id):
        super(Node, self).__init__()
        self.data = data
        self.id = id

    def __repr__(self):
        return str([self.data, self.id])


class Board(object):
    """holds a game"""
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

    def __init__(self, barray):
        super(Board, self).__init__()
        barrayarr = barray.split("\n")
        self.name = barrayarr[0]
        self.barray = "\n".join(barrayarr[1:])

    def generateNodes(self):
        anodes = []
        id = 0
        for x in self.barray.split("\n"):
            for z in x.split(","):
                anodes.append(Node(z, id))
                id = id + 1
        self.allnodes = anodes

    def generateBlankNodes(self):
        bnodes = []
        for x in self.allnodes:
            if x.data == '_':
                bnodes.append(x)
        self.blanknodes = bnodes

    def check(self):
        for x in self.cliques:
            # print(x)
            nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            for y in x:
                if self.allnodes[y].data in nums:
                    nums.remove(self.allnodes[y].data)
            if (len(nums) > 0):
                return False
        return True

    def swaptest(self):
        x = self.allnodes[0]
        y = self.allnodes[1]
        # print(x.id, y.id)
        z = x.id
        x.id = y.id
        y.id = z
        # print(x.id, y.id)
        # print(self.check())

    def swapper(self):
        for nx, x in enumerate(self.allnodes):
            for ny, y in enumerate(self.allnodes):
                self.currid = [x.id, y.id]
                z = x.id
                x.id = y.id
                y.id = z
                nz = self.allnodes[nx]
                self.allnodes[nx] = self.allnodes[ny]
                self.allnodes[ny] = nz
                if (self.check()):
                    # print("we swapped", currid[0], currid[1])
                    return True
                z = x.id
                x.id = y.id
                y.id = z
                nz = self.allnodes[nx]
                self.allnodes[nx] = self.allnodes[ny]
                self.allnodes[ny] = nz

    # def print(self):
    #     print(self.allnodes)
    # def printbarray(self):
    #     print(self.barray)
    # def printAllNodesPretty(self):
    #     out = ""
    #     for x in self.allnodes:
    #         out = out + x.data
    #         out = out + ", "
    #         if x.id%8 == 0:
    #             out+="\n"
    #     print(out)


b = Board(allboards[1])


allnodeboards = []
for x in allboards:
    allnodeboards.append(Board(x))


f= open(sys.argv[2],"w")
out = ""



for z in allnodeboards:
    z.generateNodes()
    z.swapper()
    out = out + str(z.currid[0])
    out = out + ","
    out = out + str(z.currid[1])
    out = out + "\n"

out = out.strip()

f.write(out)

f.close()
