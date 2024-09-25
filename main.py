import pypokedex
import PIL.Image
import PIL.ImageTk
import tkinter as tk
import urllib3
from io import BytesIO
from pynput.keyboard import Key, Listener

dexwindow = tk.Tk()
dexwindow.geometry("500x800")
dexwindow.title("Jackiedex")
dexwindow.config(padx=10, pady=10)

title_label = tk.Label(dexwindow, text="Jackiedex")
title_label.config(font=("Times New Roman", 32))
title_label.pack(padx=10, pady=10)

pokemon_image = tk.Label(dexwindow)
pokemon_image.pack(padx=10, pady=10)

pokemon_information = tk.Label(dexwindow)
pokemon_information.config(font=("Times New Roman", 20))
pokemon_information.pack(padx=10, pady=10)

pokemon_types = tk.Label(dexwindow)
pokemon_types.config(font=("Times New Roman", 20))
pokemon_types.pack(padx=10, pady=10)

pokemon_abilities = tk.Label(dexwindow)
pokemon_abilities.config(font=("Times New Roman", 20))
pokemon_abilities.pack(padx=10, pady=10)

pokemon_stats = tk.Label(dexwindow)
pokemon_stats.config(font=("Times New Roman", 20))
pokemon_stats.pack(padx=10, pady=10)


def load_pokemon():
    pokemon = pypokedex.get(name=text_id_name.get(1.0, "end-1c"))
    http = urllib3.PoolManager()
    response = http.request('GET', pokemon.sprites.front.get('default'))
    image = PIL.Image.open(BytesIO(response.data))
    img = PIL.ImageTk.PhotoImage(image)
    pokemon_image.config(image=img)
    pokemon_image.image = img

    pokemon_information.config(text=f"{pokemon.dex} - {pokemon.name}".title())
    pokemon_types.config(text=" - ".join(t for t in pokemon.types).title())
    pokemon_abilities.config(text=f"Abilities - {pokemon.abilities}")
    pokemon_stats.config(text=f"Base Stats - {pokemon.base_stats}")


label_id_name = tk.Label(dexwindow, text="ID or Name")
label_id_name.config(font=("Times New Roman", 20))
label_id_name.pack(padx=10, pady=10)

text_id_name = tk.Text(dexwindow, height=1)
text_id_name.config(font=("Times New Roman", 20))
text_id_name.pack(padx=10, pady=10)

btn = tk.Button(dexwindow, text="Search", command=load_pokemon)
btn.config(font=("Times New Roman", 20))
btn.pack(padx=10, pady=10)

dexwindow.mainloop()
