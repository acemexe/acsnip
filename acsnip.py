import pyautogui
import tkinter as tk
from tkinter import filedialog, Text, DISABLED, NORMAL, ttk, font, RIGHT, messagebox, Y
from tkinter.filedialog import *
import webbrowser
import pynput
from pynput.keyboard import Key, Listener
import time
import random
import pygame
import json
import threading
import subprocess
from win10toast import ToastNotifier

pygame.mixer.init()
baslangic = pygame.mixer.Sound("baslangic.mp3")
click = pygame.mixer.Sound("click.mp3")
wow = pygame.mixer.Sound("wow.mp3")
tik = pygame.mixer.Sound("tik.mp3")
sss = pygame.mixer.Sound("ss.mp3")
tost = ToastNotifier()
def get_key(key=None):
    with open('data.json', 'r') as f:
        yol = json.load(f)
    if key in yol:
        return yol[key]
    else:
        return 0

def basis(Key):
    try:
        if Key == Key.print_screen:
            pygame.mixer.Sound.play(sss)
            try:
                print("ss alınıyor")
                ss = pyautogui.screenshot()
                if get_key(key="kirpma") == 1:
                    print("kırpma arayüzü yaratılıyor...")

                    def kirpmaarayuz():
                        print("Kırpıcı Aciliyor...")
                        win = tk.Tk()

                        # Set the size of the window
                        win.geometry("700x350")

                        # Remove the Title bar of the window
                        win.overrideredirect(True)
                        win.wm_attributes('-transparentcolor', "#00ff00")

                        

                        # Add a Label widget
                        
                        kenarlar = tk.Frame(win, bg="#ffffff")
                        kenarlar2 = tk.Frame(kenarlar, bg="#00ff00")
                        label=tk.Label(kenarlar2, text="Ekran Kesintisi Almak İstediğiniz Bölgeyi Seçiniz.", fg="#000000",bg= "#ffffff")
                        label.config(font=("Montserrat Medium", "10"))
                        def pencere_hareketettir(e):

                            penc_x = win.winfo_width()
                            penc_y = win.winfo_height()

                            nokta_x = e.x

                            nokta_y = e.y

                            mouse_x = win.winfo_pointerx()
                            mouse_y = win.winfo_pointery()
                            naberx = round(penc_x/nokta_x)
                            nabery = round(penc_y/nokta_y)

                            gidilcek_x = round(mouse_x - penc_x/2)
                            gidilcek_y = round(mouse_y - penc_y/2)
                            #print(f"{penc_x}x{penc_y}+{gidilcek_x}+{gidilcek_y}")
                            win.geometry(f"+{gidilcek_x}+{gidilcek_y}")

                        
                        kenarlar.pack(side="top", fill="both", expand=True)
                        kenarlar2.pack(pady = 15, padx= 15,side="top", fill="both", expand=True)
                        label.pack(pady = 150, padx= 100, side="top", fill="both", expand=True)
                        # Add the gripper for resizing the window
                        grip=ttk.Sizegrip()
                        grip.place(relx=1.0, rely=1.0, anchor="se")
                        grip.lift(label)
                        #grip.bind("<B1-Motion>", moveMouseButton)
                        label.bind("<B1-Motion>", pencere_hareketettir)
                        win.mainloop()

                    kirpthread = threading.Thread(target=kirpmaarayuz)
                    kirpthread.start()

                if get_key(key="oto_save") == 0:
                    root = tk.Tk()
                    root.attributes("-alpha", 0)
                    root.title(f"AcSnip")
                    root.iconbitmap("ikon.ico")
                    root.wm_state('iconic')
                    root.wm_state('normal')
                    root.overrideredirect(1)
                    root.attributes("-alpha", 0.3)
                    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
                    save_yol = asksaveasfilename(title="Kayıt Yolu Seçiniz.", initialfile=f"AcSnip[{random.randint(1000, 9999)}]", defaultextension=".png", filetypes=(("PNG Dosyası","*.png"),("JPEG Dosyası","*.jpg"),("GIF Dosyası","*.gif"),("Tüm Dosyalar","*.*")))
                    root.attributes("-alpha", 0)

                    ss.save(save_yol)
                    
                    messagebox.showinfo("Başarılı!", f'Ekran Fotoğrafınız Başarıyla "{save_yol.split("/")[-1]}" Olarak Kaydedildi!')
                else:
                    save_yol = get_key(key="oto_save").split(".")[0] + f"[{random.randint(1000, 9999)}]." + get_key(key="oto_save").split(".")[-1]
                    ss.save(save_yol)
                    def dosyak():
                        redir_save = save_yol.replace("/", "\\")
                        subprocess.Popen(fr'explorer /select,"{redir_save}"')
                    try:
                        tost.show_toast("Başarılı!",f'Ekran Fotoğrafınız Başarıyla "{save_yol.split("/")[-1]}" Olarak Kaydedildi!', threaded=True, icon_path=r"./ikon.ico", callback_on_click=dosyak)
                    except:
                        print("windows 10 değil")

                randomsayi = random.randint(0, 10)
                print(randomsayi)
                if randomsayi == 0 or randomsayi == 10:
                    sayibru = random.randint(1,5)
                    print(sayibru)
                    if get_key(key="oto_save") != 0:
                        root = tk.Tk()
                        root.title(f"AcSnip")
                        root.iconbitmap("ikon.ico")
                        root.wm_state('iconic')
                        root.wm_state('normal')
                        root.attributes("-alpha", 0)
                        
                    def msjbox():
                        if sayibru == 1:
                            return ["Youtube Kanalıma Göz Atmak İster Misiniz?", "https://www.youtube.com/channel/UCh5PbyYxZUGAYm8cGRRLWYQ"]
                        elif sayibru == 2:
                            return ["Youtube Kanalıma Göz Atmak İster Misiniz?", "https://www.youtube.com/channel/UCh5PbyYxZUGAYm8cGRRLWYQ"]
                        elif sayibru == 3:
                            return ["Youtube Kanalıma Göz Atmak İster Misiniz?", "https://www.youtube.com/channel/UCh5PbyYxZUGAYm8cGRRLWYQ"]
                        elif sayibru == 4:
                            return ["AcemTube İsimli Youtube Ses/Video Ve Spotify Listesi İndirme Programıma Göz Atmak İster Misiniz?", "https://acemtube.glitch.me"]
                        elif sayibru == 5:
                            return ["AcemTube İsimli Youtube Ses/Video Ve Spotify Listesi İndirme Programıma Göz Atmak İster Misiniz?", "https://acemtube.glitch.me"]
                    pygame.mixer.Sound.play(wow)
                    evthayr = messagebox.askyesno("AcSnip", msjbox()[0])
                    pygame.mixer.Sound.play(click)
                    print(evthayr)
                    if evthayr == True:
                        webbrowser.open(msjbox()[1])
                    pygame.mixer.Sound.play(tik)
                    messagebox.showinfo("AcSnip", f'Programımı Kullandığınız İçin Teşekkür Ederim!')
                try:
                    root.destroy()
                except:
                    pass
                time.sleep(1)

            except Exception as e:
                print("Verilen yol(" + str(save_yol) + ")")
                if save_yol != "":
                    print("Bir Hata Oluştu: " + str(e))
                    messagebox.showerror("Hata!", "Bir Hata Oluştu: " + str(e))
                try:
                    root.destroy()
                except:
                    pass
    except:
        pass

with Listener(on_press=basis) as listener:
    listener.join()