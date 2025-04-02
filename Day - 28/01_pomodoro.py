import math
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
reps = 0
timer_tt = None
# ---------------------------- TIMER RESET ------------------------------- #
def timer_reset():
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    tick_mark.config(text="")
    window.after_cancel(timer_tt)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = 5#WORK_MIN * 60
    short_break_sec = 5 #SHORT_BREAK_MIN * 60
    long_break_sec = 10 #LONG_BREAK_MIN * 60
    reps += 1

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif not reps % 2 == 0:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minute = str(math.floor(count/60)).zfill(2)
    sec = str(count % 60).zfill(2)
    canvas.itemconfig(timer_text, text=f"{minute}:{sec}")
    if count > 0:
        global timer_tt
        timer_tt = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        global reps
        if not reps % 2 == 0:
            tick_mark.config(text="✔"*(math.floor(reps/2)))


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
photo_image = PhotoImage(file="tomato.png")
canvas.create_image(105, 112, image=photo_image)
timer_text = canvas.create_text(105, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

start_btn = Button(text="Start", highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", highlightthickness=0, command=timer_reset)
reset_btn.grid(column=2, row=2)

tick_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
tick_mark.grid(column=1, row=3)



window.mainloop()