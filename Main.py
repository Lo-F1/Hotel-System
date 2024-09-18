from tkinter import *
from tkinter import messagebox
import random, os

# Functionality
def SaveBill():
    #global BillNumber
    Result = messagebox.askyesno("Confirm", "Do you want to save the bill?")
    if Result:
        BillContent = BillTextArea.get(1.0, END)
        #Create Directory if it doesn't exist
        if not os.path.exists('Bills'):
            os.makedirs('Bills')
        file = open(f'Bills/{BillNumber}.txt', 'w')
        file.write(BillContent)
        file.close()
        messagebox.showinfo("Success", f"Bill number {BillNumber} is saved successfully")

# Exit Button
def Exit():
    root.destroy()

# Reset Button
def Reset():
    CustomerNameEntry.delete(0, END)
    SodaEntry.delete(0, END)
    WaterEntry.delete(0, END)
    JuiceEntry.delete(0, END)
    WineEntry.delete(0, END)
    CoffeeEntry.delete(0, END)
    MilkEntry.delete(0, END)
    BlackTeaEntry.delete(0, END)
    MatokeEntry.delete(0, END)
    RiceEntry.delete(0, END)
    PoshoEntry.delete(0, END)
    MeatEntry.delete(0, END)
    BeansEntry.delete(0, END)
    VegetablesEntry.delete(0, END)
    ScreenEntry.delete(0, END)
    BillTextArea.delete(1.0, END)
    TaxEntry.delete(0, END)
    TotalEntry.delete(0, END)

# Total
def Total():
    global StringTax, StringTotal
    try: a1 = int(Soda.get())
    except: a1 = 0
    try: a2 = int(Water.get())
    except: a2 = 0
    try: a3 = int(Juice.get())
    except: a3 = 0
    try: a4 = int(Wine.get())
    except: a4 = 0
    try: a5 = int(Coffee.get())
    except: a5 = 0
    try: a6 = int(Milk.get())
    except: a6 = 0
    try: a7 = int(BlackTea.get())
    except: a7 = 0
    try: a8 = int(Matoke.get())
    except: a8 = 0
    try: a9 = int(Rice.get())
    except: a9 = 0
    try: a10 = int(Posho.get())
    except: a10 = 0
    try: a11 = int(Meat.get())
    except: a11 = 0
    try: a12 = int(Beans.get())
    except: a12 = 0
    try: a13 = int(Vegetables.get())
    except: a13 = 0

    global c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13
    c1 = 80 * a1
    c2 = 40 * a2
    c3 = 70 * a3
    c4 = 700 * a4
    c5 = 120 * a5
    c6 = 60 * a6
    c7 = 80 * a7
    c8 = 150 * a8
    c9 = 100 * a9
    c10 = 50 * a10
    c11 = 240 * a11
    c12 = 100 * a12
    c13 = 40 * a13
    NetPrice = c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9 + c10 + c11 + c12 + c13

    # Tax
    TotalTaxAmount = NetPrice * 0.16
    StringTax = "Ksh. " + str('%.2f' % TotalTaxAmount)
    TotalTax.set(StringTax)

    TotalCostAmount = NetPrice + TotalTaxAmount
    StringTotal = "Ksh. " + str('%.2f' % TotalCostAmount)
    TotalCost.set(StringTotal)

