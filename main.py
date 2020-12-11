import board
import neopixel
import time
import random
from christmas_tree import *
from  packman_monster import *
#from godjul import *
from G import *
from O import *
from D import *
from J import *

pixel_pin = board.D18
# The number of NeoPixels
num_pixels = 256
# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB
 
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.09, auto_write=False, pixel_order=ORDER
)

for zero in range(31):
	pixels[zero] = (  0, 0, 0)
pixels.show()

#for i in range(256):
#	pixels[i] = (int(i/2),0,i)
#pixels.show()	

def show_letter(pos,let):
	row = 0
	column = pos
	letter = []
	if let == 'G':
		letter = g_letter()
	if let == 'O':
		letter = o_letter()
	if let == 'D':
		letter = D_letter()
	if let == 'J':
		letter = J_letter()
	for i in letter:
		column = pos
		for b in i:
			if b == 1:
				pixels[map_matrix(row, column)] =(66, 0, 0)
			elif b ==2:
				pixels[map_matrix(row, column)] =(0, 66, 0)
			elif b == 3:
				pixels[map_matrix(row, column)] =(random.randint(8,255), random.randint(30,255), random.randint(10,255))
			else:
				pixels[map_matrix(row, column)] =(0, 66, 0)
			column +=1
		row +=1 
		
def show_roll():
		roll = 3
		roll_actual = int(roll * 128)
		roll_god = int( 128)
		iv = 0
	for i in range (roll_actual, 0, -1):
		#show_letter(i,'G')
		#show_letter(i+11,'O')
		#show_letter(i+22,'D')
		#show_letter(i+128 ,'J')
		#show_letter(i+128 ,'J')
		#show_letter(i+128 ,'J')
		show_packmonster(i)
		show_packmonster(i+16)
		pixels.show()
		time.sleep(0.09)
		index += 1
	for i in range (0, roll_actual, 1):
		show_chris_tree(i)
		show_chris_tree(i+16)
		time.sleep(0.1)		

if __name__ == '__main__':
	try:
		#pass
		my_color=1
		while True:
			#my_color +=1
			#if(my_color ==256):
			#	my_color=0
			#test1(my_color)
			#time.sleep(0.1)
			#show_chris_tree()
			pixels.show()
			show_roll()
			time.sleep(0.5)
	except KeyboardInterrupt:
		for i in range(0,256):
			pixels[i] =(0, 0, 0)
		pixels.show()	
