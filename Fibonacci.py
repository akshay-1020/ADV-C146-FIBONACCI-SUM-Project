from tkinter import *

root = Tk()
root.title("Fibonacci Experiment")
root.geometry("400x400")
root.configure(bg = "coral")
box = Entry(root)

label_series = Label(root, text="Fibonacci Series:   ", bg = "coral")
label_sum = Label(root, bg = "coral")

def Fibonacci():
    num = int(box.get())
    first_no = 0
    second_no = 1
    sum = 0
    counter = 1
    lblsum = 0
    while (counter <= num):
        label_series["text"] += str(sum) + " "
        counter = counter + 1
        first_no = second_no
        second_no = sum
        sum = first_no + second_no
        lblsum = lblsum + second_no
        label_sum['text'] = "The sum is " + str(lblsum) + "."    

btn = Button(root, text="Show Fibonacci Series", command=Fibonacci, bg="black", fg = "white")
box.pack()
btn.pack()
label_series.pack()
label_sum.pack()

root.mainloop()