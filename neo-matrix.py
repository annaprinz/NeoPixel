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
    pixel_pin, num_pixels, brightness=0.15, auto_write=False, pixel_order=ORDER
)

########################################
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.OUT)

Anna = True

########################################

def map_matrix(row, column):
	Anna = False
	if Anna:
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
	else:
		row = row % 8
		column = column % 32
		add_from_column = (31 - column)*8
		if column % 2 == 1:
			add_from_row = 7- (row % 8)
		else:
			add_from_row = row % 8
		return (add_from_column + add_from_row)
	
def power_supply(stand):
	if stand or stand == 'ON' or stand == 1:
		GPIO.output(21, 1)
		time.sleep(0.025)
	else:
		GPIO.output(21, 0)
		
def clear_matrix():		
	for lala in range(256):
		pixels[lala] = (0,0,0)
	pixels.show()


#####################################################################

def matrix(columns, lengt=35):
	pss = ['a']*15 + [0]
	for i in range(len(columns)):
		if columns[i] == 'a':
			columns[i] = random.choice(pss)
		elif columns[i] < lengt:
			columns[i] = columns[i] + 1
		elif columns[i] == lengt:
			columns[i] ='a'
	#print(columns)
	return columns


def pix_show(matrix_map, speed = 0.05, step = 4):
	shutdown = lambda val: 0 if (val-step < 1) else val-step
	#colors = [(255,0,0),(255,255,0), (0,0,255)]
	#abc = random.choice(colors)
	for column in range(32):
		for row in range(8):
			if matrix_map[column] == row:
				pixels[map_matrix(row, column)] = (0,120,0)
			else:
				pix_lvl = pixels[map_matrix(row, column)]
				r = shutdown(pix_lvl[0])
				g = shutdown(pix_lvl[1])
				b = shutdown(pix_lvl[2])
				pixels[map_matrix(row, column)] = (r, g, b)
	pixels.show()
	time.sleep(0.003)
			
	
########################################################				
		
if __name__ == '__main__':
	try:
		GPIO.output(21, 1)
		columns = ['a']*32
		#matrix(columns)
		while True:
			a = matrix(columns)
			for i in range(8):
				pix_show(a)
			#pix_show(a)
			#matrix(a)
		GPIO.output(21, 0)
			
		
	except KeyboardInterrupt:
		for i in range(256):
			pixels[i] =(0, 0, 0)
		pixels.show()
		time.sleep(0.025)
		GPIO.output(21, 0)	
