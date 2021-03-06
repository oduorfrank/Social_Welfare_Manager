import tkinter
from tkinter import * 

win = Tk()
win.geometry('900x300')
win.title("Social Welfare")

# Labels for the data defined here
date = Label(win, text = 'Date: ')
date.grid(row = 0, column = 0)
hospNumber = Label(win, text = 'Hospital Number: ')
hospNumber.grid(row = 0, column = 3 )
name = Label(win, text = 'Name: ')
name.grid(row = 2, column = 0 )
age = Label(win, text = 'Age: ')
age.grid(row = 2, column = 3 )
department = Label(win, text = 'Department: ')
department.grid(row = 3, column = 0 )
residence = Label(win, text = 'Residence: ')
residence.grid(row = 3, column = 3 )
sex = Label(win, text = 'Sex: ')
sex.grid(row = 4, column = 0 )
reasonWaiver = Label(win, text = 'Reason for Waiver: ')
reasonWaiver.grid(row = 8, column = 0 )
totalAmount = Label(win, text = 'Total Amount: ')
totalAmount.grid(row = 7, column = 0 )
waiverAmount = Label(win, text = 'Amount Waived: ')
waiverAmount.grid(row = 7, column = 3)
waiverNo = Label(win, text = 'Waiver Number: ')
waiverNo.grid(row = 0, column = 6 ) 

# data for entry boxes defined here
data_1 = IntVar()
hospital_Number = IntVar()
name_1 = StringVar()
age_1 = IntVar()
department_1 = StringVar()
residence_1 = StringVar()
sex_1 = StringVar()
reason_waiver = StringVar()
total_amount = IntVar()
amount_waived = IntVar()
waiver_number = IntVar()

# Entry boxes for the data defined here
date1 = Entry(win, textvariable = data_1)
date1.grid(row = 0, column = 1)
hospNumber1 = Entry(win, textvariable = hospital_Number)
hospNumber1.grid(row = 0, column = 4 )
name1 = Entry(win, textvariable = name_1)
name1.grid(row = 3, column = 1 )
age1 = Entry(win, textvariable = age_1)
age1.grid(row = 2, column = 4 )
department1 = Entry(win, textvariable = department_1)
department1.grid(row = 2, column = 1 )
residence1 = Entry(win, textvariable = residence_1)
residence1.grid(row = 3, column = 4 )
sex1 = Entry(win, textvariable = sex_1)
sex1.grid(row = 4, column = 1 )
reasonWaiver1 = Entry(win, textvariable = reason_waiver)
reasonWaiver1.grid(row = 9, column = 0, rowspan = 3, columnspan = 4)
totalAmount1 = Entry(win, textvariable = total_amount)
totalAmount1.grid(row = 7, column = 1 )
waiverAmount1 = Entry(win, textvariable = amount_waived)
waiverAmount1.grid(row = 7, column = 4)
waiverNo1 = Entry(win, textvariable = waiver_number)
waiverNo1.grid(row = 0, column = 7 ) 



win.mainloop()