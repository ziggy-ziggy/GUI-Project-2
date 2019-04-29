#**********************************************
#Students   : Jacob, Mark, Viraj, Cole
#Class      : Human Factors and User Interface
#Instructor : Gamradt
#Assignment : 4
#Due Date   : 5/3/2019
#**********************************************
#Description: This is an implementaiton for Ken's
#Coffee and Bagels
#**********************************************


import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox, StringVar, OptionMenu
from PIL import Image, ImageTk

#functions for menu
def helpBox():
    messagebox.showinfo('Help', "Welcome to Ken's Coffee and Bagels !\n 1. Select a bagel\n 2. Add shmears\n 3. Add to cart")
def studentBox():
    messagebox.showinfo('Students', 'Jacob\nMark\nViraj\nCole')
def courseBox():
    messagebox.showinfo('Course', 'SE330: Human Factors & User Interface')
def AssignmentBox():
    messagebox.showinfo('Assignment', 'Assignment 4 and 5 - Project 2')

#menu function
def makeMenu(root):
    top = tk.Menu(root)
    root.config(menu = top)
    file = tk.Menu(top, tearoff = False)
    file.config(bg = '#E5E5E5')
    file.add_command(label = 'Help', command = helpBox, underline = 0)
    file.add_command(label = 'Quit', command = root.destroy, underline = 0)
    top.add_cascade(label = 'File', menu = file, underline = 0)
    edit = tk.Menu(top, tearoff = False)
    edit.add_command(label = 'Student', command = studentBox, underline = 0)
    edit.add_command(label = 'Course', command = courseBox, underline = 0)
    edit.add_command(label = 'Assignment', command = AssignmentBox, underline = 0)
    top.add_cascade(label = 'Edit', menu = edit, underline = 0)

##### Functions that check states #####
#######################################
def checkButtons(root):
    buttons = 'Strawbery Shmear -- $1.00', 'Blueberry Shmear -- $1.00', 'Cream Cheese -- $1.00', 'Butter -- $50.00'
    for button in buttons:
        row = ttk.Frame(root)
        row.grid()
        vars = tk.IntVar()
        ttk.Checkbutton(row, text = button, variable = vars).grid()
        states.append(vars)
        num = tk.Spinbox(row, from_ = 1, to = 10, command = checkAmount).grid()
        amounts.append(num)

def onPress():
        updateCosts(var.get(), list(map((lambda vars: vars.get()), states)))
        pick = var.get()
        print('You pressed', pick)
        print('Result:', pick)

def report():
        updateCosts(var.get(), list(map((lambda vars: vars.get()), states)))
        print (var.get())

def checkReport():
        print (list(map((lambda vars: vars.get()), states)))

def onMove(scalVar):
    updateCosts(var.get(), list(map((lambda vars: vars.get()), states)))
    print ('Moved to', scaleVar.get())

def checkAmount():
        #value = num.get()
        print (list(map((lambda num: num.get()), amounts)))
#######################################

##### Fills entries located in Information section #####
def makeform(root, fields):
    entries = []
    i = 2
    for field in fields:
        i = i + 1
        lab = ttk.Label(root, width = 20, text = field, style="My.TLabel")
        lab.grid(row=i, column=0, pady=(3,0), padx=15, sticky="nw")
        ent = ttk.Entry(root, width = 30)
        ent.grid(row=i, column=0, columnspan=2, pady=(3,0), padx=(0,20), sticky="we")
        entries.append(ent)
    return entries

