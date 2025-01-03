from tkinter import Tk,Entry,Button,Label,StringVar

#creating a window

window = Tk()

#width and length of window.
window.geometry("600x400")

window.title("Multi-language Dictionary")



entry_text =Entry(window)

entry_text.pack()


result = StringVar()
result_label=Label(window,textvariable=result)
result_label.pack()


Spanish_dictionary =  { "Hola" : "Hello",
                       "Adios" : "Goodbye",
                       "Gracias" : "Thankyou",
                       "Lo siento": "Excuse me/Sorry",
                       "Como estas?" : "How are you",
                       "Estoy bien" : "I am fine",
                       "Agua": "Water",
                       "Comida" : "Food",
                       "Casa" : "House",
                       "Coche" : "Car",
                       "Amigo" : "Friend",
                       "Familia" : "Family",
                       "Amor": "Love",
                       "Feliz": "Happy",
                       "Triste":"Sad",
                       "Verdad":"True",
                       "Falso":"False",
                       "Si":"Yes",
                       "No":"No"}

French_Dictionary = {
    "Viens": "Come",
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
    "Travail": "Work"
}

def search(word):
    if word in Spanish_dictionary:
        result.set(Spanish_dictionary[word])
        print(Spanish_dictionary[word])

    else:
        result.set("Not found")
        print("Not found")

def search(word):
    if word in French_Dictionary:
        result.set(French_Dictionary[word])
        print(French_Dictionary[word])

    else:
        result.set("Not found")
        print("Not found")


search_btn =Button(window,text = "search", command=lambda:search(entry_text.get()))
search_btn.pack()
window.mainloop()

