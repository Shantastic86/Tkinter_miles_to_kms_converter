import tkinter as tk

FONT = ("Arial", 12, "bold")


def miles_to_kms():
    miles = float(input_miles.get())
    kms = miles * 1.60934
    input_kms.delete(0, tk.END)
    input_kms.insert(0, round(kms, 2))


window = tk.Tk()
window.title("Mile to Kilometer Converter")
window.config(padx=20, pady=20)
window.minsize(500, 300)

# Entry for miles
input_miles = tk.Entry(width=7)
input_miles.grid(row=0, column=1)

# Entry for kilometres
input_kms = tk.Entry(width=7)
input_kms.grid(row=1, column=1)

miles = tk.Label(window, text="Miles", font=FONT)
miles.grid(row=0, column=2)

is_equal_to = tk.Label(window, text="is equal to", font=FONT)
is_equal_to.grid(row=1, column=0)

km = tk.Label(window, text="Km", font=FONT)
km.grid(row=1, column=2)

# Creating a button
button = tk.Button(text="Calculate", command=miles_to_kms)
button.grid(row=2, column=1)

window.mainloop()