##### Updates the cost of selections #####
def updateCosts(primary, accessories = None):
    quantity = scaleVar.get()
    print(primary)
    if(primary is not 0):
        if(primary is 1):
            primaryCost = 1
        else:
            primaryCost = 1
        accessoryCost = 0

        if(accessories is not None):
            accessoryCost = accessories[0]*15 + accessories[1]*50 + accessories[2]*20 + accessories[3]*50
        costs = []
        costs.append(primaryCost * quantity + accessoryCost)
        if(primaryCost * quantity + accessoryCost >= 1200):
            costs.append(costs[0]*0.1)
        else:
            costs.append(costs[0] - costs[0])
        costs.append(costs[0]*.04)
        costs.append(costs[0] + costs[2] - costs[1])
        for i, costEnt in enumerate(costEntries):
            dollars = '${:,.2f}'.format(costs[i])
            costEnt.config(state=tk.NORMAL)
            costEnt.delete(0, tk.END)
            costEnt.insert(0, dollars)
            costEnt.config(state=tk.DISABLED)
    else:
        costEntries[0].config(state=tk.NORMAL)
        costEntries[0].delete(0, tk.END)
        costEntries[0].insert(0, "Must have a bagel selected")
        costEntries[0].config(state=tk.DISABLED)

##### Main #####
if __name__ == '__main__':
    root = tk.Tk()
    root.title("Ken's Coffee And Bagels")
    makeMenu(root)

    ##### Styles #####
    frame_style = ttk.Style()
    frame_style.configure("My.TFrame", background="#ffffff", borderwidth=1, relief="raised")
    borderlessFrame_style = ttk.Style()
    borderlessFrame_style.configure("borderless.TFrame", background="#ffffff")
    radioButton_style = ttk.Style()
    radioButton_style.configure("My.TRadiobutton", background="#ffffff")
    label_style = ttk.Style()
    label_style.configure("My.TLabel", background="#ffffff")
    line_style = ttk.Style()
    line_style.configure("line.TFrame", background="#626567")
    checkButton_style = ttk.Style()
    checkButton_style.configure("My.TCheckbutton", background="#ffffff")
    scale_style = ttk.Style()
    scale_style.configure("My.Horizontal.TScale", background="#ffffff")

    ##### Frames #####
    product_frame = ttk.Frame(root, style="My.TFrame", width=1400, height=675)
    cartInfo_frame = ttk.Frame(root, style = "My.TFrame", width=400, height=675)
    addOn_frame = ttk.Frame(product_frame, style="borderless.TFrame", width=300, height=200)
    addOnUnderline_line = ttk.Frame(addOn_frame, style="line.TFrame", width=250, height=1)
    checkButtons_frame = ttk.Frame(product_frame, style="borderless.TFrame", width=300, height=200)
    costInfo_frame = ttk.Frame(cartInfo_frame, style="borderless.TFrame", width=400, height=400)
    list_frame = ttk.Frame(cartInfo_frame, style="borderless.TFrame", width=400, height=400)
    costInfoUnderline_line = ttk.Frame(costInfo_frame, style="line.TFrame", width=250, height=1)

	##### Header Button #####
    gifdir = "images/"
    headerImg = tk.PhotoImage(file = gifdir + "KENSBAGELS.png")
    headerImg = headerImg.subsample(5)
    tk.Label(root, image = headerImg, bg = 'green', height = 90).grid(sticky="nsew", columnspan=5)
    root.grid_columnconfigure(0, weight = 1)

    ##### Product Frame #####
    product_frame.grid_configure(column=2, columnspan=3, pady=30, padx=(30,30), sticky="e")
    var = tk.IntVar()
    versions = 'Bagel 1 -- $2.00', 'Bagel 2 -- $2.00', 'Bagel 3 -- $2.00', 'Bagel 4 -- $2.00', 'Bagel 5 -- $2.00', 'Bagel 6 -- $2.00' 
    imageName = "bagel1.png", "bagel2.png", "bagel3.png", "bagel4.png", "bagel5.png", "bagel6.png"
    gifdir = "images/"
    imag = []
    i = 1
    rowNo = 0
    colNo = 0

    #loop to display the product radio buttons and picture
    for version in versions:
        if i % 4 == 0:
            rowNo = 2
            colNo = 0
        ttk.Radiobutton(product_frame, text = version, command = onPress, value = i, variable = var, style="My.TRadiobutton", cursor="hand2").grid(row=rowNo, column=colNo, pady=(10,0), padx=60, sticky="NW")
        photo = gifdir + imageName[i - 1]
        img = Image.open(photo)
        img = img.resize((80, 80), Image.ANTIALIAS)
        photoImage = ImageTk.PhotoImage(img)
        imag.append(photoImage)
        ttk.Label(product_frame, image = imag[i - 1]).grid(row=rowNo + 1, column = colNo, pady=(10,20), padx=60, sticky="nw")
        colNo = colNo + 1
        i = i + 1

    #cart vertical frame - contains addOn_frame and personalInfo_frame
    cartInfo_frame.grid_configure(row=1, column=0, columnspan=2, pady=30, padx=(30, 110), sticky="nw")

    ##### GPU Additional Accessories Frame #####
    #accessories label and underline
    addOn_frame.grid_configure(row=5, column=0, columnspan=4, pady=(30,30), padx=10, sticky="sw")
    addOnLabel = ttk.Label(addOn_frame, style="My.TLabel", text="Shmears")
    addOnLabel.config(font = ('rockwell', 12))
    addOnLabel.grid(sticky="ns", column=0, columnspan=3)
    addOnUnderline_line.grid(sticky="ns", column=0, columnspan=2, pady=(0,5))

    checkButtons_frame.grid_configure(row=5, column=0, columnspan=4, pady=(30,30), padx=10, sticky="se")
    ttk.Button(checkButtons_frame, width=10, text = 'Add to Cart', cursor="hand2", command = (lambda: confirmation(completeForm))).grid(column=0, row=1, columnspan=1, pady=(5, 15), sticky="sw")
    #checkButtonsLabel.config(font = ('rockwell', 12))
    #checkButtonsLabel.grid(sticky="se", column=0, columnspan=3)
    #checkButtonsUnderline_line.grid(sticky="se", column=0, columnspan=2, pady=(0,5))



    states = []
    amounts = []
    num = tk.IntVar()
    buttons = 'Strawbery Shmear -- $1.00', 'Blueberry Shmear -- $1.00', 'Cream Cheese -- $1.00', 'Butter -- $50.00'
    rowNo = 2
    colNo = 0

    #loop to display accessory checkbuttons
    for button in buttons:
        if colNo == 2:
            rowNo = rowNo + 2
            colNo = 0
        vars = tk.IntVar()
        ttk.Checkbutton(addOn_frame, text = button, variable = vars, command = report, style="My.TCheckbutton", cursor="hand2").grid(row=rowNo, column=colNo, columnspan=1, pady=2, padx=20, sticky="NW")
        states.append(vars)
        colNo = colNo + 1

    ##### Cost Information Frame #####
    #cost info label and underline
    costInfo_frame.grid_configure(row=1, columnspan=5, pady=10, padx=(50,0), sticky="nw")
    costInfoLabel = ttk.Label(costInfo_frame, style="My.TLabel", text="Cost Info")
    costInfoLabel.config(font = ('rockwell', 12))
    costInfoLabel.grid(sticky="ns", column=0, columnspan=5)
    costInfoUnderline_line.grid(sticky="ns", column=0, columnspan=5)

    completeForm = []

    #create cost info data
    costFields = 'Subtotal','Discount', 'Tax', 'Total'
    costEntries = makeform(costInfo_frame, costFields)
    i = 0
    for costEnt in costEntries:
        completeForm.append(costEntries[i])
        costEntries[i].insert(0, "$0.00")
        costEntries[i].config(state=tk.DISABLED)
        i = i + 1

    root.bind('<Return>', (lambda event: fetch(ents)))
    ttk.Button(cartInfo_frame, width=10, text = 'Checkout', cursor="hand2", command = (lambda: confirmation(completeForm))).grid(column=0, columnspan=4, pady=(5, 15), sticky="ns")
    ttk.Button(list_frame, width=10, text = 'testing', cursor="hand2", command = (lambda: confirmation(completeForm))).grid(column=0, columnspan=4, pady=(5, 15), sticky="ns")
    shoppingList = tk.Listbox(cartInfo_frame)
    #shoppingList = tk.Listbox(cartInfo_frame, width = 500, height = 500)
    shoppingList.insert(END, 'Bagel1')
    shoppingList.insert(END, 'Bagel2')

    root.grid_columnconfigure(0, weight = 1)

root.mainloop()
