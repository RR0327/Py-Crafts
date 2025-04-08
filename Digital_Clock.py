"""import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")

clock_label = tk.Label(root,
                       font=("Helvetica", 48),
                       bg="black", fg ="cyan")

clock_label.pack(anchor="center", fill= "both",
                 expand= True)

def update_time():
    # current_time = strftime("%H:%M:%S")
    current_time = strftime("%I:%M:%S %p")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)


# date_label = tk.Label(root, font=("Helvetica", 24), bg="black", fg="white")
# date_label.pack(anchor="center")

# def update_date():
#     current_date = strftime("%A, %B %d, %Y")  # Example: "Friday, January 4, 2025"
#     date_label.config(text=current_date)
#     date_label.after(1000, update_date)

# update_date()

update_time()
root.mainloop()"""

"""import tkinter as tk
root = tk.Tk()
root.title("Test")
tk.Label(root, text="Tkinter is working!").pack()
root.mainloop()"""




