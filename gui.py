'''
	@descr: gui for image slicer
	@version: 1.0
'''
import crop
from tkinter import filedialog
from tkinter import *

root = Tk()
root.minsize(300,150)
root.title("Image Slicer")
root.configure(bg='#6b788c')

def askForInputFile():
	root.filename =  filedialog.askopenfilename(initialdir = "./",title = "Select input image",filetypes = (("jpeg files","*.jpg"), ("png files","*.png"), ("all files","*.*")))
	btn2.configure(state=NORMAL)
	status.configure(text="")

def askForTargetFolder():
	root.directory = filedialog.askdirectory()
	btn3.configure(state=NORMAL)

def cropImage():
	crop.cropImage(root.filename, root.directory)
	status.configure(text="Done.")
	status.grid(row=4, column=0)
	btn2.configure(state=DISABLED)
	btn3.configure(state=DISABLED)

heading = Label(root, text='Slice an image in 3 steps:', bg='#9ea9ba')
status = Label(root, text='', bg='#9ea9ba')

btn1 = Button(root, text="1. Select Image ", command=askForInputFile, height=2, width=50, padx=2)
btn2 = Button(root, text="2. Select Output Folder ", command=askForTargetFolder, state=DISABLED, height=2, width=50)
btn3 = Button(root, text="3. Slice it! ", command=cropImage, state=DISABLED, height=2, width=50)

heading.grid(row=0, column=0)
btn1.grid(row=1, column=0)
btn2.grid(row=2, column=0)
btn3.grid(row=3, column=0)

mainloop()