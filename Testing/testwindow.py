from tkinter import *

app = Tk()
app.eval('tk::PlaceWindow %s right' % app.winfo_pathname(app.winfo_id()))
app.mainloop()
