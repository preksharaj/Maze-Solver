
class Maze:
    #Dictionary which holds the indexes for moving right left up or down for a particular point
    dirs = {"right":{"dir":">","x":0,"y":1},"down":{"dir":"v","x":1,"y":0},"left":{"dir":"<","x":0,"y":-1},"up":{"dir":"^","x":-1,"y":0}}
    
    def __init__(self, maze):
        self.maze = self.load(maze)
	self.START = "D" # this is the Desk 
        self.END   = "C" # This is the coffee machine
        self.WALL  = "#"
        self.PATH  = " "
        self.FLOOR  = {self.PATH, self.END}  # Tuple to check if a path or a wall/desk is reached
	
    def load(self, file):
	lines = []
	m = []
	with open(file) as c:
	    for line in c:
		lines.append(line.strip("\r\n"))	
	    for l in lines:
		m.append(list(l))
	return m
	
    def __str__(self):
        return "\n".join(''.join(line) for line in self.maze)      

    def start(self):
        for x,line in enumerate(self.maze):
            try:
                y = line.index(self.START)
                return x, y
            except ValueError:
                pass

        # not found!
        raise ValueError("Start location not found")

    def solve(self, x, y):
        if self.maze[x][y] == self.END:
            # base case - The Coffee Machine has been found
            return True
        else:
            # search recursively in each direction from here
            #for dir in Maze.DIRS:
            for k,v in Maze.dirs.items():
		nx, ny = x + v['x'], y + v['y'] 
                if self.maze[nx][ny] in self.FLOOR:  # check if a particular direction has a path or not
                    if self.maze[x][y] != self.START: # don't overwrite START index
                        self.maze[x][y] = v['dir']  # mark direction chosen
                    if self.solve(nx, ny):          # recurse...
                        return True                 # solution found!

            # no solution found from this location
            if self.maze[x][y] != self.START:       # don't overwrite the start index 
                self.maze[x][y] = self.PATH         # clear failed search from map
            return False

def main():
    maze = Maze("mazefile.txt")
    print("\nOffice Maze:\n")
    print(maze)

    try:
        sx, sy = maze.start()
        print("\nSolution to Coffee:\n")
        if maze.solve(sx, sy):
            print(maze)
        else:
            print("    no solution found")
    except ValueError:
        print("Desk Not Found, Kindly check the input maze text file")

if __name__=="__main__":
    main()
