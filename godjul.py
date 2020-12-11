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
ORDER = neopixel.GRB
 
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.1, auto_write=False, pixel_order=ORDER
)

def godjul_message(pos=0):
	row = 0
	column = pos
	tree = [
	[0,0,0,1,1,1,1,1,0,0,0,0,0],
	[0,0,1,1,1,1,1,1,1,0,0,0,0],
	[0,1,1,1,0,0,0,0,0,0,0,0,0],
	[0,1,1,0,0,0,1,1,1,1,0,0,0],
	[0,1,1,0,0,0,1,1,1,1,0,0,0],
	[0,1,1,1,0,0,0,1,1,0,0,0,0],
	[0,0,1,1,1,1,1,1,1,0,0,0,0],
	[0,0,0,1,1,1,1,1,0,0,0,0,0]]
	for i in tree:
		column = pos
		for b in i:
			if b == 1:
				pixels[map_matrix(row, column)] =(0, 66, 0)
			elif b ==2:
				pixels[map_matrix(row, column)] =(66, 0, 0)
			elif b == 3:
				pixels[map_matrix(row, column)] =(random.randint(8,255), random.randint(30,255), random.randint(10,255))
			elif b == 4:
				pixels[map_matrix(row, column)] =(random.randint(8,255), random.randint(30,255), random.randint(10,255))
			else:
				pixels[map_matrix(row, column)] =(33, 0, 100)
			column +=1
		row +=1 
def show_godjul(post=1):
	godjul_message(post)
	#pixels.show()

