from tkinter import Tk,Entry,Button,Label,StringVar

#creating a window

window = Tk()

#width and length of window.
window.geometry("600x400")

window.title("Spanish_dictionary")



entry_text =Entry(window)

entry_text.pack()


result = StringVar()
result_label=Label(window,textvariable=result)
result_label.pack()


Spanish_dictionary =  { "hola" : "hello",
                       "adios" : "goodbye",
                       "gracias" : "thankyou",
                       "lo siento": "excuse me/sorry",
                       "como estas?" : "how are you",
                       "estoy bien" : "i am fine",
                       "agua": "water",
                       "comida" : "food",
                       "casa" : "house",
                       "coche" : "car",
                       "amigo" : "friend",
                       "familia" : "family",
                       "amor": "love",
                       "feliz": "happy",
                       "triste":"sad",
                       "verdad":"true",
                       "falso":"false",
                       "si":"yes",
                       "no":"no"}

def search(word):
    if word in Spanish_dictionary:
        result.set(Spanish_dictionary[word])
        print(Spanish_dictionary[word])


    else:
        result.set("Not found")
        print("Not found")

search_btn =Button(window,text = "search", command=lambda:search(entry_text.get()))
search_btn.pack()
window.mainloop()

