from tkinter import *

class loancalculator:
    def __init__(self):
        window = Tk()
        window.title("Loan Calculator")
        window.configure(background = "light green")
        Label(window, font="Helvetica 12 bold",bg="light green",text="anual interest rate").grid(row=1,column=1,sticky=W)
        Label(window, font="Helvetica 12 bold", bg="light green", text="number of year").grid(row=2, column=1,sticky=W)
        Label(window, font="Helvetica 12 bold", bg="light green", text="loan amount").grid(row=3, column=1,sticky=W)
        Label(window, font="Helvetica 12 bold", bg="light green", text="monthly payment").grid(row=4, column=1, sticky=W)
        Label(window, font="Helvetica 12 bold", bg="light green", text="total amount").grid(row=5, column=1,sticky=W)
                                
        self.annualInterestRateVar = StringVar()
        Entry(window, textvariable=self.annualInterestRateVar,justify=RIGHT).grid(row=1,column=2)
        self.numberofYearVar = StringVar()
        Entry(window, textvariable=self.numberofYearVar, justify=RIGHT).grid(row=2, column=2)
        self.loanAmountVar = StringVar()
        Entry(window, textvariable=self.loanAmountVar, justify=RIGHT).grid(row=3, column=2)
        self.monthlyPaymentVar = StringVar()
        IblMonthlyPayment=  Label(window, font="Helvetica 12 bold", bg="light green", textvariable=self.monthlyPaymentVar).grid(row=4, column=2, sticky=E)
        self.totalPaymentVar = StringVar()
        IblTotalPayment = Label(window, font="Helvetica 12 bold", bg="light green" ,textvariable=self.totalPaymentVar).grid(row=5, column=2, sticky=E)

        btComputePayment = Button(window,text="Compute payment",bg="blue",fg="white",font="Helvetica 12 bold",command=self.computePayment).grid(row=6,column=2,sticky=E)
        btclear = Button(window, text="Clear", bg="red", fg="white",font="Helvetica 12 bold",command=self.delete_all).grid(row=6, column=8, padx=25, pady=25, sticky=E)
        
        window.mainloop()
        
    def computePayment(self):
        monthlyPayment = self.getMonthlyPayment(
            float(self.loanAmountVar.get()),
            float(self.annualInterestRateVar.get())  / 1200 ,
            int(self.numberofYearVar.get()))
        
        
        self.monthlyPaymentVar.set(format(monthlyPayment,'10.2f'))
        totalPayment = float(self.monthlyPaymentVar.get()) *12 \
          * int(self.numberofYearVar.get()) 
        self.totalPaymentVar.set(format(totalPayment,'10.2f'))
    def getMonthlyPayment(self,loanAmount,monthlyInterestRate,numberofYears):   
        monthlyPayment = loanAmount * monthlyInterestRate / (1-1/(1 + monthlyInterestRate)** (numberofYears * 12))
        return monthlyPayment;

    def delete_all(self):
        self.monthlyPaymentVar.set("")
        self.loanAmountVar.set("")
        self.annualInterestRateVar.set("")
        self.numberofYearVar.set("")
        self.totalPaymentVar.set("")

loancalculator()
              
        