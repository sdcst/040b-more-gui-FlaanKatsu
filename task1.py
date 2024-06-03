import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("Fake Calculator Dayo!")
window.resizable(False,False)

Pt = tk.Label(window,text="Principal")
IRt = tk.Label(window,text="Interest Rate")
Yt = tk.Label(window,text="Years")
At = tk.Label(window,text="Amount")
dt = tk.Label(window,text="-")

Pb = tk.Entry(window,width="12")
IRb = tk.Entry(window,width="12")
Ab = tk.Entry(window,width="12")
Yb = ttk.Combobox(window,width="12",values=["2024-2025","2024-2026","2024-2027","2024-2028","2024-2029"])

Pt.grid(row=1,column=1)
IRt.grid(row=1,column=2)
Yt.grid(row=1,column=3)
At.grid(row=4,column=1,sticky="e")
dt.grid(row=3,column=1)

Pb.grid(row=2,column=1)
IRb.grid(row=2,column=2)
Ab.grid(row=4,column=2)
Yb.grid(row=2,column=3)

window.mainloop()