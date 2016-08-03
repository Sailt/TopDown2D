import Tkinter as tk
#Soon working on collisions
class setupGame(tk.Frame):
	def __init__(self, parent = None):

		tk.Frame.__init__(self, parent)

		self.objCoords = []
		self.canvasWidth = 600
		self.canvasHeight = 400
		self.charWidth = 40
		self.scrollIncr = 10
		self.halfWidth = self.charWidth - 5
		
		self.char = []
		
		self.canvas = tk.Canvas(self, width = self.canvasWidth, height = self.canvasHeight, background = "Blue")
		
		self.bind("<Up>", self.moveNorth)
		self.bind("<Down>", self.moveSouth)
		self.bind("<Right>",self.moveEast)
		self.bind("<Left>",self.moveWest)
		self.canvas.bind("<Button-1>", self.callback)

		self.canvas.configure(yscrollincrement = str(self.scrollIncr), xscrollincrement = str(self.scrollIncr))
		self.canvas.pack(side = "top", fill = "both", expand = True)

		self.screenTest()

		for i in range (0,len(self.char)-1):
			self.objCoords.append(self.canvas.coords(self.char[i])) 

		self.numChars = len(self.char)

	#def new_window(self):
	#	self.count += 1
    #	id = self.count#"New window #%s" % self.count
    #	window = tk.Toplevel(self)
    #	label = tk.Label(window, text="New")
    #	label.pack(side="top", fill="both", padx=10, pady=10)		

	def addChar(self,name,row,column): #row = 4, column = 4)
		rectangle = self.canvas.create_rectangle(0,0,self.charWidth,self.charWidth,fill="Red")
		self.char.append(rectangle)
		self.canvas.move(self.char[-1],row,column)

	def moveNorth(self, event):
		charCoords = self.canvas.coords(self.char[-1])
		i = True
		for j in range (0,self.numChars-1):
			if charCoords[1] == self.objCoords[j][1] + self.charWidth and charCoords[3] == self.objCoords[j][3] + self.charWidth:
				if self.objCoords[j][0] - self.halfWidth < charCoords[0] < self.objCoords[j][0] + self.halfWidth:
					if self.objCoords[j][2] - self.halfWidth < charCoords[2] < self.objCoords[j][2] + self.halfWidth:
						i = False
						#if j == 0:
							#self.new_window()
		if i == True:
			self.canvas.yview_scroll(-1,"units")
			self.canvas.move(self.char[-1],0,-self.scrollIncr)
	
					
	def moveSouth(self, event):
		charCoords = self.canvas.coords(self.char[-1])
		i = True
		for j in range (0,self.numChars-1):
			if charCoords[1] == self.objCoords[j][1] - self.charWidth and charCoords[3] == self.objCoords[j][3] - self.charWidth:
				if self.objCoords[j][0] - self.halfWidth < charCoords[0] < self.objCoords[j][0] + self.halfWidth:
					if self.objCoords[j][2] - self.halfWidth < charCoords[2]< self.objCoords[j][2] + self.halfWidth:
						i = False

		if i == True:
			self.canvas.yview_scroll(1,"units")
			self.canvas.move(self.char[-1],0,self.scrollIncr)

	def moveEast(self, event):
		charCoords = self.canvas.coords(self.char[-1])
		i = True
		for j in range (0,self.numChars-1):
			if charCoords[0] == self.objCoords[j][0] - self.charWidth and charCoords[2] == self.objCoords[j][2] - self.charWidth:
				if self.objCoords[j][1] - self.halfWidth < charCoords[1] < self.objCoords[j][1] + self.halfWidth:
					if self.objCoords[j][3] - self.halfWidth < charCoords[3] < self.objCoords[j][3] + self.halfWidth:
						i = False

		if i == True:
			self.canvas.xview_scroll(1,"units")
			self.canvas.move(self.char[-1],self.scrollIncr,0)

	def moveWest(self, event):
		charCoords = self.canvas.coords(self.char[-1])
		i = True
		for j in range (0,self.numChars-1):
			if charCoords[0] == self.objCoords[j][0] + self.charWidth and charCoords[2] == self.objCoords[j][2] + self.charWidth:
				if self.objCoords[j][1] - self.halfWidth < charCoords[1] < self.objCoords[j][1] + self.halfWidth:
					if self.objCoords[j][3] - self.halfWidth < charCoords[3] < self.objCoords[j][3] + self.halfWidth:
						i = False
			
		if i == True:					
			self.canvas.xview_scroll(-1,"units")
			self.canvas.move(self.char[-1],-self.scrollIncr,0)

	def screenTest(self):
		self.addChar("rectangle",0, 0)
		self.addChar("rectangle",self.canvasWidth - self.charWidth, 0)
		self.addChar("rectangle",0, self.canvasHeight - self.charWidth)
		self.addChar("rectangle",self.canvasWidth - self.charWidth, self.canvasHeight - self.charWidth)
		self.addChar("rectangle",self.canvasWidth/2 - self.charWidth/2, self.canvasHeight/2 - self.charWidth/2)

	def callback(self,event):
		self.focus_set()
#		print "clicked at", event.x, event.y

root = tk.Tk()
game = setupGame(root)
game.pack()
game.mainloop()
