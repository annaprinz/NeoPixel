import board
import neopixel
import time
from  alphabet import *
pixel_pin = board.D18
# The number of NeoPixels
num_pixels = 256
# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB
 
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.1, auto_write=False, pixel_order=ORDER
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
	Anna = True
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

def colors(color_def):
	if color_def == 1:
		return (0, 66, 0)
	elif color_def == 2:
		return (140, 140, 0)		
	elif color_def == 3:		
		return (66, 0, 0)
	else:
		return (0,0,0)
###################################################################
	
def disp_lay(led_table, pos_x=0, pos_z =0):
	row = 0
	column = 0
	asp = 10
	for row in range(8):
		for column in range(32):
			pick_up_x = (column + pos_x) % (len(led_table[0]))
			pick_up_z = (row + pos_z) % (len(led_table))
			b = led_table[pick_up_z][pick_up_x]
			pixels[map_matrix(row, column)] =colors(b)
			column +=1
		row +=1 

########################################################

def create_display_map(*elements):
	# creating one large table from many small 
	elements_sum = (8*[[]])
	for element in elements:
		for i in range(8):
			elements_sum[i] = elements_sum[i] + element[i]
	return(elements_sum)
	
def turn_off_slowly(speed = 0.05, step = 1):
	shutdown = lambda val: 0 if (val-step < 5) else val-step
	leds_on = True
	while leds_on:
		temp = 0
		for led in range (num_pixels):
			r = shutdown(pixels[led][0])
			g = shutdown(pixels[led][1])
			b = shutdown(pixels[led][2])
			pixels[led] = (r, g, b)
			temp = temp + r+g+b
		pixels.show()
		if temp == 0:
			leds_on = False
		else:
			time.sleep(speed)
########################################################				
		
if __name__ == '__main__':
	try:
		power_supply(True)
		
		O = letter('O')
		G = letter('G')
		D = letter('D')
		J = letter('J')
		U = letter('U')
		L = letter('L')
		tree = letter('tree')
		
		led_table = create_display_map(G,O,D,tree,J,U,L,letter('tree'),)
		# add as much as yoy like to 'led_table'
		
		roll = 3
		# the number of repetitions 
		
		roll_actual = len(led_table[0])*roll
		
		# from right to left
		for i in range(roll_actual):
			disp_lay(led_table,i,)
			pixels.show()
			time.sleep(0.01)
			
		# from left to right
		for i in range (roll_actual, 0, -1):
			disp_lay(led_table,i,)
			pixels.show()
			time.sleep(0.01)
			
		# for fun ;)
		for i in range(roll_actual):
				disp_lay(led_table,i,i)
				pixels.show()
				time.sleep(0.1)
		turn_off_slowly()
		time.sleep(3)
		power_supply(0)
		
	except KeyboardInterrupt:
		for i in range(256):
			pixels[i] =(0, 0, 0)
		pixels.show()
		time.sleep(0.025)
		GPIO.output(21, 0)	
