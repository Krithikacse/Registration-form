from tkinter import*
root = Tk()
root.geometry("500x300")

def getvals():
    print("Your form has been successfully submitted")

# Heading
Label(root, text="Python Registration Form", bg="blue", fg="white", font="arial 15 bold").grid(row=0, column=3)

# Field Name
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
course = Label(root, text="Course")
paymentmood = Label(root, text="Payment Mood")

# Packing Fields
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
course.grid(row=4, column=2)
paymentmood.grid(row=5, column=2)

# Variable for storing data
namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
coursevalue = StringVar
paymentmoodvalue = StringVar
checkvalue = IntVar

# Creating entry field
nameentry = Entry(root, textvariable =namevalue)
phoneentry = Entry(root, textvariable =phonevalue)
genderentry = Entry(root, textvariable =gendervalue)
courseentry = Entry(root, textvariable =coursevalue)
paymentmoodentry = Entry(root, textvariable =paymentmoodvalue)


# packing entry fields
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
courseentry.grid(row=4, column=3)
paymentmoodentry.grid(row=5, column=3)

# Creating Checkbox
checkbtn = Checkbutton(text="remember me?", variable = checkvalue)
checkbtn.grid(row=6, column= 3)

# Submit button
Button(text="Submit", command=getvals).grid(row=7, column=3)

root.mainloop()
