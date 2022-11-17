from tkinter import *
import time
import random
#init{
tk = Tk()
tk.title("stuff")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
#}




class ball:
	def __init__(self, canvas, color):
		 self.canvas = canvas
		 self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
		 self.canvas.move(self.id, 245, 100)
		 self.x = 0
		 self.y = -1
		 self.canvas_height = self.canvas.winfo_height()
	def draw(self):
		self.canvas.move(self.id, self.x, self.y)
		#pos = self.coords(self.id)
ball = ball(canvas, "cyan")




while True:
	ball.draw()
	tk.update_idletasks()
	tk.update()
	time.sleep(.01)
