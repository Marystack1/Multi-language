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
             "French":"Salut",
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
    "Goodbye":{"Spanish":"Adios",
           "French":"Au revoir",
           "Hausa":"Sai an juma",
           "Korean":"annyeonghi gaseyo",
           "Japanese":"Sayonara",
           }
"Yes":{"Spanish":"Si",
       "French":"Oui",
       "Hausa":"Iya",
       "Korean":"Ne",
       "Japanese":"Hai",
      }
"No":{"Spanish":"No",
      "French":"Non",
      "Hausa":"A'a",
      "Korean":"Aniyo",
      "Japanese":"Ije",
      }
"Excuse me":{"Spanish":"Lo siento",
             "French":"Excusez-moi",
             "Hausa":"Gafara",
             "Korean":"Joheunhamnida",
             "Japanese":"Sumimasen",
             }
"Tree":{"Spanish":"Arbol",
        "French":"Arbre",
        "Hausa":"Bishiya",
        "Korean":"Namu",
        "Japanese":"Ki",
         }
"Cat":{"Spanish":"Gato",
       "French":"Chat",
       "Hausa":"Muskule",
       "Korean":"Goyang-i",
       }
"Dog":{"Spanish":"Peru",
       "Ffench":"Chien",
       "Hausa":"Kare",
       "Korean":"Gae",
       "Japanese":"Inu",
       }
"Sun":{"Spanish":"sol",
       "French":"Soliel",
       "Hausa":"Rana",
       "Korean":"Taeyang",
       "Japanese":"Taiyo",},
"Moon":{"Spanish":"Luna",
            "French":"Lune",
            "Hausa":"Wata",
            "Korean":"Dal",
            "Japanese":"tsuki",
            },
    "Love":{"Spanish":"Amor",
            "French":"Amour",
            "Hausa":"Soyayya",
            "Korean":"Sarang",
            "Japanese":"Ai",
            },
    "Family":{"Spanish":"Familia",
              "French":"Famille",
              "Hausa":"Iyali",
              "Korean":"Gajok",
              "Japanese":"Kazoku",
              },
    "Friend":{"Spanish":"Amigo",
              "French":"Ami",
              "Hausa":"Aboki",
              "Korean":"Chingu",
              "Japanese":"Tomodachi",
              },
    "Big":{"Spanish":"Grande",
           "French":"Grand",
           "Hausa":"Babba",
           "Korean":"Keun",
           "Japanese":"Okii",
           },
    "Small":{"Spanish":"Pequeno",
             "French":"Petit",
             "Hausa":"Karami",
             "Korean":"Jagi",
             "Japanese":"Chilisai",
             },
    "Good":{"Spanish":"Bueno",
            "French":"Bon",
            "Hausa":"Mai kyau",
            "Korean":"Joh-eun",
            "Japanese":"Waruii",
            },
    "Bad":{"Spanish":"Malo",
           "French":"Mauvais",
           "Hausa":"Mara kyau",
           "Korean":"Nappeun",
           "Japanese":"Warui",
           },
    "Beautiful":{"Spanish":"Hermosa",
                 "French":"Beau",
                 "Hausa":"Mai kyau",
                 "Korean":"Areumdaun",
                 },
    "House":{"Spanish":"Casa",
             "French":"Maison",
             "Hausa":"Gida",
             "Korean":"Jip",
             "Japanese":"Ie", }
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

