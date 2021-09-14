from tkinter import *
from tkinter.colorchooser import askcolor


b1 = "up"
xold, yold = None, None

def main():
    global coord_list
    global canvas
    global active_button
    tk = Tk()
    canvas = Canvas(tk, bg='white', width=600, height=600)
    canvas.grid(row=1, columnspan=5)
    reset_button = Button(tk, text='reset', command=reset())
    reset_button.grid(row=0, column=3)
    # canvas.pack()
    canvas.bind("<Motion>", draw)
    canvas.bind("<ButtonPress-1>", mouse_down)
    canvas.bind("<ButtonRelease-1>", mouse_up)
    active_button = reset_button
    coord_list = []
    tk.mainloop()

def mouse_down(event):
    global down
    down = True

def mouse_up(event):
    global down, x_old, y_old
    down = False
    x_old = None
    y_old = None

def reset():
    canvas.delete(ALL)
    canvas.create_rectangle(0, 0, 600, 600)
    print("clear")
    coord_list = []

def reset_button(button):
        active_button.config(relief=RAISED)
        button.config(relief=SUNKEN)
        active_button = button

def draw(event):
    if down:
        global x_old, y_old
        if x_old is not None and y_old is not None:
            line = canvas.create_line(x_old, y_old, event.x, event.y, smooth=TRUE)
                          # here's where you draw it. smooth. neat.
        x_old = event.x
        y_old = event.y
        coord_list.append((x_old, y_old))
        print(coord_list)
    

main()