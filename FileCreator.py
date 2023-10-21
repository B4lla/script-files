import os
import sys
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from time import sleep
from tkinter import PhotoImage, Button, Tk
from tkinter import ttk

base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))


def html():
    config_content = """
    """

    server_content = """
    """

    client_content = """
    """

    fxmanifest_content = """
    fx_version 'cerulean'
    game 'gta5'
    author '.balla'
    description 'https://discord.com/invite/hJg5c2Dw5y'
    version '1.0'

    shared_scripts {
        'config.lua',
    }

    client_scripts {
        'client.lua',
    }

    server_scripts {
        'server.lua',
    }
    """

    index_html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Pressure Shop</title>
        <link rel="stylesheet" type="text/css" href="style.css">
    </head>
    <body>

        <script src="script.js"></script>
    </body>
    </html>
    """

    pathfolder_info = pathfolder.get()
    name_info = name.get()

    if os.path.exists(pathfolder_info):
        folder_path = os.path.join(pathfolder_info, name_info)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Carpeta '{name_info}' creada en '{pathfolder_info}'.")

            subfolder_name = "html"
            subfolder_path = os.path.join(folder_path, subfolder_name)
            os.makedirs(subfolder_path)

            subfolder_file_names = ["index.html", "style.css", "script.js"]

            for subfolder_file_name in subfolder_file_names:
                subfolder_file_path = os.path.join(
                    subfolder_path, subfolder_file_name)

                if subfolder_file_name == "index.html":
                    with open(subfolder_file_path, "w") as subfolder_file:
                        subfolder_file.write(index_html_content)
                else:
                    with open(subfolder_file_path, "w") as subfolder_file:
                        subfolder_file.write("/* Developed by B4lla */")

            # Código para crear los archivos en la carpeta raíz
            file_contents = {
                "server.lua": server_content,
                "client.lua": client_content,
                "config.lua": config_content,
                "fxmanifest.lua": fxmanifest_content
            }

            for file_name, content in file_contents.items():
                file_path = os.path.join(folder_path, file_name)
                with open(file_path, "w") as file:
                    file.write(content)

            assets_subfolder_path = os.path.join(subfolder_path, "assets")
            os.makedirs(assets_subfolder_path)

            print(
                f"Se han creado los archivos y subcarpetas dentro de '{name_info}'.")
        else:
            print(
                f"La carpeta '{name_info}' ya existe en '{pathfolder_info}'.")
    else:
        print(f"La ruta '{pathfolder_info}' no es válida.")


def tail():
    config_content = """
-- Developed by B4lla
    """

    server_content = """
-- Developed by B4lla
    """

    client_content = """
-- Developed by B4lla
    """

    fxmanifest_content = """
    fx_version 'cerulean'
    game 'gta5'
    author '.balla'
    description 'https://discord.com/invite/hJg5c2Dw5y'
    version '1.0'

    shared_scripts {
        'config.lua',
    }

    client_scripts {
        'client.lua',
    }

    server_scripts {
        'server.lua',
    }
    """

    index_html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Pressure Shop</title>
        <link href="https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css" rel="stylesheet">
        <link rel="stylesheet" type="text/css" href="style.css">
    </head>
    <body>

        <script src="script.js"></script>
    </body>
    </html>
    """

    pathfolder_info = pathfolder.get()
    name_info = name.get()

    if os.path.exists(pathfolder_info):
        folder_path = os.path.join(pathfolder_info, name_info)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Carpeta '{name_info}' creada en '{pathfolder_info}'.")

            subfolder_name = "html"
            subfolder_path = os.path.join(folder_path, subfolder_name)
            os.makedirs(subfolder_path)

            subfolder_file_names = ["index.html", "style.css", "script.js"]

            for subfolder_file_name in subfolder_file_names:
                subfolder_file_path = os.path.join(
                    subfolder_path, subfolder_file_name)

                if subfolder_file_name == "index.html":
                    with open(subfolder_file_path, "w") as subfolder_file:
                        subfolder_file.write(index_html_content)
                else:
                    with open(subfolder_file_path, "w") as subfolder_file:
                        subfolder_file.write("/* Developed by B4lla */")

            # Código para crear los archivos en la carpeta raíz
            file_contents = {
                "server.lua": server_content,
                "client.lua": client_content,
                "config.lua": config_content,
                "fxmanifest.lua": fxmanifest_content
            }

            for file_name, content in file_contents.items():
                file_path = os.path.join(folder_path, file_name)
                with open(file_path, "w") as file:
                    file.write(content)

            assets_subfolder_path = os.path.join(subfolder_path, "assets")
            os.makedirs(assets_subfolder_path)

            print(
                f"Se han creado los archivos y subcarpetas dentro de '{name_info}'.")
        else:
            print(
                f"La carpeta '{name_info}' ya existe en '{pathfolder_info}'.")
    else:
        print(f"La ruta '{pathfolder_info}' no es válida.")


