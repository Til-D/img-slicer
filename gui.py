'''
	@descr: gui for image slicer
	@version: 1.0
'''

import crop
from tkinter import filedialog
from tkinter import *

root = Tk("Image Cropper")
root.minsize(600,200)
root.geometry("320x100")

def askForInputFile():
	root.filename =  filedialog.askopenfilename(initialdir = "./",title = "Select input image",filetypes = (("jpeg files","*.jpg"), ("png files","*.png"), ("all files","*.*")))

def askForTargetFolder():
	root.directory = filedialog.askdirectory()

def cropImage():
	crop.cropImage(root.filename, root.directory)

btn1 = Button(root, text="Select Image", command=askForInputFile)
btn2 = Button(root, text="Select Output Folder", command=askForTargetFolder)
btn3 = Button(root, text="Crop", command=cropImage)

btn1.place(x = 20, y = 20)
btn2.place(x = 20, y = 60)
btn3.place(x = 20, y = 100)

mainloop()