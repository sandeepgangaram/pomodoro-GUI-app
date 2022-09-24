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
reps = 4
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(canvas_text, text="00:00")
    check_label.config(text="")
    timer_label.config(text="Timer", font=(FONT_NAME, "40", "bold"), fg=GREEN)
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 8 == 8:
        count_down(long_break_sec)
        timer_label.config(text="Break", font=(FONT_NAME, "40", "bold"), fg=RED)

    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", font=(FONT_NAME, "40", "bold"), fg=PINK)

    else:
        count_down(work_sec)
        timer_label.config(text="Work", font=(FONT_NAME, "40", "bold"), fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = count // 60  # same as Math.floor(count/60) - // is called integer division
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(canvas_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        check_label.config(text="✔" * (reps // 2))


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(width=200, height=224, bg=YELLOW)
window.config(pady=50, padx=100)

#Labels
timer_label = Label(text="Timer")
timer_label.config(font=(FONT_NAME, "40", "bold"), fg=GREEN, bg=YELLOW)


check_label = Label(text="")
check_label.config(font=(FONT_NAME, "20", "bold"), fg=GREEN, bg=YELLOW, pady=50)

#Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato)
canvas_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, "35", "bold"))

#Buttons
start_button = Button(text="Start")
start_button.config(command=start_timer)

# start_button.config(pady=10, padx=20, borderwidth=0)
reset_button = Button(text="Reset", command=reset_timer)


#layout
timer_label.grid(row=0, column=1)
canvas.grid(row=1, column=1)
start_button.grid(row=2, column=0)
reset_button.grid(row=2, column=2)
check_label.grid(row=2, column=1)

window.mainloop()
