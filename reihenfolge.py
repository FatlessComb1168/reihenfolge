'''
Reihenfolge.
Copyright (C) 2022 by Fedor Egorov <fedoregorov1@yandex.ru>
This file is part of Reihenfolge.

Reihenfolge is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Reihenfolge is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Reihenfolge. If not, see <https://www.gnu.org/licenses/>.
'''

from tkinter import *;
from random import choice;
from time import sleep;
from threading import Thread;
from webbrowser import open_new;
from os import _exit;

def on_close():
    _exit(1);

def crr(x1, y1, x2, y2):
    return canvas.create_rectangle(
        x1, y1, x2, y2,
        outline = "#000", fill = "#fff" 
    );

def clear():
    for i in array:
        canvas.itemconfig(i, fill = '#fff', outline = '#000');

def links(text, x, y, l):
    global root;
    link = Label(text = text, font = ('Arial',
        8), fg = 'blue', cursor = 'hand2', underline = True);
    link.place(x = x, y = y);
    link.bind("<Button-1>", lambda e: open_new(l));

def start_level():
    global seq;
    wp.config(text = 'Wait...', fg = '#f00');
    seq = [];
    
    for i in range(level + 1):
        seq.append(choice(array));
    print('Level sequence:', seq);
    for i in seq:
        clear();
        sleep(0.5);
        canvas.itemconfig(i, fill = '#000', outline = '#000');
        sleep(0.5);
    wp.config(text = 'Play', fg = '#0c0');
    clear();

def change_color(r):
    global seq, seq2, temp, re, re_a, subscore, score_lbl, lever;
    if lever == True:
        seq2.append(r);
        clear();
        temp += 1;

        if seq2[temp] == seq[temp]:
            if temp == level:
                canvas.itemconfig(r, fill = '#0f0', outline = '#000');
            else:
                if seq2[temp] == seq2[temp - 1]:
                    re += 1;
                    if re >= 10:
                        canvas.itemconfig(r,
                            fill = f'#{re_a[re - 10] * 3}', outline = '#000');
                    else:
                        canvas.itemconfig(r, fill = f'#{str(re) * 3}',
                            outline = '#000');

                else:
                    canvas.itemconfig(r, fill = '#000', outline = '#000');
            
            subscore += 1;
            score_lbl.config(text = f'Score: {subscore}');
            
        else:
            canvas.itemconfig(r, fill = '#f00', outline = '#000');
            lever = False;

        print('Player sequence:', seq2, "Game's sequence:", seq);

def game():
    global seq, seq2, temp, level, re, lvl_name, score, subscore, lever;
    
    while True:
        lever = False;
        start_level();
        lever = True;

        seq2 = [];
        temp = -1;
        re = 0;
        subscore = score;

        while temp <= level:
            if temp >= 0 and seq2[temp] != seq[temp]:
                    print('Incorrect!');
                    lever = False;
                    sleep(1);
                    break;

            elif level == temp and seq2[temp] == seq[temp]:
                level += 1;
                print('Nice! The next level is', level + 1);
                lvl_name.config(text = f'Level {level + 1}');
                score = subscore;
                score_lbl.config(text = f'Score: {score}');
                lever = False;
                sleep(1);
                break;

root = Tk();
root.title('Reihenfolge');
root.geometry('460x180');
root.resizable(width = False, height = False);

canvas = Canvas(root);
r1 = crr(60, 10, 10, 60);
r2 = crr(60, 10, 110, 60);
r3 = crr(110, 10, 160, 60);
r4 = crr(60, 60, 10, 110);
r5 = crr(60, 60, 110, 110);
r6 = crr(110, 60, 160, 110);
r7 = crr(60, 110, 10, 160);
r8 = crr(60, 110, 110, 160);
r9 = crr(110, 110, 160, 160);
canvas.pack(fill = 'both', expand = 1);

canvas.tag_bind(r1, '<Button-1>', lambda event: change_color(r1));
canvas.tag_bind(r2, '<Button-1>', lambda event: change_color(r2));
canvas.tag_bind(r3, '<Button-1>', lambda event: change_color(r3));
canvas.tag_bind(r4, '<Button-1>', lambda event: change_color(r4));
canvas.tag_bind(r5, '<Button-1>', lambda event: change_color(r5));
canvas.tag_bind(r6, '<Button-1>', lambda event: change_color(r6));
canvas.tag_bind(r7, '<Button-1>', lambda event: change_color(r7));
canvas.tag_bind(r8, '<Button-1>', lambda event: change_color(r8));
canvas.tag_bind(r9, '<Button-1>', lambda event: change_color(r9));

array = [r1, r2, r3, r4, r5, r6, r7, r8, r9];
level = 0;
score = 0;
re_a = ['a', 'b', 'c', 'd', 'e', 'f'];

Label(text = 'Reihenfolge', font = ('Arial',
    16, 'bold')).place(x = 170, y = 8);

lvl_name = Label(text = f'Level {level + 1}', font = ('Arial', 12));
lvl_name.place(x = 170, y = 38);

score_lbl = Label(text = f'Score: {score}', font = ('Arial', 12));
score_lbl.place(x = 170, y = 58);

wp = Label(text = 'Wait...', font = ('Arial', 12, 'bold'), fg = '#f00');
wp.place(x = 170, y = 78);

Label(text = 'Game by Fedor Egorov aka FatlessComb1168', font = ('Arial',
    8)).place(x = 170, y = 103);

links('(GitHub)', 395, 103, "https://github.com/FatlessComb1168");
links('Reihenfolge on GitHub', 170, 123,
    "https://github.com/FatlessComb1168/reihenfolge");
links('Learn more about GNU GPL v3.0...', 170, 143,
    "https://www.gnu.org/licenses/gpl-3.0.en.html");

Thread(target = game).start();

root.protocol('WM_DELETE_WINDOW', lambda: _exit(1));
root.mainloop();