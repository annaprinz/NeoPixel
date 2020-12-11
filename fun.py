import board
import neopixel
import time
import random

pixel_pin = board.D18
# The number of NeoPixels
num_pixels = 256
# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB
 
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.1, auto_write=False, pixel_order=ORDER
)
def map_matrix(row, column):
	column = column % 32
	row = row % 8
	if row == 0:
		return column
	elif row == 1:
		return (63-column)
	elif row == 2:
		return ( column + 64)
	elif row == 3:
		return ( 127- column)
	elif row == 4:
		return (column + 128)
	elif row == 5:
		return (191 - column)
	elif row == 6:
		return (column + 192)
	elif row == 7:
		return (255 - column)

def christmas_tree(pos=10):
	row = 0
	column = pos
	tree = [
	[4,0,0,0,0,0,1,0,0,0,0,0,0],
	[0,0,0,0,0,1,1,1,0,0,0,0,0],
	[0,0,0,0,1,1,2,1,1,0,0,0,0],
	[0,0,0,1,1,3,1,1,1,1,0,0,0],
	[0,0,1,2,1,1,1,1,2,1,1,0,0],
	[0,1,1,3,1,2,1,1,1,3,1,1,0],
	[0,0,0,0,0,0,1,0,0,0,0,0,0],
	[0,0,0,0,0,0,1,0,0,0,0,0,0]]
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

def test1(my_color):
	for i in range(256):
		pixels[i] = (my_color,0,i)
	pixels.show()

