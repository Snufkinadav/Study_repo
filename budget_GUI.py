from tkinter import *
root = Tk()

e = Entry(root, width = 100)
e.insert(0,'Write your answer here and click Done!')
#functions
def my_click():
    myLabel= Label(root, text = f'Hi {e.get()}') 
    myLabel.pack()
#sandbox
myLabel1 = Label(root, text = 'AI rob')
myLabel2 = Label(root, text = "Hi!, How are you?\nTell me your name and we'll start the game")
my_button = Button(root, text ='Done!',
padx = 50,pady = 50, command = my_click, 
fg ='Green',bg = 'red')
#packing
myLabel1.pack()
myLabel2.pack()
my_button.pack()
e.pack()
#button
root.mainloop()


