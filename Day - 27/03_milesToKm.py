from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.minsize(50, 50)
window.config(padx=20, pady=20)

def calculate_km():
    mile = mile_input.get()
    km = round(int(mile) * 1.6)
    final_label.config(text=str(km))

mile_input = Entry()
mile_input.config(width=10)
mile_input.grid(column=1, row=0)

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

final_label = Label(text="")
final_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

cal_button = Button(text="calculate", command=calculate_km)
cal_button.grid(column=1, row=2)


window.mainloop()