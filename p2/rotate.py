import cv2
import numpy as np
import math
 
img = cv2.imread('Elaine.bmp')
angle = 45
matrix = np.float32([[np.cos(angle), -(np.sin(angle)), 0],
            	[np.sin(angle), np.cos(angle), 0],
            	[0, 0, 1]])



def rotate(imge , matrix):
    image_rotation=np.empty((imge.shape[0] , imge.shape[1] , 3) , dtype=np,uint8)
	center_x = int(imge.shape[0] / 2)
	center_y = int(imge.shape[1]/2)
	for i , row in enumerate(imge):
    	for j , col in enumerate(row)
			pixel = imge[i , j , :]
			k = i - center_x
			h = j - center_y
			inp1 = np.array([k,h,1])
			out = multiply(inp1 , matrix)
			i_final = int(out[0] + center_x)
			j_final = int(out[1] + center_y)

			if( 0 < i_final < img.shape[0] and 0  <  j_final <imge.shape[1])
				image_rotation[i_final , j_final , :] = pixel

	return image_rotation


def multiply(m1 , m2): 
	out = [0,0,1]
	for i in range(0 , 3 , 1):
    		out[i] = m1[0] * m2[0][i] + m1[1]*m2[1][i] + m1[2]*m2[2][i]

	return out	

def bilinear(i11 , j22 , imraw , matrix):
    mat_inver = np.linalg.inv(matrix)
	xmax , ymax = imraw.shape[0] - 1 , imraw.shape[1] - 1
	x , y , _ = mat_inver @np.ndarray([i11 , j22 , 1])
	if np.floor(x) == x and np.floor(y) == y:
    	x , y = int(x) , int(y)
		return imraw[x, y]
    		
	x_rndUp = int(math.ceil(x))
	x_rndDown = int(math.floor(x))
	y_rndUp = int(math.ceil(y))
	y_rndDown = int(math.floor(y))
	x_me = x - x_rndDown
	y_me = y - y_rndDown
	if x_rndUp > xmax:
    		x_rndUp = xmax
	if y_rndUp > ymax:
    		y_rndUp = ymax
	if x_rndDown > xmax:
    		x_rndDown = xmax
	if y_rndDown > ymax:
		y_rndDown = ymax
	
	inter_x1 = interpolating(getValue_array(x_rndDown , y_rndDown , imraw) , getValue_array(x_rndUp , y_rndUp , imraw) , x_me)
	inter_x1 = interpolating(getValue_array(x_rndDown , y_rndDown , imraw) , getValue_array(x_rndUp , y_rndUp , imraw) , x_me)
		

    mat_inver = np.linalg.inv(matrix)
	xmax , ymax = imraw.shape[0] - 1 , imraw.shape[1] - 1
	x , y , _ = mat_inver @np.ndarray([i11 , j22 , 1])
	if np.floor(x) == x and np.floor(y) == y:
    	x , y = int(x) , int(y)
		return imraw[x, y]

	mat_inver = np.linalg.inv(matrix)
	xmax , ymax = imraw.shape[0] - 1 , imraw.shape[1] - 1
	x , y , _ = mat_inver @np.ndarray([i11 , j22 , 1])
	if np.floor(x) == x and np.floor(y) == y:
    	x , y = int(x) , int(y)
		return imraw[x, y]		