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


Spanish_dictionary =  { "Hello" : "Hola",
                       "Goodbye" : "Adios",
                       "Thankyou" : "Gracias",
                       "Excuse me/Sorry": "Lo siento",
                       "How are you?" : "Como estas?",
                       "I am fine" : "Estoy bien",
                       "Water": "Agua",
                       "Food" : "Comida",
                       "House" : "Casa",
                       "Car" : "Coche",
                       "Friend" : "Amigo",
                       "Family" : "Familia",
                       "Love": "Amor",
                       "Happy": "Feliz",
                       "Sad":"Triste",
                       "True":"Verdad",
                       "False":"Falso",
                       "Yes":"Si",
                       "No":"No"}

Hausa_dictionary = {"Zo" "Come",
                    "Baya" "Back",
                    "Je" "Go",
                    "Kalma" "Word",
                    "Kai" "Head",
                    "Hanu" "Hand",
                    "Litafi" "Bible",
                    "Mama" "Father",
                    "Woya""Phone",
                    "Daki" "Room",
                    "Waka" "Song",
                    "Suna" "Name",
                    "Dan Uwa" "Brother",
                    "Yar Uwa" "Sister",
                    "Wuta" "Light",
                    "Dama" "Right",
                    "Hagu" "Left",
                    "Mota" "Car",
                    "Hanya" "Road",
                    "Karshe" "Last",
                   }

French_Dictionary = {
    "Come": "Viens",
    "Go": "Aller",
    "Good morning": "Bonjour",
    "Hello": "Salut",
    "Good bye": "Au revior",
    "Thankyou": "Merci",
    "Thank you very much": "Merci beaucoup",
    "Excuse me": "Pardon",
    "Mister": "Monsieur",
    "Madam": "Madame",
    "Miss": "Mademoiselle",
    "Good": "Bon",
    "Big": "Grande",
    "Small": "Petit",
    "A boy": "Un Garcon",
    "A girl": "Une Fille",
    "House": "Maison",
    "School": "Lecole",
    "Car": "Voiture",
    "Beautiful": "Beau",
    "Work": "Travail"
}

def search(word):
    if word in Hausa_dictionary:
        result.set(Hausa_dictionary[word])
        print(Hausa_dictionary[word])

    else:
        result.set("Not found")
        print("Not found")

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


spanish_btn =Button(window,text = "spanish", command=lambda:search(entry_text.get()))
spanish_btn.pack()

french_btn = Button(window , text = "french", command=lambda: search(entry_text.get()))
french_btn.pack()


window.mainloop()