BillNumber = random.randint(1000, 100000)
# Text Area Display
def BillArea():
    BillTextArea.delete(1.0, END)

    if CustomerNameEntry.get() == '':
        messagebox.showerror("Error", "Enter customer name")
    elif TaxEntry.get() == '' and TotalEntry.get() == '':
        messagebox.showerror("Error", "No items billed")
    elif TaxEntry.get() == 'Ksh. 0.00' and TotalEntry.get() == 'Ksh. 0.00':
        messagebox.showerror("Error", "Bill cannot be equal to Zero. Bill an item to proceec")
    else:
        BillTextArea.insert(END, '     ** Welcome Customer **\n')
        BillTextArea.insert(END, f'\nBill Number: {BillNumber}')
        BillTextArea.insert(END, f'\nCustomer Name: {CustomerNameEntry.get()}')
        BillTextArea.insert(END, f'\n==============================')
        BillTextArea.insert(END, f'\nProduct\t      Qty\t    Price')
        BillTextArea.insert(END, f'\n==============================')
        if Soda.get() != '':
            BillTextArea.insert(END, f'\nSoda\t      {Soda.get()}\t      Sh. {c1}')
        if Water.get() != '':
            BillTextArea.insert(END, f'\nWater\t      {Water.get()}\t      Sh. {c2}')
        if Juice.get() != '':
            BillTextArea.insert(END, f'\nJuice\t      {Juice.get()}\t      Sh. {c3}')
        if Wine.get() != '':
            BillTextArea.insert(END, f'\nWine\t      {Wine.get()}\t      Sh. {c4}')

        if Coffee.get() != '':
            BillTextArea.insert(END, f'\nCoffee\t      {Coffee.get()}\t      Sh. {c5}')
        if Milk.get() != '':
            BillTextArea.insert(END, f'\nMilk\t      {Milk.get()}\t      Sh. {c6}')
        if BlackTea.get() != '':
            BillTextArea.insert(END, f'\nBlack Tea\t    {BlackTea.get()}\t      Sh. {c7}')

        if Matoke.get() != '':
            BillTextArea.insert(END, f'\nMatoke\t      {Matoke.get()}\t      Sh. {c8}')
        if Rice.get() != '':
            BillTextArea.insert(END, f'\nRice\t      {Rice.get()}\t      Sh. {c9}')
        if Posho.get() != '':
            BillTextArea.insert(END, f'\nPosho\t      {Posho.get()}\t      Sh. {c10}')

        if Meat.get() != '':
            BillTextArea.insert(END, f'\nMeat\t      {Meat.get()}\t      Sh. {c11}')
        if Beans.get() != '':
            BillTextArea.insert(END, f'\nBeans\t      {Beans.get()}\t      Sh. {c12}')
        if Vegetables.get() != '':
            BillTextArea.insert(END, f'\nVegetables\t   {Vegetables.get()}\t      Sh. {c13}')
        BillTextArea.insert(END, f'\n------------------------------')

        if TotalTax.get() != '':
            BillTextArea.insert(END, f'\nV.A.T\t         {StringTax}')

        BillTextArea.insert(END, f'\n\nTotal Bill\t      {StringTotal}')
        BillTextArea.insert(END, f'\n------------------------------')
        #SaveBill()

# combine the functions to populate the Bill Text Area and save the bill
def CombinedFunctions():
    BillArea()
    SaveBill()

# Calculator Functionality
def ButtonClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def ButtonClearDisplay():
    global operator
    operator = ""
    text_Input.set("")

def ButtonEquals():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)

# GUI
root = Tk()
root.title("Billing System")
root.geometry("1030x565+161+80")
root.resizable(False, False)
root.overrideredirect(True)

HeadingLabel = Label(root, text="HOTEL MANAGEMENT SYSTEM", fg="#FCE6C9", bg='#33A1C9', font=('Calibri', 33, 'bold'), width=300, height="1")
HeadingLabel.pack(fill=X)
HeadingCanvas = Canvas(root, height=5, bg="#756642", highlightthickness=0)
HeadingCanvas.pack(fill=X)
# Main Frame
MainFrame = Frame(root)
MainFrame.pack()
# The Left Frame containing the Customer Label and entry as well as menus
Frame1 = Frame(MainFrame)
Frame1.grid(row=0, column=0)
# Customer Name Label and Entry
CustomerNameLabel = Label(Frame1, text="Customer Name", foreground="#756642", font=('Calibri', 20, 'bold'))
CustomerNameLabel.grid(row=0, column=0, sticky=W)
CustomerNameEntry = Entry(Frame1, font=('Calibri', 20, 'bold'), bd=7, width=20)
CustomerNameEntry.grid(row=0, column=1, pady=2, padx=5)
CustomerLine = Canvas(Frame1, height=1, bg="#756642", highlightthickness=0)
CustomerLine.place(x=0, y=50, relwidth=1, relheight=0.009)

