import common
import math #note, for this lab only, your are allowed to import math

def detect_slope_intercept(image):
	# PUT YOUR CODE HERE
	space=common.init_space(2000, 2000)
	for y in range(common.constants.WIDTH):
		for x in range(common.constants.HEIGHT):
			if image[y][x]==0:
				for i in range(2000):
					mm = 10-i/100
					bb = round(y-mm*x)
					if bb>-1000 and bb<=1000:
						space[bb+999][i] += 1
	curr=0
	kMax, jMax=0, 0
	line=common.Line()
	for k in range(2000):
		for j in range(2000):
			if space[k][j]>curr:
				curr=space[k][j]
				kMax, jMax=k, j
	# access the image using "image[y][x]"
	# where 0 <= y < common.constants.WIDTH and 0 <= x < common.constants.HEIGHT 
	# set line.m and line.b
	# to create an auxiliar bidimentional structure 
	# you can use "space=common.init_space(heigh, width)"
	
	line.m= round(10-jMax/100, 2)
	line.b= kMax-999
	return line

def detect_circles(image):
	# PUT YOUR CODE HERE
	space=common.init_space(200, 200)
	for y in range(common.constants.WIDTH):
		for x in range(common.constants.HEIGHT):
			if image[y][x]==0:
				for b in range(max(0,y-33), min(200,y+33)):
					for a in range(max(0,x-33), min(200,x+33)):
						if math.ceil(math.sqrt((y-b)**2 + (x-a)**2))==30:
							space[b][a]+=1 
	# access the image using "image[y][x]"
	# where 0 <= y < common.constants.WIDTH and 0 <= x < common.constants.HEIGHT 
	# to create an auxiliar bidimentional structure 
	# you can use "space=common.init_space(heigh, width)"
	#print(space) 
	curr=0
	for k in range(200):
		for j in range(200):
			if space[k][j]>93: curr+=1			#interesting threshold
	return curr
	