def create_entry_with_style(parent, textvar, width, style_name):
    entry = tk.Entry(parent, textvariable=textvar,
                     width=width, font=("Arial", 12, "bold"))
    entry.configure(style_name)
    return entry


def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        pathfolder.set(folder_path)


window = Tk()
window.geometry("1000x600")
window.resizable(False, False)
window.title("B4lla Creation Files")
#window.iconbitmap("logo.ico")

style = ttk.Style()

style.configure("TEntry",
                fieldbackground="gray60",
                borderwidth=5,
                padding=(10, 5),
                relief="flat",
                font=("Arial", 12, "bold"))

style.configure("TButton", font=("Arial", 12, "bold"))

style.configure("TButton", background="lightblue", foreground="black")

image_path = os.path.join(base_path, "images", "background2.png")
imagebackground = PhotoImage(file=image_path)
label1 = Label(window, image=imagebackground)
label1.pack()


class CustomEntry(Entry):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(
            bg="black",
            fg="white",
            bd=0,
            highlightthickness=0,
            insertbackground="white",
            selectbackground="white",
            selectforeground="black",
            highlightbackground="white",
            highlightcolor="white",
            relief="flat",
        )
        self.config(font=("Arial", 14), justify=CENTER)


name_text = Label(text="Script Name:", font=(
    "Arial", 14, "bold"), bg="black", fg="white")
pathfolder_text = Label(text="Put The Path Folder Here:", font=(
    "Arial", 14, "bold"), bg="black", fg="white")
select_folder_button = Button(window, text="Select Folder", command=browse_folder, font=(
    "Arial", 14, "bold"), bg="black", fg="white", bd="0")
select_folder_button.place(x=385, y=95)


name_text.place(x=15, y=20)
pathfolder_text.place(x=15, y=80)


name = StringVar()
pathfolder = StringVar()


first_name_entry = CustomEntry(window, textvariable=name, width=30)
pathfolder_entry = CustomEntry(window, textvariable=pathfolder, width=30)


first_name_entry.place(x=15, y=50)
pathfolder_entry.place(x=15, y=110)


photo_path = os.path.join(base_path, "images", "html.png")
photo = PhotoImage(file=photo_path)
photoimage = photo.subsample(5, 5)

photo1_path = os.path.join(base_path, "images", "tailwind.png")
photo1 = PhotoImage(file=photo1_path)
photoimage1 = photo1.subsample(5, 5)

bttn = Button(window, text=' TailWind ', command=tail, image=photoimage1, compound=LEFT,
              font=("Arial", 12, "bold"), bg="blue", fg="white", bd="0")
bttn.place(x=175, y=200)

bttn2 = Button(window, text='    HTML         ', command=html, image=photoimage, compound=LEFT,
               font=("Arial", 12, "bold"), bg="green", fg="white", bd="0")
bttn2.place(x=15, y=200)



mainloop()
