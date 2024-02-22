
from tkinter import *
from tkinter.filedialog import *
import tkinter as tk


def  saveFile():
    #asksaveasfile fonksiyonu kullanıcının bir dosya seçmesini ve dosya türünü belirlemesini sağlar.
    new_file=asksaveasfile(mode="w",filetype=[("text files",".txt")])
    
    #Kullanıcı bir dosya seçmez veya işlem iptal ederse
    if new_file is None:
        return
    text=str(entry.get(1.0,END))
    #Seçilen dosyaya metin yazılır
    new_file.write(text)
    #dosya kapatılmalıdır
    new_file.close()
    
def openFile():
    #askopenfile ile kullanıcıya bir dosya açma penceresi açılır
    file=askopenfile(mode="r",filetype=[("text files","*.txt")])
    if file is not None:
        content=file.read()
    #dosya içeriğini "Text " widget'inin içine ekler
    entry.insert(INSERT,content)

def clearFile():
    entry.delete(1.0,END)

def exit():
    canvas.destroy()

#Tkinter'da penceri oluşturan bir "Tk" nesnesi oluşturur
canvas=tk.Tk()

canvas.geometry("400x600")
canvas.title("Not defteri")
canvas.config(bg="white")
top=Frame(canvas)

#pack Tkinter'da bir winget'in pencereüzerinde nasıl yerleştirileceğini belirlemek için kullanırlır
top.pack(padx=10,pady=5,anchor="nw")
b1=Button(canvas,text="Aç",bg="white",command=openFile)
b1.pack(in_=top,side=LEFT)

b2=Button(canvas,text="Kaydet",bg="white",command=saveFile)
b2.pack(in_=top,side=LEFT)

b3=Button(canvas,text="Yeni",bg="white",command=clearFile)
b3.pack(in_=top,side=LEFT)

b4=Button(canvas,text="Çıkış",bg="white",command=exit)
b4.pack(in_=top,side=LEFT)

#Text widget'i oluşturuldu
entry=Text(canvas,wrap=WORD,bg='lightgreen',font=("poppins",15))
entry.pack(padx=10,pady=5,expand=TRUE,fill=BOTH)

canvas.mainloop()
