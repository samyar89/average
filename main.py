from tkinter import *

root = Tk()

root.geometry("400x350")
root.title("محاسبه میانگین")

def average():
    numbers = number_entry.get()
    int_numbers = list(map(int, numbers.split(",")))
    
    avg = sum(int_numbers) / len(int_numbers)
    
    result_label.config(text=f"میانگین: {avg}")

number_label = Label(root, text="لطفا اعداد خود را با کاما جدا کنید:")
number_label.pack(pady=10)

number_entry = Entry(root, width=40)
number_entry.pack(pady=5)

calculate_button = Button(root, text="محاسبه میانگین", command=average)
calculate_button.pack(pady=10)

result_label = Label(root, text="")
result_label.pack()

root.mainloop()
