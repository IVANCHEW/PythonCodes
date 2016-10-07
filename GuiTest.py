import Tkinter

#My understanding: The arguement here is the reference to a parent GUI. 
#Since it is possible for the current GUI to be housed in a bigger window or frame

class simpleapp_tk(Tkinter.Tk):
	
	
	#What does _init_ mean?
	#Is self and parent a keyword in python?
	
	#[Ans] The self variable represents the instance of the object itself
	
	def __init__(self,parent):
		Tkinter.Tk.__init__(self,parent)
		self.parent=parent
		self.initialize()
		
	def initialize(self):
		self.grid()
		
		#Note that the creation of an entry widget is different from that of the others
		self.entryVariable = Tkinter.StringVar()
		self.entry = Tkinter.Entry(self, textvariable=self.entryVariable)
		self.entry.grid(column=0,row=0,sticky="EW")
		
		#The first arguement of the bind method is the key we want to catch 
		#The second arguement is the event handler we want to fire
		self.entry.bind("<Return>", self.OnPressEnter)
		self.entryVariable.set("Enter Text Here")
		
		#The command="Arguement" refers to the handler fired when the button is pressed
		button = Tkinter.Button(self,text="Click Me", command=self.OnButtonClick)
		button.grid(column=1,row=0)
		
		self.labelVariable=Tkinter.StringVar()
		label=Tkinter.Label(self, textvariable=self.labelVariable, 
			anchor="w",fg="white",bg="blue")
		label.grid(column=0,row=1,columnspan=2,sticky="EW")
		self.labelVariable.set("Hello")
		
		self.grid_columnconfigure(0,weight=1)
		self.resizable(True,False)
		
		self.FocusOnEntry
		
		
	def OnButtonClick(self):
		self.labelVariable.set(self.entryVariable.get()+"You Clicked the button!")
		
	def OnPressEnter(self,event):
		self.labelVariable.set("You pressed enter!")
	
	#Defining a function to set the focus in the initialization code does not work. Why?	
	def FocusOnEntry(self):
		self.entry.focus_set()
		self.entry.selection_range(0,Tkinter.END)
		self.labelVariable.set("Function Works")

if __name__ == "__main__":
	app = simpleapp_tk(None)
	app.title("my application")
	app.mainloop()
	
	