Soda = StringVar()
Water = StringVar()
Juice = StringVar()
Wine = StringVar()
Coffee = StringVar()
Milk = StringVar()
BlackTea = StringVar()
Matoke = StringVar()
Rice = StringVar()
Posho = StringVar()
Meat = StringVar()
Beans = StringVar()
Vegetables = StringVar()
TotalTax = StringVar()
TotalCost = StringVar()

# Calculator Functionality
text_Input = StringVar()
operator = ""

# Drinks Label Frame
ColdDrinksLabelFrame = LabelFrame(Frame1, text="Cold Drinks", font=('Calibri', 15, 'bold'), foreground="#756642")
ColdDrinksLabelFrame.grid(row=1, column=0, padx=5)
# Labels and Entries inside cold drinks Label Frame
SodaLabel = Label(ColdDrinksLabelFrame, text="Soda", font=('Calibri', 15, 'bold'), foreground='#DD8838')
SodaLabel.grid(row=0, column=0, pady=3, sticky=W)
SodaEntry = Entry(ColdDrinksLabelFrame, font=('Calibri', 18, 'bold'), textvariable=Soda, bd=5, width=12, bg='#FCE6C9')
SodaEntry.grid(row=0, column=1, pady=3)
WaterLabel = Label(ColdDrinksLabelFrame, text="Water", font=('Calibri', 15, 'bold'), foreground='#DD8838')
WaterLabel.grid(row=1, column=0, pady=3, sticky=W)
WaterEntry = Entry(ColdDrinksLabelFrame, font=('Calibri', 18, 'bold'), bd=5, textvariable=Water, width=12, bg='#FCE6C9')
WaterEntry.grid(row=1, column=1, pady=3)
JuiceLabel = Label(ColdDrinksLabelFrame, text="Juice", font=('Calibri', 15, 'bold'), foreground='#DD8838')
JuiceLabel.grid(row=2, column=0, pady=3, sticky=W)
JuiceEntry = Entry(ColdDrinksLabelFrame, font=('Calibri', 18, 'bold'), textvariable=Juice, bd=5, width=12, bg='#FCE6C9')
JuiceEntry.grid(row=2, column=1, pady=3)
WineLabel = Label(ColdDrinksLabelFrame, text="Wine", font=('Calibri', 15, 'bold'), foreground='#DD8838')
WineLabel.grid(row=3, column=0, pady=3, sticky=W)
WineEntry = Entry(ColdDrinksLabelFrame, font=('Calibri', 18, 'bold'), bd=5, textvariable=Wine, width=12, bg='#FCE6C9')
WineEntry.grid(row=3, column=1, pady=3)

# Hot drinks label frame inside the cold drinks label frame
HotDrinksLabelFrame = LabelFrame(ColdDrinksLabelFrame, text="Hot Drinks", font=('Calibri', 15, 'bold'), foreground="#756642")
HotDrinksLabelFrame.grid(row=4, column=0, columnspan=2, padx=5, pady=10)
# Labels and Entries inside Hot drinks Label Frame
CoffeeLabel = Label(HotDrinksLabelFrame, text="Coffee", font=('Calibri', 15, 'bold'), foreground='#DD8838')
CoffeeLabel.grid(row=0, column=0, pady=5, sticky=W)
CoffeeEntry = Entry(HotDrinksLabelFrame, font=('Calibri', 18, 'bold'), textvariable=Coffee, bd=5, width=10, bg='#FCE6C9')
CoffeeEntry.grid(row=0, column=1, pady=5)
MilkLabel = Label(HotDrinksLabelFrame, text="Milk", font=('Calibri', 15, 'bold'), foreground='#DD8838')
MilkLabel.grid(row=1, column=0, pady=5, sticky=W)
MilkEntry = Entry(HotDrinksLabelFrame, font=('Calibri', 18, 'bold'), textvariable=Milk, bd=5, width=10, bg='#FCE6C9')
MilkEntry.grid(row=1, column=1, pady=5)
BlackTeaLabel = Label(HotDrinksLabelFrame, text="Black Tea", font=('Calibri', 15, 'bold'), foreground='#DD8838')
BlackTeaLabel.grid(row=2, column=0, pady=5, sticky=W)
BlackTeaEntry = Entry(HotDrinksLabelFrame, font=('Calibri', 18, 'bold'), textvariable=BlackTea, bd=5, width=10, bg='#FCE6C9')
BlackTeaEntry.grid(row=2, column=1, pady=5)

