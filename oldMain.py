#**********************************************
#Students   : Austin, Jamison, Jacob, Justin
#Class      : Human Factors and User Interface
#Instructor : Gamradt
#Assignment : 2
#Due Date   : 3/13/2019
#**********************************************
#Description: This program implements a store front
#for a company that sells graphics cards along with 
#accessories for graphics cards.
#**********************************************


import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox, StringVar, OptionMenu
from PIL import Image, ImageTk

#functions for menu
def helpBox():
    messagebox.showinfo('Help', 'Welcome to our store!\n 1. Select a product\n 2. Add accessories\n 3. Enter information')
def studentBox():
    messagebox.showinfo('Students', 'Austin Hochhalter\n Justin Glenn\n Jamison French\n Jacob Simondet\n')
def courseBox():
    messagebox.showinfo('Course', 'SE330: Human Factors & User Interface')
def AssignmentBox():
    messagebox.showinfo('Assignment', 'Assignment 1 and 2 - Project 1')

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
    buttons = 'GPU Support Bracket -- $15.00', 'SLI Bridge -- $50.00', 'Thermal Paste -- $20.00', 'GPU Backplate (Nickel) -- $50.00'
    for button in buttons:
        row = ttk.Frame(root)
        row.grid()
        vars = tk.IntVar()
        ttk.Checkbutton(row, text = button, variable = vars).grid()
        states.append(vars)
        num = tk.Spinbox(row, from_ = 1, to = 10, command = checkAmount).grid()
        amounts.append(num)
    #ttk.Button(root, text = 'checkState', command = checkReport).grid()

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

##### Confirmation Window #####
def confirmation(entries):
    confirm = tk.Toplevel(root)
    confirm.geometry("420x480")
    confirm.title("Confirm Order")
    confirm_frame = ttk.Frame(confirm, style="My.TFrame", width=400, height=675)
    confirm_frame.grid_configure(columnspan=2, pady=30, padx=30, sticky="ns")
    confirm_frame.grid_columnconfigure(0, weight = 1)
    entryTitles = 'Subtotal Price','Discount', 'Tax', 'Total Price', 'Full name', 'Street address', 'City', 'State', 'Zip Code', 'Credit Card Number', 'CVC', 'Email'
    i = 0
    eRow = 0
    for entry in entries:
        if i == 4 or i == 0:
            ttk.Label(confirm_frame, text=entryTitles[i], style="My.TLabel").grid(row=eRow, column = 0, pady=(20,0), padx=20, sticky="nsw")
            ttk.Label(confirm_frame, text=entries[i].get(), style="My.TLabel").grid(row=eRow, column = 1, pady=(20,0), padx=20, sticky="nsew")
        else:
            ttk.Label(confirm_frame, text=entryTitles[i], style="My.TLabel").grid(row=eRow, column = 0, pady=2, padx=20, sticky="nsw")
            ttk.Label(confirm_frame, text=entries[i].get(), style="My.TLabel").grid(row=eRow, column = 1, pady=2, padx=20, sticky="nsew")
        eRow = eRow + 1
        print('Input => "%s"' % entry.get())
        i = i + 1
        eRow = eRow + 1
    ttk.Button(confirm_frame, text = 'Confirm Order', cursor="hand2", command=confirm.destroy).grid(column=0, pady=(5, 20), columnspan=2, sticky="ns")

##### Fills entries located in Information section #####
def makeform(root, fields):
    entries = []
    i = 2
    for field in fields:
        i = i + 1
        lab = ttk.Label(root, width = 20, text = field, style="My.TLabel")
        lab.grid(row=i, column=0, pady=(3,0), padx=15, sticky="nw")
        ent = ttk.Entry(root, width = 30)
        ent.grid(row=i, column=1, columnspan=2, pady=(3,0), padx=(0,20), sticky="we")
        entries.append(ent)
    return entries

##### Updates the cost of selections #####
def updateCosts(primary, accessories = None):
    quantity = scaleVar.get()
    print(primary)
    if(primary is not 0):
        if(primary is 1):
            primaryCost = 400
        elif(primary is 2):
            primaryCost = 800
        elif(primary is 3):
            primaryCost = 600
        elif(primary is 4):
            primaryCost = 1200
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
        costEntries[0].insert(0, "Must have a graphics card selected")
        costEntries[0].config(state=tk.DISABLED)

