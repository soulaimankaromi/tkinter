from tkinter import *
from tkinter import ttk
import sqlite3


window = Tk()
myfar= IntVar()
res=StringVar
window.title("bank")
window.geometry("1000x1000")
l1=Label (window, text='Numéro:')
l1.place(x=0,y=20)
l2=Label (window, text='Propriétaire:')
l2.place(x=0,y=50)
v2=Entry(window).place (x=90,y=50)
l3=Label (window, text='solde Initial :')
l3.place(x=0,y=80)
v3=Entry(window). place (x=90,y=80)
l5=Label(window, text="Euro")
l5.place(x=220,y=80)
l4=Label(window,text="Type:")
l4.place(x=0,y=110)
Radiobutton(window, text="Courant", variable=myfar, value=1).place(x=80,y=110)
Radiobutton(window, text="Epargne", variable=myfar, value=2).place(x=220,y=110)
l6=Label(window, text="Taux Interet:").place(x=0,y=140)
v4=Entry(window).place(x=90,y=140)
l7=Label(window, text="%").place(x=220,y=140)
l8=Label(window, text="M.Découvert:").place(x=0,y=170)
v5=Entry(window).place(x=90,y=170)


b1=Button(window,text='Creation Compte', width=15). place (x=90,y=220)


table=ttk.Treeview(window, columns=("#","Numero","Proprietaire","Solde initiale","Type","Taux interet","Montant Decouvert"),show="headings",height=15)
table.heading("#",text="#")
table.heading("Numero",text="Numero")
table.heading("Proprietaire",text="Proprietaire")
table.heading("Solde initiale",text="Solde initiale")
table.heading("Type",text="Type")
table.heading("Taux interet",text="Taux interet")
table.heading("Montant Decouvert",text="Montant Decouvert")
table.pack()
table.place(x=300,y=300)
table.column(0,width=150)
table.column(1,width=100)
table.column(2,width=120)
table.column(3,width=130)
table.column(4,width=140)
table.column(5,width=150)
table.column(6,width=160)


window.mainloop()