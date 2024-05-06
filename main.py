from tkinter import *
from tkinter import messagebox


def morse_code():
    original_text = text_input.get()
    morse_code = {'a': '.-',
                  'b': '-...',
                  'c': '-.-.',
                  'd': '-..',
                  'e': '.',
                  'f': '..-.',
                  'g': '--.',
                  'h': '....',
                  'i': '..',
                  'j': '.---',
                  'k': '-.-',
                  'l': '.-..',
                  'm': '--',
                  'n': '-.',
                  'o': '---',
                  'p': '.--.',
                  'q': '--.-',
                  'r': '.-.',
                  's': '...',
                  't': '-',
                  'u': '..-',
                  'v': '...-',
                  'w': '.--',
                  'x': '-..-',
                  'y': '-.--',
                  'z': '--..',
                  '1': '.----',
                  '2': '..---',
                  '3': '...--',
                  '4': '....-',
                  '5': '.....',
                  '6': '-....',
                  '7': '--...',
                  '8': '---..',
                  '9': '----.',
                  '0': '-----'
                  }

    translated_text = []
    try:
        for letter in original_text:
            char = morse_code[letter]
            translated_text.append(char)
        messagebox.showinfo(title="Here is the Morse Code", message=translated_text)
    except KeyError:
        messagebox.showinfo(title="Oops: Invalid Character", message="Please use characters A-Z and 0-9")

window = Tk()
window.title("Morse Code Converter")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

text_input = Entry(width=40)
text_input.grid(column=1, row=1)

my_label = Label(text='Enter your original text code?')
my_label.grid(column=1, row=0)

button = Button(text='convert', command=morse_code)
button.grid(column=1, row=2)

window.mainloop()
