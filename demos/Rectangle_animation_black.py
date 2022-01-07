from tkinter import *;
from random import choice, randint;
from time import sleep;

colors = ['black', 'white'];


def change_color():
    rectangles = [r1, r2, r3, r4, r5, r6, r7, r8, r9];
    canvas.itemconfig(choice(rectangles), fill = choice(colors), outline = '#000');

root = Tk();
root.title("Reihenfolge");
root.geometry("400x300");

canvas = Canvas(root);
root_rectangle = canvas.create_rectangle(
    160, 10, 10, 160,
    outline="#000", fill="#e8e8e8"
);

r1 = canvas.create_rectangle(
    60, 10, 10, 60, # x0 y0 x1 y1
    outline="#000", fill="#fff"   
);

r2 = canvas.create_rectangle(
    60, 10, 110, 60, # x0 y0 x1 y1
    outline="#000", fill="#fff"   
);

r3 = canvas.create_rectangle(
    110, 10, 160, 60, # x0 y0 x1 y1
    outline="#000", fill="#fff"   
);

r4 = canvas.create_rectangle(
    60, 60, 10, 110, # x0 y0 x1 y1
    outline="#000", fill="#fff"   
);

r5 = canvas.create_rectangle(
    60, 60, 110, 110, # x0 y0 x1 y1
    outline="#000", fill="#fff"   
);

r6 = canvas.create_rectangle(
    110, 60, 160, 110, # x0 y0 x1 y1
    outline="#000", fill="#fff"   
);

r7 = canvas.create_rectangle(
    60, 110, 10, 160, # x0 y0 x1 y1
    outline="#000", fill="#fff"   
);

r8 = canvas.create_rectangle(
    60, 110, 110, 160, # x0 y0 x1 y1
    outline="#000", fill="#fff"   
);

r9 = canvas.create_rectangle(
    110, 110, 160, 160, # x0 y0 x1 y1
    outline="#000", fill="#fff"   
);

canvas.pack(fill = BOTH, expand = 1);




i = 0;
temp = 90;
subtemp = 0;
for i in range(temp):
    subtemp += 1000;

while i <= subtemp:
    root.after(i, change_color);
    i += 1000;

root.mainloop();