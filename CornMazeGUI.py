from tkinter import *
from PIL import ImageTk, Image
root = Tk()

# Adjust size 
root.geometry("800x500")

root.title("Corn Maze")
root.iconbitmap('Images/icongame.ico')

# Add image file
bg = PhotoImage(file = "Images/backgroundimg.png")


# Create Canvas for Background Image
canvas1 = Canvas( root, width = 800,height = 500)  
canvas1.pack(fill = "both", expand = True)
  
# Display image
canvas1.create_image( 0, 0, image = bg, anchor = "nw")

#Creating Welcome Label
canvas1.create_text(400,25,text="Welcome!",font=("Helvetica",35),fill="white")

#Add some buttons
button1 = Button(root,text="Start")
button2 = Button(root,text="Reset")
button3 = Button(root,text="Exit")

button1_window = canvas1.create_window(10,35,anchor="nw",window=button1)
button2_window = canvas1.create_window(50,35,anchor="nw",window=button2)
button3_window = canvas1.create_window(95,35,anchor="nw",window=button3)



root.mainloop()