# Label Frames Right side in Frame 1
# Foods Label Frame
FoodsLabelFrame = LabelFrame(Frame1, text="Foods", font=('Calibri', 15, 'bold'), foreground="#756642")
FoodsLabelFrame.grid(row=1, column=1)
# Labels and Entries inside cold drinks Label Frame
MatokeLabel = Label(FoodsLabelFrame, text="Matoke", font=('Calibri', 15, 'bold'), foreground='#DD8838')
MatokeLabel.grid(row=0, column=0, pady=5, sticky=W)
MatokeEntry = Entry(FoodsLabelFrame, font=('Calibri', 18, 'bold'), textvariable=Matoke, bd=5, width=12, bg='#FCE6C9')
MatokeEntry.grid(row=0, column=1, pady=5)
RiceLabel = Label(FoodsLabelFrame, text="Rice", font=('Calibri', 15, 'bold'), foreground='#DD8838')
RiceLabel.grid(row=1, column=0, pady=5, sticky=W)
RiceEntry = Entry(FoodsLabelFrame, font=('Calibri', 18, 'bold'), bd=5, textvariable=Rice, width=12, bg='#FCE6C9')
RiceEntry.grid(row=1, column=1, pady=5)
PoshoLabel = Label(FoodsLabelFrame, text="Posho", font=('Calibri', 15, 'bold'), foreground='#DD8838')
PoshoLabel.grid(row=2, column=0, pady=5, sticky=W)
PoshoEntry = Entry(FoodsLabelFrame, font=('Calibri', 18, 'bold'), textvariable=Posho, bd=5, width=12, bg='#FCE6C9')
PoshoEntry.grid(row=2, column=1, pady=5)

# Sauce label frame inside the cold drinks label frame
SauceLabelFrame = LabelFrame(FoodsLabelFrame, text="Sauce", font=('Calibri', 15, 'bold'), foreground="#756642")
SauceLabelFrame.grid(row=4, column=0, columnspan=2, pady=10, padx=5)
# Labels and Entries inside Hot drinks Label Frame
MeatLabel = Label(SauceLabelFrame, text="Meat", font=('Calibri', 15, 'bold'), foreground='#DD8838')
MeatLabel.grid(row=0, column=0, pady=10, sticky=W)
MeatEntry = Entry(SauceLabelFrame, font=('Calibri', 18, 'bold'), textvariable=Meat, bd=5, width=10, bg='#FCE6C9')
MeatEntry.grid(row=0, column=1, pady=10)
BeansLabel = Label(SauceLabelFrame, text="Beans", font=('Calibri', 15, 'bold'), foreground='#DD8838')
BeansLabel.grid(row=1, column=0, pady=10, sticky=W)
BeansEntry = Entry(SauceLabelFrame, font=('Calibri', 18, 'bold'), textvariable=Beans, bd=5, width=10, bg='#FCE6C9')
BeansEntry.grid(row=1, column=1, pady=10)
VegetablesLabel = Label(SauceLabelFrame, text="Vegetables", font=('Calibri', 15, 'bold'), foreground='#DD8838')
VegetablesLabel.grid(row=2, column=0, pady=10, sticky=W)
VegetablesEntry = Entry(SauceLabelFrame, font=('Calibri', 18, 'bold'), textvariable=Vegetables, bd=5, width=10, bg='#FCE6C9')
VegetablesEntry.grid(row=2, column=1, pady=10)

