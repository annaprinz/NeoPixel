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
