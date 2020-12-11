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

def rud(pos=10,c=2):
    #2=color
	row = 0
	column = pos
	my_array = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,4,4,4,0,0,0,0,0,0,0],
    [0,0,0,4,4,4,4,4,0,0,0,0,0,0],
	[0,0,4,0,0,4,0,0,4,0,0,0,0,0],
    [0,0,4,0,1,4,0,1,4,0,0,0,0,0],
	[0,0,4,4,4,4,4,4,4,0,0,0,0,0],
    [0,0,4,4,4,4,4,4,4,0,0,0,0,0],
	[0,0,4,0,4,0,4,0,4,0,0,0,0,0]]
	#my_array.where(my_array==2, 2, my_array) 
	for i in my_array:
		column = pos
		for b in i:
			if b == 1:
				pixels[map_matrix(row, column)] =(0, 0, 255) #blue
			elif b == 2:
				pixels[map_matrix(row, column)] =(166, 50, 255) #light blue
			elif b == 3:
				pixels[map_matrix(row, column)] =(167, 254, 100) #orange
			elif b == 4:
				pixels[map_matrix(row, column)] =(0, 66, 0) #red
			elif b == 5:
				pixels[map_matrix(row, column)] =(255, 255, 0) #yellow
			elif b == 6:
				pixels[map_matrix(row, column)] =(255, 0, 0) #green
			elif b == 7:
				pixels[map_matrix(row, column)] =(0, 130, 95) #purpel
			else:
				pixels[map_matrix(row, column)] =(0, 0, 0) #black
			column +=1
		row +=1 
def show_packmonster(post=10):
	rud(post)
	pixels.show()
	
def test1(my_color):
	for i in range(256):
		pixels[i] = (my_color,0,i)
	pixels.show()

