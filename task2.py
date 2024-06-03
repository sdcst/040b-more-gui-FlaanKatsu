import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("ポケモンだよ！")
window.geometry("630x600")
window.resizable(False,False)
window.iconphoto(False,PhotoImage(file='img/pokeball.png'))


viewport = PhotoImage(file="main.png")
minimap = PhotoImage(file="minimap.png")
logo = PhotoImage(file="img/logo.png")
conpass = PhotoImage(file="img/compass.png")

pka = tk.Label(window,text="POKEMON ADVENTURE")
mnmp = tk.Label(window,text="MINIMAP")
mp = tk.Button(window,text="MAP",width=10)
inv = tk.Button(window,text="INVENTORY",width=10)
pd = tk.Button(window,text="POKEDEX",width=10)
rs = tk.Button(window,text="ROSTER",width=10)
jn = tk.Button(window,text="JOURNAL",width=10)
hlp = tk.Button(window,text="HELP",width=10)
shp = tk.Button(window,text="SHOP",width=10)

viewport1 = tk.Label(window,image=viewport)
minimap1 = tk.Label(window,image=minimap)
logo1 = tk.Label(window,image=logo)
conpass1 = tk.Label(window,image=conpass)

pka.place(x="250",y="5")
viewport1.place(x="5",y="30")
mnmp.place(x="535",y="50")
minimap1.place(x="510",y="75")
mp.place(x="512",y="170")
inv.place(x="512",y="201")
pd.place(x="512",y="232")
rs.place(x="512",y="263")
jn.place(x="512",y="294")
hlp.place(x="512",y="325")
shp.place(x="512",y="356")
logo1.place(x="250",y="500")
conpass1.place(x="5",y="475")

window.mainloop()
