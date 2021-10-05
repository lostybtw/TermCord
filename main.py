from tkinter import *

root = Tk()

root.title("TermCord")
root.geometry("1280x720")

# Logins 

Login_text= Text(root, height=300,width=int(720/2))
Login_text.insert(1.0,"Login")

# Placements
Login_text.grid(column=300,row=360)

root.mainloop()
