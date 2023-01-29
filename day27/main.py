import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# label
my_label = tkinter.Label(text="I Am a label", font=("Arial", 15, "bold"))
my_label.pack(side="left")


window.mainloop()
