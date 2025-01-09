from re import search
from tkinter import Tk,Entry,Button,Label,StringVar


#creating a window

window = Tk()

#width and length of window.
window.geometry("600x400")

window.title("Multi-language Dictionary")


# To hold the text that will be displayed
result = StringVar()
result_label=Label(window,textvariable=result,font=("Arial",14))
result_label.pack()

Translations = {
    "Hello":{"Spanish": "Hola",
             "French":"Bonjour",
             "Hausa": "Sannu",
             "Korean":"Hello",
             "Japanese":"Konnichiwa"
             },
    "Thankyou":{"Spanish":"Gracias",
                "French":"Merci",
                "Hausa":"Nagode",
                "Korean":"Gamsahamnida",
                "Japanese":"Arigatou",
                },
}

Label(window, text="Enter a word:").pack()
input_entry = Entry(window)
input_entry.pack()

def show_translations():
    """"
    Fetches the translations of the input word from the dictionary and displays them.
   """
    word = input_entry.get().capitalize()
    if word in Translations:
        translations = Translations[word]
        result.set("\n".join([f"{lang}: {trans}" for lang, trans in translations.items()]))
    else:
        result.set("Word not found in dictionary")

Button(window, text="Show Translations", command=show_translations).pack()
window.mainloop()



window.mainloop()