# The Left Frame containing the receipt, calculators and functional buttons
Frame2 = Frame(MainFrame)
Frame2.grid(row=0, column=1, padx=2)
# Frame to contain the bill text area and Calculator
Frame3 = Frame(Frame2)
Frame3.grid(row=0, column=0)

# Receipt Label Frame
ReceiptLabelFrame = LabelFrame(Frame3, text="Receipt", font=('Calibri', 15, 'bold'), foreground="#756642")
ReceiptLabelFrame.grid(row=0, column=0)
# Bill frame
BillFrame = Frame(ReceiptLabelFrame, bd=5, relief='ridge')
BillFrame.grid(row=0, column=0)
# Create scroll bar to view overflowing text
BillScrollBar = Scrollbar(BillFrame, orient=VERTICAL)
BillScrollBar.pack(side=RIGHT, fill=Y)
# Bill Text Area
BillTextArea = Text(BillFrame, height=18, width=30, yscrollcommand=BillScrollBar.set)
BillTextArea.pack()
# Functionality to be able to move the scroll Bar up and down
# Configuration
BillScrollBar.config(command=BillTextArea.yview)

# Calculator Label Frame
CalculatorLabelFrame = LabelFrame(Frame2, text='Calculator', font=('Calibri', 15, 'bold'), foreground="#756642")
CalculatorLabelFrame.grid(row=0, column=1, padx=10, pady=5)
# Calculator Frame
CalculatorFrame = Frame(CalculatorLabelFrame, bd=1, relief='ridge')
CalculatorFrame.grid(row=0, column=0)
# Calculator
ScreenEntry = Entry(CalculatorFrame, bd=5, width=13, justify='right', relief='ridge', textvariable=text_Input, font=('Calibri', 18, 'bold'), bg='#FCE6C9')
ScreenEntry.grid(row=0, column=0, columnspan=4, padx=2, pady=5)
# Calculator Buttons
# Row 1
btn7 = Button(CalculatorFrame, padx=3, pady=1, bd=2, fg='black', font=('Calibri', 18, 'bold'), text='7', command=lambda:ButtonClick(7))
btn7.grid(row=1, column=0)
btn8 = Button(CalculatorFrame, padx=3, pady=1, bd=2, fg='black', font=('Calibri', 18, 'bold'), text='8', command=lambda:ButtonClick(8))
btn8.grid(row=1, column=1)
btn9 = Button(CalculatorFrame, padx=3, pady=1, bd=2, fg='black', font=('Calibri', 18, 'bold'), text='9', command=lambda:ButtonClick(9))
btn9.grid(row=1, column=2)
btnAdd = Button(CalculatorFrame, padx=3, pady=1, bd=2, fg='black', font=('Calibri', 18, 'bold'), text='+', command=lambda:ButtonClick('+'))
btnAdd.grid(row=1, column=3)
# Row 2
btn4 = Button(CalculatorFrame, padx=3, pady=1, bd=2, fg='black', font=('Calibri', 18, 'bold'), text='4', command=lambda:ButtonClick(4))
btn4.grid(row=2, column=0)
btn5 = Button(CalculatorFrame, padx=3, pady=1, bd=2, fg='black', font=('Calibri', 18, 'bold'), text='5', command=lambda:ButtonClick(5))
btn5.grid(row=2, column=1)
btn6 = Button(CalculatorFrame, padx=3, pady=1, bd=2, fg='black', font=('Calibri', 18, 'bold'), text='6', command=lambda:ButtonClick(6))
btn6.grid(row=2, column=2)
btnSubtract = Button(CalculatorFrame, padx=6, pady=1, bd=2, fg='black', font=('Calibri', 18, 'bold'), text='-', command=lambda:ButtonClick('-'))
btnSubtract.grid(row=2, column=3)
# Row 3
btn1 = Button(CalculatorFrame, padx=3, pady=1, bd=2, fg='black', font=('Calibri', 18, 'bold'), text='1', command=lambda:ButtonClick(1))
btn1.grid(row=3, column=0)
btn2 = Button(CalculatorFrame, padx=3, pady=1, bd=2, fg='black', font=('Calibri', 18, 'bold'), text='2', command=lambda:ButtonClick(2))
btn2.grid(row=3, column=1)
btn3 = Button(CalculatorFrame, padx=3, pady=1, bd=2, fg='black', font=('Calibri', 18, 'bold'), text='3', command=lambda:ButtonClick(3))
btn3.grid(row=3, column=2)
btnMultiply = Button(CalculatorFrame, padx=3, pady=1, bd=2, fg='black', font=('Calibri', 18, 'bold'), text='*', command=lambda:ButtonClick('*'))
btnMultiply.grid(row=3, column=3)
# Row 4
btn0 = Button(CalculatorFrame, padx=3, pady=1, bd=2, fg='black', font=('Calibri', 18, 'bold'), text='0', command=lambda:ButtonClick(0))
btn0.grid(row=4, column=0)
btnDecimal = Button(CalculatorFrame, padx=6, pady=1, bd=2, fg='black', font=('Calibri', 18, 'bold'), text='.', command=lambda:ButtonClick('.'))
btnDecimal.grid(row=4, column=1)
btnClear = Button(CalculatorFrame, padx=3, pady=1, bd=2, fg='black', font=('Calibri', 18, 'bold'), text='C', command=lambda:ButtonClearDisplay())
btnClear.grid(row=4, column=2)
btnDivide = Button(CalculatorFrame, padx=4, pady=1, bd=2, fg='black', font=('Calibri', 18, 'bold'), text='/', command=lambda:ButtonClick('/'))
btnDivide.grid(row=4, column=3)
# Row 5
btnEquals = Button(CalculatorFrame, bd=2, fg='black', font=('Calibri', 18, 'bold'), text='              =             ', command=lambda:ButtonEquals())
btnEquals.grid(row=5, column=0, columnspan=4)

