from tkinter import *;
from random import choice, randint;
from time import sleep;
from os import system;

colors = ['black', 'white'];

def change_color(rectangle):
    # system('cls');
    color = colored_array[rectangle];
    color = colors[colors.index(color) - 1];
    colored_array[rectangle] = color;
    canvas.itemconfig(rectangle, fill = color, outline = '#000');
    
    print(colored_array);

def click(event):
    x = event.x;
    y = event.y;
    print(x, y);

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
canvas.tag_bind(r1, '<Button-1>', lambda event: change_color(r1));
canvas.tag_bind(r2, '<Button-1>', lambda event: change_color(r2));
canvas.tag_bind(r3, '<Button-1>', lambda event: change_color(r3));
canvas.tag_bind(r4, '<Button-1>', lambda event: change_color(r4));
canvas.tag_bind(r5, '<Button-1>', lambda event: change_color(r5));
canvas.tag_bind(r6, '<Button-1>', lambda event: change_color(r6));
canvas.tag_bind(r7, '<Button-1>', lambda event: change_color(r7));
canvas.tag_bind(r8, '<Button-1>', lambda event: change_color(r8));
canvas.tag_bind(r9, '<Button-1>', lambda event: change_color(r9));
colored_array = {r1: 'white', r2: 'white', r3: 'white', r4: 'white', r5: 'white', r6: 'white', r7: 'white', r8: 'white', r9: 'white'};

'''
i = 0;
temp = 90;
subtemp = 0;
for i in range(temp):
    subtemp += 1000;

while i <= subtemp:
    root.after(i, change_color);
    i += 1000;
'''
root.mainloop();