import cv2
import numpy as np
from matplotlib import pyplot as plt


def op_XOR(image1, image2):

	img1 = cv2.cvtColor(image1, cv2.cv2.COLOR_BGR2GRAY)

	img2 = cv2.cvtColor(image2, cv2.cv2.COLOR_BGR2GRAY)

	img1 = img1.astype(int)
	img2 = img2.astype(int)



	img2.shape = img1.shape #Adecuamos los tamaños de Ambos archivos para que sean iguales

	alto1,ancho1 = img1.shape
	#alto2,ancho2 = img2.shape
	##################NOT####################
	def NOT(imagen):
		alto1,ancho1 = imagen.shape
		res=imagen
		for i in range(alto1):
		    for j in range(ancho1):
		        img = abs((255-imagen[i][j]))
		        
		        if (img == 0):
		            res[i][j] = 0
		        else:
		            res[i][j] = img
		return res




	#################Threshold#####################
	def Thresholding(imagen):
		alto,ancho = imagen.shape
		result = imagen
		for x in range(alto):
			for y in range(ancho):
				if (10 < imagen[x][y] and imagen[x][y] <100):
					result[x,y]=0
				else:
					result[x,y]=255
		return result



	###########################XOR###########

	img1Not=NOT(img1)
	img2Not=NOT(img2)
	img1Bin=Thresholding(img1Not)
	img2Bin=Thresholding(img2Not)
	img1Bin=NOT(img1Bin)
	img2Bin=NOT(img2Bin)

	c=30
	for i in range(alto1):
	    for j in range(ancho1):
	        img = abs((img1Bin[i][j] ^ img2Bin[i][j]))
	        
	        if (img == 0):
	            img1[i][j] = 0
	        else:
	            img1[i][j] = img
	        
	return img1

##
imagen1 = cv2.imread("log_3.png")
imagen2 = cv2.imread("log_4.png")
result = op_XOR(imagen1, imagen2)
cv2.imwrite("resXOR.png", result)
cv2.waitKey(0)    