##### Main #####
if __name__ == '__main__':
    root = tk.Tk()
    root.title('Metafix Picker')
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
    rightInfo_frame = ttk.Frame(root, style = "My.TFrame", width=400, height=675)
    product_frame = ttk.Frame(root, style="My.TFrame", width=1200, height=675)
    addOn_frame = ttk.Frame(rightInfo_frame, style="borderless.TFrame", width=300, height=200)
    addOnUnderline_line = ttk.Frame(addOn_frame, style="line.TFrame", width=250, height=1)
    costInfo_frame = ttk.Frame(rightInfo_frame, style="borderless.TFrame", width=400, height=400)
    costInfoUnderline_line = ttk.Frame(costInfo_frame, style="line.TFrame", width=250, height=1)
    shippingInfo_frame = ttk.Frame(rightInfo_frame, style="borderless.TFrame", width=400, height=400)
    shippingInfoUnderline_line = ttk.Frame(shippingInfo_frame, style="line.TFrame", width=250, height=1)
    paymentInfo_frame = ttk.Frame(rightInfo_frame, style="borderless.TFrame", width=400, height=400)
    paymentInfoUnderline_line = ttk.Frame(paymentInfo_frame, style="line.TFrame", width=250, height=1)

    ##### Header Button #####
    gifdir = "images/"
    headerImg = tk.PhotoImage(file = gifdir + "metafix.png")
    headerImg = headerImg.subsample(5)
    tk.Label(root, image = headerImg, bg = 'black', height = 60).grid(sticky="nsew", columnspan=5)
    root.grid_columnconfigure(0, weight = 1)

    ##### Product Frame #####
    product_frame.grid_configure(columnspan=3, pady=30, padx=(110,30), sticky="w")
    var = tk.IntVar()
    versions = 'RTX 2060 -- $400.00', 'RTX 2080 -- $800.00', 'RTX 2070 -- $600.00', 'RTX 2080 Ti -- $1200.00'
    imageName = "2060.png", "2080.png", "2070.png", "2080 ti.png"
    gifdir = "images/"
    imag = []
    i = 1
    rowNo = 0
    colNo = 0

    #loop to display the product radio buttons and picture
    for version in versions:
        if i == 3:
            rowNo = 2
            colNo = 0
        ttk.Radiobutton(product_frame, text = version, command = onPress, value = i, variable = var, style="My.TRadiobutton", cursor="hand2").grid(row=rowNo, column=colNo, pady=(10,0), padx=60, sticky="NW")
        photo = gifdir + imageName[i - 1]
        img = Image.open(photo)
        img = img.resize((200, 230), Image.ANTIALIAS)
        photoImage = ImageTk.PhotoImage(img)
        imag.append(photoImage)
        ttk.Label(product_frame, image = imag[i - 1]).grid(row=rowNo + 1, column = colNo, pady=(10,20), padx=60, sticky="nw")
        colNo = colNo + 1
        i = i + 1

    #right vertical frame - contains addOn_frame and personalInfo_frame
    rightInfo_frame.grid_configure(row=1, column=3, columnspan=2, pady=30, padx=(0, 110), sticky="nw")

    ##### GPU Additional Accessories Frame #####
    #accessories label and underline
    addOn_frame.grid_configure(row=0, columnspan=4, pady=(10,0), padx=10, sticky="nw")
    addOnLabel = ttk.Label(addOn_frame, style="My.TLabel", text="GPU Accessories")
    addOnLabel.config(font = ('rockwell', 12))
    addOnLabel.grid(sticky="ns", column=0, columnspan=3)
    addOnUnderline_line.grid(sticky="ns", column=0, columnspan=2, pady=(0,5))

    states = []
    amounts = []
    num = tk.IntVar()
    buttons = 'GPU Support Bracket -- $15.00', 'SLI Bridge -- $50.00', 'Thermal Paste -- $20.00', 'GPU Backplate (Nickel) -- $50.00'
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

    #creates quantity scale
    scaleVar = tk.IntVar()
    ttk.Label(costInfo_frame, width = 20, text = "Quantity", style="My.TLabel").grid(row=2, column=0, sticky="nw", pady=(15,0), padx=(15,0))
    ttk.Scale(costInfo_frame, from_=0, to=10, command=onMove, variable=scaleVar, cursor="hand2", style="My.Horizontal.TScale", length=250).grid(row=2, column=1, columnspan=3, sticky="nsw", pady=(15,0))

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

    ##### Shipping Information Frame #####
    #shipping info label and underline
    shippingInfo_frame.grid_configure(row=2, columnspan=5, pady=10, padx=(50,0), sticky="nw")
    shippingInfoLabel = ttk.Label(shippingInfo_frame, style="My.TLabel", text="Shipping Info")
    shippingInfoLabel.config(font = ('rockwell', 12))
    shippingInfoLabel.grid(sticky="ns", column=0, columnspan=5)
    shippingInfoUnderline_line.grid(sticky="ns", column=0, columnspan=5)

    #create shipping info data
    shippingFields = 'Full name', 'Street address', 'City', 'State', 'Zip Code'
    shippingEntries = makeform(shippingInfo_frame, shippingFields)
    i = 0
    for shipEnt in shippingEntries:
        completeForm.append(shippingEntries[i])
        i = i + 1

    ##### Payment Information Frame #####
    #payment info label and underline
    paymentInfo_frame.grid_configure(row=3, columnspan=5, pady=10, padx=(50,0), sticky="nw")
    paymentInfoLabel = ttk.Label(paymentInfo_frame, style="My.TLabel", text="Payment Info")
    paymentInfoLabel.config(font = ('rockwell', 12))
    paymentInfoLabel.grid(sticky="ns", column=0, columnspan=5)
    paymentInfoUnderline_line.grid(sticky="ns", column=0, columnspan=5)

    #create payment info data
    paymentFields = 'Credit Card Number', 'CVC', 'Email'
    paymentEntries = makeform(paymentInfo_frame, paymentFields)
    i = 0
    for payEnt in paymentEntries:
        completeForm.append(paymentEntries[i])
        i = i + 1

    root.bind('<Return>', (lambda event: fetch(ents)))
    ttk.Button(rightInfo_frame, width=10, text = 'Submit', cursor="hand2", command = (lambda: confirmation(completeForm))).grid(column=0, columnspan=4, pady=(5, 15), sticky="ns")

    root.grid_columnconfigure(0, weight = 1)

root.mainloop()
