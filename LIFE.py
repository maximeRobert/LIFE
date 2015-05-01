import random;
import time;

def printGrid(_grid, _size):
    for i in range(_size):
        for j in range(_size):
            if(_grid[i][j] == 1):
                print ('X'),
            else:
                print (' '),
        print
    print "\n\n"

def computeGrid(_grid, _size):
    ret = []
    for i in xrange(size):
        grid.append([]);
        for j in xrange(size):
            grid[i].append(0);
    for i in xrange(_size):
        ret.append([]);
        for j in xrange(_size):
            liveNeighbourgs = computeNeighbours(i, j, _grid, _size);
            if(_grid[i][j] == 1):
                if((liveNeighbourgs < 2) or (liveNeighbourgs > 3)):
                    ret[i].append(0);
                else:
                    ret[i].append(1);
            else:
                if(liveNeighbourgs == 3):
                    ret[i].append(1);
                else:
                    ret[i].append(0);
    return ret;
          
def computeNeighbours(x, y, _grid, _size):
    res = 0;
    for i in xrange(-1, 2):
        for j in xrange(-1, 2):
            if(i != 0 or j != 0):
                if((x + i) in xrange(0, _size)) and ((y + j) in xrange(0, _size)):
                    res += 1 if _grid[x + i][y + j] == 1 else 0;
    return res;
    
print("Hello!");

spawn = 0.20;
size = 30;
grid = [];

for i in xrange(size):
    grid.append([]);
    for j in xrange(size):
        if random.random() < spawn:
            grid[i].append(1);
        else:
            grid[i].append(0);
     
while True:
   printGrid(grid, size);
   time.sleep(0.5)
   grid = computeGrid(grid, size);