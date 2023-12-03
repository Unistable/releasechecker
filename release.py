from bs4 import BeautifulSoup
import requests
import tkinter as tk
from tkinter import ttk
import sys

urls = {
    "OLD": "https://www.unknowncheats.me/forum/tags/release.html",
    "APEX": "https://www.unknowncheats.me/forum/apex-legends/",
    "EFT": "https://www.unknowncheats.me/forum/escape-from-tarkov/",
    "GTA5": "https://www.unknowncheats.me/forum/grand-theft-auto-v/",
    "OVERWATCH": "https://www.unknowncheats.me/forum/overwatch/",
    "PALADINS": "https://www.unknowncheats.me/forum/paladins/",
    "PUBG": "https://www.unknowncheats.me/forum/pubg-releases/",
    "RUST": "https://www.unknowncheats.me/forum/rust/",
    "SOT": "https://www.unknowncheats.me/forum/sea-of-thieves/",
    "TF2": "https://www.unknowncheats.me/forum/team-fortress-2-a/",
    "VALORANT": "https://www.unknowncheats.me/forum/valorant/",
    "BATTLEBIT": "https://www.unknowncheats.me/forum/battlebit-remastered/",
    "GMOD": "https://www.unknowncheats.me/forum/garry-s-mod/",
    "COD": {
        "COD1": "https://www.unknowncheats.me/forum/call-of-duty-1-a/",
        "COD2": "https://www.unknowncheats.me/forum/call-of-duty-2-a/",
        "COD4MW": "https://www.unknowncheats.me/forum/call-of-duty-4-modern-warfare/",
        "COD5WaW": "https://www.unknowncheats.me/forum/call-of-duty-5-world-at-war/",
        "COD6MW2": "https://www.unknowncheats.me/forum/call-of-duty-6-modern-warfare-2-a/",
        "CODBO": "https://www.unknowncheats.me/forum/call-of-duty-black-ops/",
        "CODMW3": "https://www.unknowncheats.me/forum/call-of-duty-modern-warfare-3-a/",
        "CODBO2": "https://www.unknowncheats.me/forum/call-of-duty-black-ops-2-a/",
        "CODBO3": "https://www.unknowncheats.me/forum/call-of-duty-black-ops-3-a/",
        "CODGHOST": "https://www.unknowncheats.me/forum/call-of-duty-ghosts/",
        "CODAW": "https://www.unknowncheats.me/forum/call-of-duty-advanced-warfare/",
        "CODBO4": "https://www.unknowncheats.me/forum/call-of-duty-black-ops-4-a/",
        "COD:MW": "https://www.unknowncheats.me/forum/call-of-duty-modern-warfare/",
        "CODCW": "https://www.unknowncheats.me/forum/call-of-duty-black-ops-cold-war/",
        "CODVANG": "https://www.unknowncheats.me/forum/call-of-duty-vanguard/",
        "COD:MW2": "https://www.unknowncheats.me/forum/call-of-duty-modern-warfare-ii/",
        "COD:MW3": "https://www.unknowncheats.me/forum/call-of-duty-modern-warfare-iii/"
    },
    "CSTRIKE": {
        "CSS": "https://www.unknowncheats.me/forum/counterstrike-source/",
        "CS2": "https://www.unknowncheats.me/forum/counter-strike-2-releases/",
        "CS16": "https://www.unknowncheats.me/forum/counterstrike-1-5-1-6-and-mods/"
    },
    "PAYDAYS": {
        "PAYDAY2": "https://www.unknowncheats.me/forum/payday-2-a/",
        "PAYDAY3": "https://www.unknowncheats.me/forum/payday-3-a/"
    },
    "OTHERS": {
        "OTHER1": "https://www.unknowncheats.me/forum/other-fps-games/",
        "OTHER2": "https://www.unknowncheats.me/forum/other-fps-games/index2.html",
        "OTHER3": "https://www.unknowncheats.me/forum/other-fps-games/index3.html"
    }
}

def parse_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    divs = soup.find_all('div')
    for div in divs:
        text = div.text.strip()
        if text.startswith('[Release]'):
            print(text)

def select_category():
    category = category_combobox.get()
    subcategory = subcategory_combobox.get()
    
    if subcategory:
        url = urls[category][subcategory]
    else:
        url = urls[category]
    
    console_text.delete(1.0, tk.END)
    sys.stdout = ConsoleRedirector(console_text)
    parse_url(url)

class ConsoleRedirector:
    def __init__(self, console_text_widget):
        self.console_text_widget = console_text_widget

    def write(self, text):
        self.console_text_widget.insert(tk.END, text)
        self.console_text_widget.see(tk.END)

window = tk.Tk()
window.title("UC Release finder")
window.geometry("400x300")

category_label = ttk.Label(window, text="Game Category:")
category_label.pack()
category_combobox = ttk.Combobox(window, values=list(urls.keys()))
category_combobox.pack()

subcategory_label = ttk.Label(window, text="Subcategory:")
subcategory_label.pack()
subcategory_combobox = ttk.Combobox(window, values=[])
subcategory_combobox.pack()

def update_subcategories(event):
    selected_category = category_combobox.get()
    if selected_category in urls and isinstance(urls[selected_category], dict):
        subcategories = list(urls[selected_category].keys())
        subcategory_combobox.config(values=subcategories)
    else:
        subcategory_combobox.config(values=[])

category_combobox.bind("<<ComboboxSelected>>", update_subcategories)

console_text = tk.Text(window, height=10)
console_text.pack()

select_button = ttk.Button(window, text="Find", command=select_category)
select_button.pack()

window.mainloop()