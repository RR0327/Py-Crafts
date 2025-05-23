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


# Date and Time

import time
from time import strftime
import os

try:
    while True:
        # Get current time and date
        current_time = strftime("%I:%M:%S %p")       # 12-hour format
        current_date = strftime("%A, %B %d, %Y")     # e.g., Thursday, May 15, 2025

        # Clear screen (Windows: 'cls', Linux/macOS: 'clear')
        os.system('cls' if os.name == 'nt' else 'clear')

        # Display time and date
        print(f"⏰  {current_time}")
        print(f"📅  {current_date}")

        # Wait for 1 second
        time.sleep(1)
except KeyboardInterrupt:
    print("\nClock stopped.")

# CountDown

import time
import os
from datetime import timedelta

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def countdown_timer(days=0, hours=0, minutes=0, seconds=0):
    total_seconds = int(timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds).total_seconds())

    try:
        while total_seconds:
            # Convert total seconds back to days/hours/mins/secs
            time_left = str(timedelta(seconds=total_seconds))

            # Clear screen and show countdown
            clear_screen()
            print(f"⏳  Time Remaining: {time_left}")

            # Wait 1 second and decrement
            time.sleep(1)
            total_seconds -= 1

        # Time's up
        clear_screen()
        print("🚨 Time's up!")
    except KeyboardInterrupt:
        print("\n⛔ Countdown stopped.")

# 👇 Example: 5-day countdown
countdown_timer(days=5)
