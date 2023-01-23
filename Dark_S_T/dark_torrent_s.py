from tkinter import *
from tkinter.messagebox import *
import os, sys



def ctr_screen(z,ww,hh):
        global w,h 
        w,h = z.winfo_screenwidth(),z.winfo_screenheight()
        z.geometry("{}x{}+{}+{}".format(ww, hh, int((w/2) - (ww/1.9)), int((h/2.2) - (hh/2))))





def dark_splash():
    app = Tk()
    app.title("")
    app.overrideredirect(True)
    app.geometry("435x186")
    ctr_screen(app,435,186)
    app.config(background="#000")
    l = PhotoImage(file='./imgs/{0}'.format("dark.png"))
    z = Label(app, image=l, background="#fff", border=0, borderwidth=0)
    z.pack()
    z.after(3000,app.destroy)
    app.mainloop()


def not_compt():
    app = Tk()
    app.title("")
    app.overrideredirect(True)
    app.geometry("435x186")
    ctr_screen(app,435,186)
    app.config(background="#000")
    l = PhotoImage(file='./imgs/{0}'.format("nts.png"))
    z = Label(app, image=l, background="#fff", border=0, borderwidth=0)
    z.pack()
    z.after(6000,app.destroy)
    app.mainloop()

def show_box():

    enter_darks = Tk()
    enter_darks.title("List of all torrents - DarkTorrentSearcher")
    enter_darks.geometry("720x400")

    enter_darks.resizable(0,0)

    
    ert = Scrollbar(enter_darks, orient='vertical')
    ert.pack(side=RIGHT, fill='y')

    txt= Text(enter_darks, font=("Arial, 12"), background="#fff",foreground="#000", yscrollcommand=ert.set)

    with open("tt.txt","r", encoding="utf-8") as m:
        try:
                serialcounter = 0
                for y in m.read().split("\n"):
                    serialcounter += 1
                    (a,b,c,d) = y.split(",")
                    txt.insert(END, "  {:<3} {:<10}\n     seeds: {:^10} leeches: {:^10}\n     {:^10} \n\n".format(serialcounter,a,b,c,d))
        except:
            pass

    ert.config(command=txt.yview)
    txt.config(state='disabled')
    txt.pack()

    def clears():
        
        if askokcancel(title="Quit", message="are you sure want to cancel ?"):
            os.remove("tt.txt")
            enter_darks.destroy()

    enter_darks.protocol("WM_DELETE_WINDOW", clears)

    enter_darks.mainloop()


def enters(kk):
    enter_dark = Tk()
    enter_dark.title("Search - DarkTorrentSearcher")
    enter_dark.geometry("410x140")
    ctr_screen(enter_dark, 420, 140)
    l = PhotoImage(file='./imgs/{0}'.format("enter.png"))
    z = Label(enter_dark, image=l, background="#fff", border=0, borderwidth=0)
    z.pack()

    j = Entry(enter_dark, background="yellow", foreground="#000", border=1, width=30, font=("Arial, 18"), highlightcolor="yellow")
    j.pack()
    j.place(relx=0.03241,rely=0.2, height=50)



    def searcher(e):
        while j.get() != "bye":  
            p = kk(j.get())
            p.all_gets(j.get())

            j.after(1000, enter_dark.destroy)
            show_box()
            break
            


    enter_dark.bind('<Return>',searcher)
    j.delete(0,END)

    enter_dark.mainloop()