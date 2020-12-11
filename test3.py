import board
import neopixel
import time
import random
pixel_pin = board.D18
# The number of NeoPixels
num_pixels = 256
# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRBppo
 
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.10, auto_write=False, pixel_order=ORDER
)
#pixels[0] = (255, 0, 0)

#def led_map():
	

#for loop1 in range (255):
#	for i in range(255):
#		pixels[loop1] = (255, 255, 0)
#	pixels.show()
for zero in range(31):
	pixels[zero] = (  0, 0, 0)
pixels.show()

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

def left_to_right (r, g, b):
	for rr in range(32):
		pixels[rr] = (r, g, b) # 0
		pixels[63-rr] = (r, g, b) # 1
		pixels[rr + 64] = (r, g, b) # 2
		pixels[127-rr] = (r, g, b) # 3
		pixels[rr + 128] = (r, g, b) # 4
		pixels[191-rr] = (r, g, b) #5
		pixels[rr + 192] = (r, g, b) #6
		pixels[255-rr] = (r, g, b) #7 
		pixels.show()
		time.sleep(0.2)
	#time.sleep(0.4)
def clear_matrix():		
	for lala in range(255):
		pixels[lala] = (0,0,0)
	pixels.show()
clear_matrix()
time.sleep(0.9)	
pozx = 0
pozy = 12
#for i in range(8):
#	pozy +=1
#	pozx = i
#	pixels[map_matrix(i, pozy)] =(255, 0, 0)
#pozx = 0
#for i in range(8):	
#	pozx = i
#	pixels[map_matrix(i, pozy)] =(255, 0, 255)	
#	pozy -=1
pixels.show()
time.sleep(1)
#print(map_matrix(pozx, pozy))

def christams_tree(pos):
	row = 0
	column = pos
	tree = [
	[0,0,0,0,0,0,1,0,0,0,0,0,0],
	[0,0,0,0,0,1,1,1,0,0,0,0,0],
	[0,0,0,0,1,1,2,1,1,0,0,0,0],
	[0,0,0,1,1,3,1,1,1,1,0,0,0],
	[0,0,1,2,1,1,1,3,2,1,1,0,0],
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
			else:
				pixels[map_matrix(row, column)] =(33, 0, 100)
				#pixels[map_matrix(row, column)] =(255, 255, 255)
			column +=1
		row +=1 
	#pixels.show()
	
#christams_tree(0)
#christams_tree(21)
def jul():
	roll = 3 
	roll_actual = int(roll * 128)
	for i in range (0, roll_actual, 1):
		christams_tree(i)
		christams_tree(i+16)
		pixels.show()
		#time.sleep(0.09)
	for i in range (roll_actual, 0, -1):
		christams_tree(i)
		christams_tree(i+16)
		pixels.show()
		time.sleep(0.1)		
		
if __name__ == '__main__':
	try:
		while True:
			jul()
	except KeyboardInterrupt:
		for i in range(0,256):
			pixels[i] =(0, 0, 0)
		pixels.show()	
