from tkinter import *
window = Tk()

window.title("Fibonacci Series")
window.geometry("500x500")

label_series = Label(window , text = "Fibonacci Series:")

def fibonacci():
    first_number = 0
    second_number = 1
    sum = 0
    counter = 1
    num = 10

    while(counter <= num):
        label_series['text']+= str(sum)+" "
        counter = counter+1
        first_number = second_number
        second_number = sum
        sum = first_number+second_number
btn = Button(window, text = "click me " , command = fibonacci)
btn.pack()
label_series.pack()

window.mainloop()