# Frame to contain buttons
ButtonFrame = Frame(Frame2)
ButtonFrame.grid(row=1, column=0, columnspan=4)
# System Buttons
TaxLabel = Label(ButtonFrame, text="      Tax      ", font=('Calibri', 15, 'bold'), foreground='#DD8838')
TaxLabel.grid(row=0, column=0, padx=20, pady=5)
TaxEntry = Entry(ButtonFrame, font=('Calibri', 18, 'bold'), bd=2, textvariable=TotalTax, width=20, bg='#FCE6C9')
TaxEntry.grid(row=0, column=1, columnspan=3, pady=5)
TotalButton = Button(ButtonFrame, text="      Total      ", font=('Calibri', 15, 'bold'), foreground='#FCE6C9', bg="#756642", command=Total)
TotalButton.grid(row=1, column=0, padx=20, pady=5)
TotalEntry = Entry(ButtonFrame, font=('Calibri', 18, 'bold'), bd=2, textvariable=TotalCost, width=20, bg='#FCE6C9')
TotalEntry.grid(row=1, column=1, columnspan=3, pady=5)

ReceiptButton = Button(ButtonFrame, text="Print Receipt", font=('Calibri', 15, 'bold'), foreground='#FCE6C9', bg="#756642", command=CombinedFunctions)
ReceiptButton.grid(row=2, column=0, padx=20, pady=5)
ResetButton = Button(ButtonFrame, text="    Reset    ", font=('Calibri', 15, 'bold'), foreground='#FCE6C9', bg="#756642", command=Reset)
ResetButton.grid(row=2, column=1, padx=20, pady=5)
ExitButton = Button(ButtonFrame, text="     Exit     ", font=('Calibri', 15, 'bold'), foreground='#FCE6C9', bg="#756642", command=Exit)
ExitButton.grid(row=2, column=2, padx=20, pady=5)

root.mainloop()