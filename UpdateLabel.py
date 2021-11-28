import tkinter as tk
  
# toplevel window
ctr=0
# Method to make Button(Widget) invisible from toplevel


class UpdateLabel():
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Ausgangsposition")
        self.win.minsize(800, 600)
        self.ctr = "david est pas la"
        self.i=0
        self.tk_var = tk.StringVar()
        self.tk_var.set("0")
        lab=tk.Label(self.win, textvariable=self.tk_var,
                       bg='#40E0D0', fg='#FF0000')
        lab.place(x=20, y=30)
        self.updater()
        self.win.mainloop()

    def updater(self):
        self.i+=1
        self.tk_var.set(str(self.ctr))
        if (self.i > 5):
            self.ctr = "david est la"
            self.win.after(9000, self.updater)
        else:
            self.ctr = "david est la"
            self.win.after(9000, self.updater)


     
Ul = UpdateLabel()