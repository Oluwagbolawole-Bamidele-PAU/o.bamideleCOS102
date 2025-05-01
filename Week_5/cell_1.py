import tkinter as tk
from tkinter import messagebox as msgbox

#Handling button click event
def button_click():
    #print("Button clicked!")

    # Show an information message box
    msgbox.showinfo("info", "Welcome to COS  102 GUI App!")

    #Ask for User confirmation
    result = msgbox.askyesno("confirmation", "Do you want to continue")

#Create the main window
root = tk.Tk()
root.title("Home Page")
root.geometry("300x100")

#Add a label widget
label = tk.Label(root, text = "Hello Friend \n")
label.pack()

#Styling the button widget
button = tk.Button(root, text="Click Me!", command = button_click)
button.pack()

#Styling the button widget
button.config(fg="white", bg="darkblue", )

#start the event loop
root.mainloop()



