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

ShoppingCart = []
Total = 0

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
def updateCost():
	
	myTotal = 0
	
	for each in ShoppingCart:
		count = 0
		for i in range(len(each[1])):
			if(int(each[1][i]) == 1):
				count = count + 1
				
		myTotal = myTotal + (2+count)*int(each[2])
				
	Total = myTotal

	print("Total is "+ str(Total))


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
        updateCosts()
        pick = var.get()
        print('You pressed', pick)
        print('Result:', pick)


def insertCartIntoCartList():
    for each in ShoppingCart:
         shoppingList.insert(tk.END, str(each[0]) + "      Quantity: " + str(each[2])) # add it to the bottom!
         #shoppingList.insert(tk.END, each[2])
         for i in range(len(each[1])):

            if(i== 0 and int((each[1][0])) == 1):
                shoppingList.insert(tk.END, "    Straw Berry            $1.00" )
                print("strawberry")
            if(i == 1 and int((each[1][1])) == 1):
                shoppingList.insert(tk.END, "    Blue Berry              $1.00" )
                print("blueberry")
            if(i == 2 and int((each[1][2])) == 1):
                shoppingList.insert(tk.END, "    Cream Cheese      $1.00" )
                print("creamcheese")
            if(i == 3 and int((each[1][3])) == 1):
                shoppingList.insert(tk.END, "    Butter                     $1.00" )
                print("butter")

            
         
        

def addToCart():
    if(var.get() is not 0):

        Shmears = list(map((lambda vars: vars.get()), states))

        myShmears = ""

        for each in Shmears:
            myShmears = myShmears + str(each)

        found = False
			
        for each in ShoppingCart:
            if (each[0] == versions[var.get()-1]) and (each[1] == myShmears):
		#already entered
		#increment the last values
                each[2] = each[2]+1
                found = True

        if found: # clear the shopping List and reenter all the values
            shoppingList.delete(0, 'end')
            insertCartIntoCartList()
		
        else: #not found in Shopping Cart

            #shoppingList.insert(tk.END, versions[var.get()-1]) # add it to the bottom!
        
            ShoppingCart.append([versions[var.get()-1], myShmears, 1])

	    #for each in Shmears:
	    #   print(each)

            SmallList = [] 
            SmallList.append([versions[var.get()-1], myShmears, 1]) # alist of just the current entry for the for loop
																# did it for simplicity since I wrote the code below
			
			
            for each in SmallList:
                print("In cart")
                print( str(each[0]))
                #shoppingList.insert(tk.END, each[2])
                shoppingList.insert(tk.END, str(each[0]) + "      Quantity: " + str(each[2])) # add it to the bottom!
                for i in range(len(each[1])):

                    if(i== 0 and int((each[1][0])) == 1):
                        shoppingList.insert(tk.END, "    Straw Berry            $1.00" )
                        print("strawberry")
                    if(i == 1 and int((each[1][1])) == 1):
                        shoppingList.insert(tk.END, "    Blue Berry              $1.00" )
                        print("blueberry")
                    if(i == 2 and int((each[1][2])) == 1):
                        shoppingList.insert(tk.END, "    Cream Cheese      $1.00" )
                        print("creamcheese")
                    if(i == 3 and int((each[1][3])) == 1):
                        shoppingList.insert(tk.END, "    Butter                     $1.00" )
                        print("butter")

                
        updateCost()


        

        

def deleteCart():
        ShoppingCart.clear()

        print("deleted shopping cart check")

        for each in ShoppingCart:
            print (each[0])

        print("if nothing above, the cart was deleted!")
        # clear the list! on display!
        shoppingList.delete(0, 'end')

        
        
def report():
<<<<<<< HEAD
        updateCosts()
=======
    #updateCosts(var.get(), list(map((lambda vars: vars.get()), states)))
>>>>>>> a7762be4f3109cca642ae7460ef102287e725ebf
        
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

##### Cash Window #####
def cash():
    cashWindow = tk.Toplevel(root)
    cashWindow.title("Your Order Has Been Placed")
    confirm_frame = ttk.Frame(cashWindow, style="My.TFrame")
    confirm_frame.grid_configure(columnspan=2, pady=30, padx=30, sticky="ns")
    confirm_frame.grid_columnconfigure(0, weight = 1)
    w = tk.Label(confirm_frame, text = "Your order has been placed \n\nPlease pay at the register\n\nThank you")
    w.grid(pady=30, padx=30, sticky="n")
    i = 0
    eRow = 0
    ttk.Button(confirm_frame, text = 'Close window', cursor="hand2", command=cashWindow.destroy).grid(column=0, pady=(5, 20), columnspan=2, sticky="ns")

