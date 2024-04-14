from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label_title = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
label_title.grid(column=2, row=1)

canvas = Canvas(width=240, height=224 , bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="./tomato.png")
canvas.create_image(120,112, image=img)
canvas.create_text(120,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

start_btn = Button(text="Start")
start_btn.grid(column=1, row=3)

reset_btn = Button(text="Reset")
reset_btn.grid(column=3, row=3)

ticket_label = Label(text="✔", bg=YELLOW, fg=GREEN)
ticket_label.grid(column=2, row=4)


window.mainloop()