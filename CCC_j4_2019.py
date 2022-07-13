string = str(input())
class Grid():
    def __init__(self):
        self.grid = [['1', '2'],['3', '4']]
    def hFlip(self):
        self.grid = [[self.grid[1][0], self.grid[1][1]], [self.grid[0][0], self.grid[0][1]]]
    def vFlip(self):
        self.grid = [[self.grid[0][1], self.grid[0][0]], [self.grid[1][1], self.grid[1][0]]]
      
grid = Grid()


for i in string:
    if i == 'V':
        grid.vFlip()
    elif i == 'H':
        grid.hFlip()

for j in grid.grid:
    for i in j:
      print(i,end=" ")
    print('')