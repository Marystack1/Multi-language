

from tkinter import Tk, Entry, Button, Label, StringVar

# Creating a window
window = Tk()
window.geometry("300x150")
window.title("japanese dictionary")

entry_text = Entry(window)
entry_text.pack()

result = StringVar()
result_label = Label(window, textvariable=result)
result_label.pack()

japanese_dictionary ={
 "Warui" : "bad",
 "Kanashī" : "sad",
 "Mizu" : "water",
 "Onegaishimas " : "please",
 "Naze" : "why",
 "Namae " : "name",
 "hanasemasen" : "Japanese",
 "Motto" : "more",
 "Naku" : "cry",
 "Suwaru" : "sit",
 "Kuru" : "come",
 "Teishi" : "stop",
 "Tatakai" : "fight",
 "Iki o suru" : "breathe",
 "Kūki" : "air",
 "Enerugī" : "energy",
 "Josei" : "woman",
 "Anata" : "you",
 "Jaakuna" : "wicked",
 "Kōshi" : "lecturer",
 }


def search(word):
 if word in japanese_dictionary:
  result.set(japanese_dictionary[word])
 else:
  result.set("Not found")


search_btn = Button(window, text="Search", command=lambda: search(entry_text.get()))
search_btn.pack()
window.mainloop()