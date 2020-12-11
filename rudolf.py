import board
import neopixel
import time
import random
from matrix import *

pixel_pin = board.D18
# The number of NeoPixels
num_pixels = 256
# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.RGB
 
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.1, auto_write=False, pixel_order=ORDER
)

def rud(pos=10):
	row = 0
	column = pos
	tree = [
	[0,1,1,1,0,1,0,0,1,0,0,1,1,1],
	[0,0,0,1,1,2,2,2,2,1,1,0,0,0],
	[0,2,2,2,2,2,2,2,2,2,2,2,2,0],
	[0,0,3,3,2,2,2,2,2,2,2,3,3,0],
	[0,0,0,2,2,1,2,2,2,1,2,2,0,0],
	[0,0,0,2,2,2,2,2,2,2,2,0,0,0],
	[0,0,0,0,3,3,3,3,3,3,0,0,0,0],
	[0,0,0,0,0,3,4,4,3,0,0,0,0,0]]
	for i in tree:
		column = pos
		for b in i:
			if b == 1:
				pixels[map_matrix(row, column)] =(0, 0, 0) #black
			elif b ==2:
				pixels[map_matrix(row, column)] =(30, 80, 0) #dark brown
			elif b == 3:
				pixels[map_matrix(row, column)] =(85, 187, 0) #light brown
			elif b == 4:
				pixels[map_matrix(row, column)] =(0, 66, 0) #red
			else:
				pixels[map_matrix(row, column)] =(33, 0, 100)
			column +=1
		row +=1 
def show_rudolf(post=10):
	rud(post)
	pixels.show()
	
def test1(my_color):
	for i in range(256):
		pixels[i] = (my_color,0,i)
	pixels.show()

