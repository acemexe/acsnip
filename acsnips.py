import tkinter as tk
from tkinter import filedialog, Text, DISABLED, NORMAL, ttk, font, RIGHT, messagebox, Y
from tkinter.filedialog import *
import webbrowser
import time
import random
import pygame
import json
import subprocess
import os

subprocess.call("TASKKILL /F /IM acsnip.exe", shell=True)

try:
    os.startfile("acsnip.exe")
except:
    print("Yeniden başlatma başarısız.")

pygame.mixer.init()
baslangic = pygame.mixer.Sound("baslangic.mp3")
click = pygame.mixer.Sound("click.mp3")
wow = pygame.mixer.Sound("wow.mp3")
tik = pygame.mixer.Sound("tik.mp3")
sss = pygame.mixer.Sound("ss.mp3")

arkaplan = "#000000"
koyugri = "#1c1c1c"
acikgri = "#313542"
acikgri2 = "#23272a"
acikmavi = "#2082b2"
acikyesil = "#008000"
koyugri2 = "#1d1f21"
acarka = "#191414"
yazirengi = "#ffffff"
baslikyazirengi = "#ffffff"
altyazi = "By Acem8887"
kirmizi = "#FF0000"
turuncu = "#FFA500"
kenargenisligi = 0
cubukrengi = acikmavi
cubukrengi2 = acikyesil
kirmiziyazi = kirmizi
aramarengi = koyugri

version = "0.2"
pygame.mixer.Sound.play(baslangic)
root = tk.Tk()
root.title(f"AcSnip")
root.resizable(False, False)
root.iconbitmap("ikon.ico")
yer = str(root.winfo_screenwidth()/2 - 500/2).split(".")[0]
yer1 = str(root.winfo_screenheight()/2 - 400/2).split(".")[0]
root.geometry(f"500x400+{yer}+{yer1}")
baslikutu = tk.Frame(root, bg=acikmavi)
baslikutu.place(relwidth=1, relheight=0.2)
baslikutu1 = tk.Frame(root, bg=arkaplan)
baslikutu1.place(relwidth=1, relheight=0.8, rely=0.2)

baslik = tk.Label(baslikutu, text=f"AcSnip", bg=acikmavi, fg=baslikyazirengi)
baslik.config(font=("Montserrat ExtraBold", "30", "bold italic"))
baslik.place(relwidth=1, relheight=0.9)
upd = tk.Label(baslikutu1, text=altyazi, bg=arkaplan, fg=yazirengi)
upd.config(font=("Arial", "7"))
upd.place(relwidth=0.13, relheight=0.05, rely=0.95)
altlik = tk.Label(baslikutu1, text=f"           Versiyon : {version}", bg=arkaplan, fg=yazirengi)
altlik.config(font=("Arial", "7"))
altlik.place(relwidth=0.2, relheight=0.05, rely=0.95, relx=0.8)

def ayarlar():
    pygame.mixer.Sound.play(click)
    print("ayarlar basıldı")
    ayarlar.destroy()
    hakkinda.destroy()
    baslik.config(text="Ayarlar")

    def sfxf():
        pygame.mixer.Sound.play(click)
        with open('data.json', 'r') as f:
            clc = json.load(f)
        clc[str(f"sfx")] = sfxv.get()
        with open('data.json', 'w') as f:
            json.dump(clc, f, indent=4)

    def otof():
        pygame.mixer.Sound.play(click)
        if otov.get() == 1:
            save_yol = asksaveasfilename(title="Kayıt Yolu Seçiniz.", initialfile=f"AcSnip", defaultextension=".png", filetypes=(("PNG Dosyası","*.png"),("JPEG Dosyası","*.jpg"),("GIF Dosyası","*.gif"),("Tüm Dosyalar","*.*")))
            if save_yol != "":
                with open('data.json', 'r') as f:
                    clc = json.load(f)
                clc[str(f"oto_save")] = save_yol
                with open('data.json', 'w') as f:
                    json.dump(clc, f, indent=4)
            else:
                oto.deselect()
        else:
            with open('data.json', 'r') as f:
                key = json.load(f)

            key.pop("oto_save")

            with open('data.json', 'w') as f:
                json.dump(key, f, indent=4)

    sfxv = tk.IntVar()
    sfx = tk.Checkbutton(baslikutu1, text="Ses Efektleri", pady=15, padx=15, bg=acikmavi, variable=sfxv, command=sfxf)
    sfx.pack(pady=60)

    otov = tk.IntVar()
    oto = tk.Checkbutton(baslikutu1, text="Oto Kaydetme", pady=15, padx=10, bg=acikmavi, variable=otov, command=otof)
    oto.pack()
    def get_key(key=None):
        with open('data.json', 'r') as f:
            yol = json.load(f)
        if key in yol:
            return yol[key]
        else:
            return 0

    if get_key(key="sfx") != 0:
        sfx.select()

    if get_key(key="oto_save") != 0:
        oto.select()

ayarlar = tk.Button(baslikutu1, text="Ayarlar", padx=30, pady=20, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, command=ayarlar)
ayarlar.pack(pady=65)

def hakkinda():
    pygame.mixer.Sound.play(click)

hakkinda = tk.Button(baslikutu1, text="hakkinda", padx=20, pady=20, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, command=hakkinda)
hakkinda.pack(pady=0)

root.mainloop()