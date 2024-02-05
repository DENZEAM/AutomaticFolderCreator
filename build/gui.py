

from pathlib import Path
import AutomaticFolderCreator

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage , filedialog , messagebox
import json
import os
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\eljai\Documents\GitHub\AutomaticFolderCreator\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


filePath = None
Config = None

def import_json():
    global Config
    filepath = filedialog.askopenfilename(filetypes=[("Fichiers JSON", "*.json")])
    if filepath:
        with open(filepath, 'r') as file:
            data = json.load(file)
            Config = filepath
            print(Config)
            messagebox.showinfo("Config sélectionnée", f"Config sélectionnée : {filepath}")
        return data
    else:
        return None

def select_path():
    global filePath
    filepath = filedialog.askdirectory()
    if filepath:
        messagebox.showinfo("Chemin sélectionné", f"Chemin sélectionné : {filepath}")
        filePath = filepath
        return filepath
    else:
        return None

def Create():
    print("Okkk")
    if Config and filePath:
        AutomaticFolderCreator.create_structure(Config, filePath)
    else:
        messagebox.showerror("Erreur", "Veuillez sélectionner une configuration et un chemin.")
window = Tk()

window.geometry("745x504")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 504,
    width = 745,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    79.0,
    745.0,
    504.0,
    fill="#8E91B0",
    outline="")

canvas.create_rectangle(
    0.0,
    0.0,
    745.0,
    80.0,
    fill="#444A80",
    outline="")

canvas.create_text(
    17.0,
    31.0,
    anchor="nw",
    text="AUTOMATIC FOLDER CREATOR",
    fill="#FFFFFF",
    font=("Inter", 20 * -1),
    justify="center"
)

canvas.create_text(
    647.0,
    33.0,
    anchor="nw",
    text="V.0.0.1",
    fill="#FFFFFF",
    font=("Inter", 13 * -1)
)

canvas.create_rectangle(
    21.0,
    96.0,
    229.0,
    420.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    47.0,
    120.0,
    anchor="nw",
    text="Selectioner votre configuration ",
    fill="#000000",
    font=("Inter", 12 * -1),
    justify="center",
    width=250.0,
  
)

canvas.create_text(
    55.0,
    324.0,
    anchor="nw",
    text="Importé une configuration",
    fill="#000000",
    font=("Inter", 12 * -1),
    justify="center",
    width=250.0
    
)

canvas.create_text(
    55.0,
    218.0,
    anchor="nw",
    text="Selectioner votre chemin",
    fill="#000000",
    font=("Inter", 12 * -1),
    justify="center",
    width=250.0,
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=2,
    highlightthickness=0,
    command=lambda: import_json(),
    relief="flat"
)
button_1.place(
    x=50.0,
    y=152.0,
    width=150.0,
    height=31.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=2,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=50.0,
    y=356.0,
    width=150.0,
    height=31.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=2,
    highlightthickness=0,
    command=lambda: select_path(),
    relief="flat"
)
button_3.place(
    x=50.0,
    y=250.0,
    width=150.0,
    height=31.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=3,
    highlightthickness=0,
    command=lambda: Create(),
    relief="flat"
)
button_4.place(
    x=29.0,
    y=430.0,
    width=180.0,
    height=46.0
)

canvas.create_rectangle(
    528.0,
    121.0,
    738.0,
    463.0,
    fill="#000000",
    outline="")

canvas.create_text(
    532.0,
    131.0,
    anchor="nw",
    text="[AFC] Chargment du systeme en cours",
    fill="#FFFFFF",
    font=("Inter", 11 * -1)
)

canvas.create_text(
    532.0,
    157.0,
    anchor="nw",
    text="[AFC] Systeme Chargé !",
    fill="#FFFFFF",
    font=("Inter", 11 * -1)
)
window.resizable(False, False)
window.mainloop()




