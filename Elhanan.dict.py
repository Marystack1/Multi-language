from tkinter import Tk, Entry, Button,Label, StringVar

#creating a window

window = Tk()

#width and length of window
window.geometry()

window.title("French Dictionary")


entry_text = Entry(window)

entry_text.pack()

result=StringVar()
result_label=Label(window,textvariable=result)
result_label.pack()




French_Dictionary = {"Viens": "Come",
                     "Aller": "Go",
                     "Bonjour": "Good morning",
                     "Salut": "Hello",
                     "Au revoir": "Goodbye",
                     "Merci": "Thank you",
                     "Merci beaucoup": "Thank you very much",
                     "Pardon": "Excuse me",
                     "Monsieur": "Mister",
                     "Madame": "Madam",
                     "Mademoiselle": "Miss",
                     "Bon": "Good",
                     "Grande": "Big",
                     "Petit": "Small",
                     "Un Garcon": "A Boy",
                     "Une Fille": "A Girl",
                     "Maison": "House",
                     "Lecole": "School",
                     "Voiture": "Car",
                     "Beau": "Beautiful",
                     "work": "Travail"}

def search(word):
     if word in French_Dictionary:
         result.set(French_Dictionary[word])
         print(French_Dictionary[word])

     else:
         result.set("Not found")
         print("Not found")


search_btn = Button(window, text="search", command=lambda:search(entry_text.get))
search_btn.pack()
window.mainloop()