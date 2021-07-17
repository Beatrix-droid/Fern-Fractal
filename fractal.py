import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

#defining the functions that draw the fern

def f_1(x,y):
	return [0.00 * x + 0.00 * y, 0.00 * x + 0.16 * y]
def f_2(x,y):
	return [0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6]
def f_3(x,y):
	return [0.20 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6]
def f_4(x,y):
	return [-0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44]

#randomly pick a function to draw
functions = [f_1, f_2, f_3, f_4]
width, height = 500, 500
fern_image = np.zeros((width, height))
points = 10000
x, y = 0, 0


for i in range(points):
	function = np.random.choice(functions, p=[0.01, 0.85, 0.07, 0.07])
	x,  y = function(x,y)
	#shift the image
	ix, iy = int(width / 2 + x * width / 10), int(y * height/12)
	#set the value of the points == 1 so that they show up on the graph
	fern_image[iy, ix] = 1

#plotting the points (in reverse order so that the image does not show
#upside down
plt.imshow(fern_image[::-1, :], cmap = cm.Blues)
plt.show()
