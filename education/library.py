def draw_horizontal_wall(length):
	print("|", end = "")
	for l in range(length):
        	print("-", end = "")
	print("|")

	
def draw_middle_section(width, length):
	for w in range(width):
		print("|", end = "")
		for l in range(length):
			print(" ", end = "")
		print("|")

def draw_library(name, length, width):
  
    """
    Draws a library of a given length and width

    args : 

    name is the name of the library
    length is the horizontal length of the library
    width is the vertical length of the library

    """
    
    # Sanitizing Parameters
    if(length <= 0 or width <= 0):
    	raise ValueError("Parameters should be greater than 0.")
    	return

    # Printing Library
    print(name)
    draw_horizontal_wall(length)
    draw_middle_section(width, length)
    draw_horizontal_wall(length)

    return
	   