def credit():
    creditWindow = tk.Toplevel(root)
    creditWindow.title("Please confirm your order")
    confirm_frame = ttk.Frame(creditWindow, style="My.TFrame", width=400, height=675)
    confirm_frame.grid_configure(columnspan=2, pady=30, padx=30, sticky="ns")
    confirm_frame.grid_columnconfigure(0, weight = 1)
    w = tk.Label(confirm_frame, text = "Please confirm your order\n")
    w.grid(pady=30, padx=30, sticky="n")
    ttk.Button(confirm_frame, text = 'Confirm Order', cursor="hand2", command=creditWindow.destroy).grid(column=0, pady=(5, 20), columnspan=2, sticky="ns")


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
def updateCosts():
    #quantity = scaleVar.get()
    print(tipAmount)
    #costEntries[2].insert(0, tipAmount*.5)
    costEntries[2].config(state=tk.NORMAL)
    costEntries[2].delete(0, tk.END)
    costEntries[2].insert(0, tipAmount)
    costEntries[2].config(state=tk.DISABLED)

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

    #addOn_frame.grid_configure(row=5, column=0, columnspan=4, pady=(30,30), padx=10, sticky="sw")
    
    
    product_frame.grid_configure(column=2, columnspan=3, pady=30, padx=(30,30), sticky="e")
    var = tk.IntVar()
    versions = 'Blueberry Bagel -- $2.00', 'Plain Bagel -- $2.00', 'Seasame Bagel -- $2.00', 'Poppy Bagel -- $2.00', 'Onion Bagel -- $2.00', 'Pumpernickel Bagel -- $2.00' 
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

    ##### Shmear Frame #####
    #accessories label and underline
    addOn_frame.grid_configure(row=5, column=0, columnspan=4, pady=(30,30), padx=10, sticky="sw")
    addOnLabel = ttk.Label(addOn_frame, style="My.TLabel", text="Toppings")
    addOnLabel.config(font = ('calibri', 16))
    addOnLabel.grid(sticky="ns", column=0, columnspan=3)

    checkButtons_frame.grid_configure(row=5, column=0, columnspan=4, pady=(30,30), padx=10, sticky="se")
    blankButton = tk.PhotoImage(file= gifdir + "buttonblank.png")
    cartButton = ttk.Button(checkButtons_frame, width=50, text = 'Add to Cart', cursor="hand2", command = addToCart).grid(column=0, row=1, columnspan=1, pady=(5, 15), sticky="sw")
<<<<<<< HEAD
=======
    deleteButton = ttk.Button(checkButtons_frame, width=50, text = 'Delete Entire Cart', cursor="hand2", command = deleteCart).grid(column=0, row=2, columnspan=1, pady=(5, 15), sticky="sw")
    #cartButton.config(height=500, width=500)
    #checkButtonsLabel.config(font = ('rockwell', 12))
    #checkButtonsLabel.grid(sticky="se", column=0, columnspan=3)
    #checkButtonsUnderline_line.grid(sticky="se", column=0, columnspan=2, pady=(0,5))
>>>>>>> a7762be4f3109cca642ae7460ef102287e725ebf



    states = []
    amounts = []
    num = tk.IntVar()
    buttons = 'Strawberry Shmear -- $1.00', 'Blueberry Shmear -- $1.00', 'Cream Cheese -- $1.00', 'Butter -- $1.00'
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
    costInfo_frame.grid_configure(row=1, columnspan=5, pady=10, padx=(50,50), sticky="nw")
    costInfoLabel = ttk.Label(costInfo_frame, style="My.TLabel", text="Cost Info")
    costInfoLabel.config(font = ('calibri', 16))
    costInfoLabel.grid(sticky="ns", column=0, columnspan=5)

    completeForm = []

    #create cost info data
    costFields = 'Subtotal','Discount', 'Tax', 'Total'
    costEntries = makeform(costInfo_frame, costFields)
    i = 0
    for costEnt in costEntries:
        completeForm.append(costEntries[i])
        costEntries[i].insert(0, Total)
        costEntries[i].config(state=tk.DISABLED)
        i = i + 1

    root.bind('<Return>', (lambda event: fetch(ents)))
    ttk.Button(cartInfo_frame, width=10, text = 'Cash', cursor="hand2", command = cash).grid(column=0, columnspan=4, pady=(5, 5), sticky="s")

    tipAmount = tk.IntVar()
    tips = 'No tip', 'Tip - 5%', 'Tip - 10%', 'Tip - 15%', 'Tip - 20%' 
    i = 1
    rowNo = 0
    colNo = 0

    #loop to display the tip radio buttons
    for tip in tips:
        if i % 2 == 0:
            rowNo = 1
            colNo = 0
        ttk.Radiobutton(cartInfo_frame, text = tip, command = updateCosts, value = i, variable = tipAmount, style="My.TRadiobutton", cursor="hand2").grid(pady=2, padx=5, sticky="n")
        colNo = colNo + 1
        i = i + 1

    
    ttk.Button(cartInfo_frame, width=10, text = 'Credit', cursor="hand2", command = credit).grid(column=0, columnspan=4, pady=(5, 5), sticky="s")
    shoppingList = tk.Listbox(cartInfo_frame, height = 10, width = 50)
    listScroll = tk.Scrollbar(cartInfo_frame)
    listScroll.grid(column=1, row=0, sticky="NSW", pady=10, padx=10)
    shoppingList.grid_configure(row=0, column=0, pady=10, padx=10, sticky="n")
    listScroll.config(command=shoppingList.yview)
    shoppingList.config(yscrollcommand=listScroll.set)

    root.grid_columnconfigure(0, weight = 1)

root.mainloop()
