# Import all files from
# tkinter and overwrite
# all the tkinter files
# by tkinter.ttk
from tkinter import *

# creates tkinter window or root window
root = Tk()
root.geometry('200x200')

# function to be called when mouse enters in a frame
def enter(event):
	print('Entered at x = % d, y = % d'%(event.x, event.y))

# function to be called when when mouse exits the frame
def exit_(event):
	print('Left at x = % d, y = % d'%(event.x, event.y))

# frame with fixed geometry
frame1 = Frame(root, height = 100, width = 200, background= 'red')

# these lines are showing the
# working of bind function
# it is universal widget method
frame1.bind('<Enter>', enter)
frame1.bind('<Leave>', exit_)

but1 = Button(root, text= "Quit", command= root.destroy)
but1.pack(side= BOTTOM)

frame1.pack()

mainloop()
