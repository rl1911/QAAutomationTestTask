import tkinter as tk
import random
import numpy as np
from collections import deque

#set m*n map
m = 20
n = 15
start_point_x = 10
start_point_y = 10
map = [[0] * m for i in range(n)]

def getRandomCell():
    rand_m = random.randint(0, m-1)
    rand_n = random.randint(0, n-1)
    if map[rand_n][rand_m] == 0:
        map[rand_n][rand_m] = 1
    else:
        getRandomCell()

def getRaftStartEndPoint(m):
    rand_n = random.randint(0, n-1)    
    if rand_n != None and map[rand_n][m] == 0:        
        return rand_n
    else:
        return getRaftStartEndPoint(m)
    
root =tk.Tk()
root.geometry('800x600')
root.title('Canvas Demo')
tk_canvas = tk.Canvas(root, width=600, height=400, bg='white')
tk_canvas.pack(anchor=tk.CENTER, expand=True)

#fill 30% of map
slice_30_percentage = int(m*n//100*30)
while slice_30_percentage > 0:
    getRandomCell()
    slice_30_percentage -=1

#generate start and finish cell
raft_start_y = getRaftStartEndPoint(0)
map[raft_start_y][0] = 2
raft_finish_y = getRaftStartEndPoint(m-1)
map[raft_finish_y][m-1] = 3

data = np.array(map)

# Get number of rows and columns
numR = len(data)
numC = len(data[0])

# Find where start and finish are
s = np.where(data == 2)
sR = int(s[0])
sC = int(s[1])

e = np.where(data == 3)
eR = int(e[0])
eC = int(e[1])

# Declare arrays
visited = np.array([[False for x in range(numC)] for y in range(numR)])
prev = {(x,y):0 for x in range(numC) for y in range(numR)}

#Provide cardinal directions
dr = [-1, +1, 0, 0]
dc = [0, 0, +1, -1]

# Use queue data structure to keep track of row and column coordinates. 
# Using one queue for each dimension. Can sub with position pairs	
rq = deque([])
cq = deque([])

# Add first node and mark it visisted
rq.append(sR)
cq.append(sC)
visited[sR,sC] = True

reached_end = False

def explore(r, c):
	for i in range (0,4):
		rr = r + dr[i]
		cc = c + dc[i]

		if rr < 0 or cc < 0: continue
		if rr >= numR or cc >= numC: continue
		if visited[rr,cc]: continue
		if data[rr,cc] == 1: continue
		#if data[rr,cc] == 3: continue

		# Save parent node for use in path reconstruction
		node = (r,c)
		prev[(rr,cc)] = node 

		# Add adjacent unvisited neighbors to the queue
		rq.append(rr)
		cq.append(cc)

		visited[rr,cc] = True
	
def reconstruct_path():
	path = []
	xy = (eR, eC)
	path.append(xy) 
	while xy != s:
		path.append(prev[xy])
		xy = prev[xy] 
	path.reverse()
	return path

#draw generated map with start and finish cells
draw_start_point_y = start_point_y
for row in map:
    draw_start_point_x = start_point_x    
    for elem in row:
        if elem == 0:
             tk_canvas.create_rectangle(draw_start_point_x, draw_start_point_y, draw_start_point_x+10, draw_start_point_y+10, fill='#000000fff', outline="#000000")
        elif elem == 1:
             tk_canvas.create_rectangle(draw_start_point_x, draw_start_point_y, draw_start_point_x+10, draw_start_point_y+10, fill='#000fff000', outline="#000000")
        elif elem == 2 or elem == 3:
             tk_canvas.create_rectangle(draw_start_point_x, draw_start_point_y, draw_start_point_x+10, draw_start_point_y+10, fill='#fff000000', outline="#000000")     
        draw_start_point_x = draw_start_point_x + 10
    draw_start_point_y = draw_start_point_y + 10
root.update()
tk_canvas.after(5000,tk_canvas.delete('all'))

#search shortest path
#If start and finish cells bloked, program finishes with error. You have to run it again!!!
while len(rq) > 0 or len(cq) > 0: # Keep repeating until there are no nodes with unexplored edges
	# Remove the node you're about to explore the edges of
	r = rq.popleft()
	c = cq.popleft()
	if (r,c) == (eR,eC):
		reached_end = True
		break
	explore(r, c)

r_path = reconstruct_path()
path_x = 0
path_y = 0
for elements in r_path:   
     map[elements[0]][elements[1]] = 2 

#draw path
draw_start_point_y = start_point_y
for row in map:
    draw_start_point_x = start_point_x    
    for elem in row:
        if elem == 0:
             tk_canvas.create_rectangle(draw_start_point_x, draw_start_point_y, draw_start_point_x+10, draw_start_point_y+10, fill='#000000fff', outline="#000000")
        elif elem == 1:
             tk_canvas.create_rectangle(draw_start_point_x, draw_start_point_y, draw_start_point_x+10, draw_start_point_y+10, fill='#000fff000', outline="#000000")
        elif elem == 2 or elem == 3:
             tk_canvas.create_rectangle(draw_start_point_x, draw_start_point_y, draw_start_point_x+10, draw_start_point_y+10, fill='#fff000000', outline="#000000")                
        draw_start_point_x = draw_start_point_x + 10
    draw_start_point_y = draw_start_point_y + 10

root.update()
root.mainloop()
