from tkinter import *
from tkinter import ttk  


root = Tk()
root.geometry("900x600")
root.title("Gui")


guiitems = ["Dropdown", "Button", "Label"]

dropdown = ttk.Combobox(root, values = guiitems, state = "readonly")
dropdown.pack()

class CreateElements:
    
    def _init_(self):
        print("This is CreateElements class")
        
        
    def createLabel(self):
        label = Label(root,text = "A new label is been created using class")
        label.pack()
        
        
    def createButton(self):    
        class_btn = Button(root, text = " A Button ", command = self.message)
        class_btn.pack(padx=20, pady = 10)
        
    def  createDropdown(self):
        value = [1,2,3,4,5,6,7,8,9,10]
        class_dropdown = ttk.Combobox(root, values = value)
        class_dropdown.pack()
        
    def choose(self):
        global dropdown
        element = dropdown.get()
        if element == "Dropdown":
            self.createDropdown()
            
        elif element == "Button":
            self.createButton()
            
        elif element == "Label":
            self.createLabel()
        
        
        
    def message(self):
        messagebox.showinfo("showinfo", "You clicked the button created using class")
        









obj_of_CreateElements = CreateElements()


btn = Button(root,text="Click to create label and button element", command = obj_of_CreateElements.choose)
btn.pack(padx=20, pady = 10)

root.mainloop()
    