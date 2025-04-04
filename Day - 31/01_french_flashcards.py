from tkinter  import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_HEADING_FONT = ('Ariel', 40, 'italic')
LANGUAGE_WORD_FONT = ('Ariel', 60, 'bold')
timer_tt = None
DATA_DIR = []
current_dir = {}

def file_load():
    global DATA_DIR
    data_csv = None
    try:
        data_csv = pandas.read_csv('./data/words_to_learn.csv')
    except FileNotFoundError:
        data_csv = pandas.read_csv('./data/french_words.csv')
    finally:
        DATA_DIR = data_csv.to_dict(orient="records")

def update_word_file():
    global DATA_DIR
    DATA_DIR.remove(current_dir)
    dir_data = pandas.DataFrame(DATA_DIR)
    dir_data.to_csv('./data/words_to_learn.csv', index=False)
    update_word()

def update_word():
    global DATA_DIR, current_dir
    global timer_tt
    if not timer_tt is None:
        window.after_cancel(timer_tt)
    current_dir = random.choice(DATA_DIR)
    english_word = current_dir['English']
    canvas.itemconfig(front_canvas, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill='black')
    canvas.itemconfig(card_word, text=f"{current_dir['French']}", fill='black')
    timer_tt = window.after(3000, flip_flashcard, english_word)

def flip_flashcard(english_word):
    canvas.itemconfig(front_canvas, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill='white')
    canvas.itemconfig(card_word, text=f"{english_word}", fill='white')

file_load()
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
front_canvas = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=LANGUAGE_HEADING_FONT)
card_word = canvas.create_text(400, 263, text=f"Word", font=LANGUAGE_WORD_FONT)
canvas.grid(column=0, row=0, columnspan=2)

wrong_path = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_path, highlightthickness=0, command=update_word)
wrong_btn.grid(column=0, row=1)

right_path = PhotoImage(file="images/right.png")
right_btn = Button(image=right_path, highlightthickness=0, command=update_word_file)
right_btn.grid(column=1, row=1)

update_word()
window.mainloop()