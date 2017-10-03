from tkinter import *
import pickle

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        menubar = Menu(master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=newInvFile(master))
        filemenu.add_command(label="Open", command=openInvFile(master))
        filemenu.add_command(label="Save", command=saveInvFile)

    def about(self, master):
        aboutWin = Toplevel(master)
        aboutLabel = Label(master, text='Inventory Manager Beta \n Created by: Dylan \n Copyright Dylan Hu 2017')
        aboutLabel.pack()
        aboutOkButton = Button(master, text="OK", command=aboutWin.destroy)
        aboutOkButton.pack()

    def openInvFile(self, master):
        pass

    def newInvFile(self, master):
        pass

    def saveInvFile(self):
        pass

root = Tk()

app = App(root)

root.mainloop()

# Websites used:
# http://effbot.org/tkinterbook/tkinter-classes.htm has all the pages i used
#
