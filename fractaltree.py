from turtle import *
import time

speed('fastest') 
rt(-90) 
angle = 30
#def wait():
#    input("press key")
#wait()
def draw(size, level): 

	if level > 0: 
		colormode(255) 
		pencolor(0, 255//level, 0) 
		fd(size) 
		rt(angle) 
		draw(0.8 * size, level-1) 
		pencolor(0, 255//level, 0) 		
		lt( 2 * angle ) 
		draw(0.8 * size, level-1) 
		pencolor(0, 255//level, 0) 
		rt(angle) 
		fd(-size) 
draw(100, 7) 

