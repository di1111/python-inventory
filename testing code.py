# Import things
from tkinter import *
import pickle

# Define some variables that I need
nameOfNewInventory = ""
nameOfInventory = ""
inventoryItems = {}
inventoryIsLoaded = False

def testing01():
    global inventoryIsLoaded
    inventoryIsLoaded = True

def testing02():
    global inventoryIsLoaded
    inventoryIsLoaded = False

def about():
    aboutWin = Toplevel(root)
    aboutLabel = Label(aboutWin, text='Inventory Manager Beta \n Created by: Dylan \n Copyright Dylan Hu 2017')
    aboutLabel.pack()
    aboutOkButton = Button(aboutWin, text="OK", command=aboutWin.destroy)
    aboutOkButton.pack()

def newInvFile():
    def doManyThings():
        makeNewInvFile()
        newInvWin.destroy()

    newInvWin = Toplevel(root)
    nameOfInvLabel = Label(newInvWin, text='Name of new inventory:')
    nameOfInvLabel.pack()
    nameOfInvEntry = Entry(newInvWin)
    nameOfInvEntry.pack()
    global nameOfNewInventory
    nameOfNewInventory = nameOfInvEntry.get()
    newInvSaveButton = Button(newInvWin, text='Save', command=doManyThings)
    newInvSaveButton.pack()

def makeNewInvFile(): # Really don't know why this is here, should be inside the newInvFile function
    global nameOfInventory
    global nameOfNewInventory
    global inventoryItems
    global inventoryIsLoaded
    nameOfInventory = nameOfNewInventory
    workingInventoryFile = open(nameOfInventory + '.dat', 'wb')
    inventoryItems["nameOfInventory"] = nameOfInventory
    inventoryIsLoaded = True

def openInvFile():
    global nameOfInventory
    global inventoryItems
    global nameOfInventory


def saveInvFile():
    pass

# =========================================================
# Above is the toplevel windows | Below is the main window
# =========================================================

root = Tk()

frame = Frame(root)
frame.pack()

# Create the dropdown menu for the main window
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=newInvFile)
filemenu.add_command(label="Open", command=openInvFile)
filemenu.add_command(label="Save", command=saveInvFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

testmenu = Menu(menubar, tearoff=0)
testmenu.add_command(label="change inventoryIsLoaded to True", command=testing01)
testmenu.add_command(label="change inventoryIsLoaded to False", command=testing02)
menubar.add_cascade(label="Test", menu=testmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

# Fix Below
if inventoryIsLoaded == False:
    plsLoadInv = Label(root, text="Please Load an Inventory File", fg="red")
    plsLoadInv.pack()

if inventoryIsLoaded == True:
    plsLoadInv.destroy()

# Fix above

root.config(menu=menubar)
root.mainloop()
workingInventoryFile.close()
root.destroy()
