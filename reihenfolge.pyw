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
from tkinter import ttk;
import sqlite3 as sl;
from random import choice, randint;
from time import sleep;
from threading import Thread;
from webbrowser import open_new;
from os import _exit, execv, getenv;
import os;
from sys import executable, argv;

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

def geometry(window, window_width, window_height):
    screen_width = window.winfo_screenwidth();
    screen_height = window.winfo_screenheight();

    x_cordinate = int((screen_width / 2) - (window_width / 2));
    y_cordinate = int((screen_height / 2) - (window_height / 2));

    window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate));
    window.resizable(width=False, height=False);

def start_level():
    global seq, speed;
    wp.config(text = 'Wait...', fg = '#f00');
    seq = [];
    
    for i in range(level + 1):
        seq.append(choice(array));
    print('Level sequence:', seq);

    for i in seq:
        if tflag == False:
            clear();
            break;
        clear();
        sleep(speed);
        canvas.itemconfig(i, fill = '#000', outline = '#000');
        sleep(speed);

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
    global seq, seq2, temp, level, re, lvl_name, score, subscore, lever, tflag;
    
    Thread(target = timer).start();
    while tflag:
        lever = False;
        start_level();
        lever = True;

        seq2 = [];
        temp = -1;
        re = 0;
        subscore = score;

        while temp <= level and tflag != False:
            if temp >= 0 and seq2[temp] != seq[temp]:
                if tflag == False:
                    break;
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
        
        if tflag == False:
            break;
        
        if mode == 0 and seq2[temp] != seq[temp]:
            play_again = crr(10, 10, 160, 160);
            Label(root, text = 'Whoops!', bg = '#fff',
                font = ('Arial', 16)).place(x = 38, y = 55);
            play_againb = Label(root, text = '↻', bg = '#fff',
                font = ('Segoe UI Black', 16));
            play_againb.place(x = 70, y = 80);
            play_againb.bind('<Button-1>', lambda e: reset());
            print('You lose! Play again?');
            tflag = False;

def timer():
    global h, m, s, timeq;
    h = 0;
    m = 0;
    s = 0;
    while tflag:
        sleep(1);
        s = int(s);
        m = int(m);
        h = int(h);

        s += 1;
        if s == 60:
            s = 0;
            m += 1;
        if m == 60:
            m = 0;
            h += 1;

        s = f'0{s}' if s < 10 else s;
        m = f'0{m}' if m < 10 else m;
        h = f'0{h}' if h < 10 else h;

        timeq = f'{h}:{m}:{s}';
        time.config(text = timeq);

def change(x):
    global mode;
    mode = x;

def savespeed():
    global speed, speed_e;
    speed = 0.5 / float(speed_e.get());
    setting.destroy();

def settings():
    global speed_e, speed, mode, setting, ch, setting;
    setting = Tk();
    setting.title('Reihenfolge Settings');
    geometry(setting, 300, 150);

    Label(setting, text = 'Settings').place(x = 120, y = 10);
    Label(setting, text = 'Mode:').place(x = 10, y = 40);
    Label(setting, text = 'Speed: ').place(x = 100, y = 40);

    ttk.Radiobutton(setting, variable = ch, value = 0, text = 'Classic', 
        command = lambda: change(0)).place(x = 10, y = 60);
    ttk.Radiobutton(setting, variable = ch, value = 1, text = 'Infinite',
        command = lambda: change(1)).place(x = 10, y = 80);

    speed_e = ttk.Entry(setting, width = 5);
    speed_e.place(x = 150, y = 40);
    speed_e.insert(0, (0.5 / speed));
    
    setting.protocol('WM_DELETE_WINDOW', lambda: savespeed());

def results():
    results_w = Tk();
    results_w.title('Records');
    geometry(results_w, 335, 200);

    columns = ('#1', '#2', '#3', '#4', '#5');
    tree = ttk.Treeview(results_w, show = 'headings', columns = columns);
    tree.heading('#1', text = 'Place');
    tree.column('#1', width = 50, anchor = 'center');
    tree.heading('#2', text = 'Player');
    tree.column('#2', width = 100, anchor = 'center');
    tree.heading('#3', text = 'Level');
    tree.column('#3', width = 50, anchor = 'center');
    tree.heading('#4', text = 'Score');
    tree.column('#4', width = 70, anchor = 'center');
    tree.heading('#5', text = 'Time');
    tree.column('#5', width = 60, anchor = 'center');
    sb = ttk.Scrollbar(results_w, orient = 'vertical', command = tree.yview);
    tree.config(yscroll = sb.set);

    db = sl.connect(getenv('APPDATA') + r'\Reihenfolge\res.db');
    # DESC - sort on descending order
    info = db.execute('SELECT * FROM PLAYERS ORDER BY score DESC');
    place = 1;
    for rec in info:
        rec = [place] + list(rec);
        tree.insert("", 'end', values = rec);
        place += 1;
    
    tree.pack(expand = True);

def reset():
    global write_name;
    if mode == 0:
        wrname = Tk();
        geometry(wrname, 300, 100);
        wrname.title('Enter your nickname');
        wrname.geometry('300x100');

        Label(wrname, text =
            'Enter your nickname for results:').place(x = 60, y = 20);
        write_name = ttk.Entry(wrname, width = 16);
        write_name.place(x = 92, y = 45);
        write_name.insert(0, f'Player{randint(0, 10 ** 10)}');

        wrname.protocol('WM_DELETE_WINDOW', truereset);
    else:
        execv(executable, [executable] + argv);

def truereset():
    nickname = write_name.get();
    if os.path.isdir(getenv('APPDATA') + '\Reihenfolge'):
        if not os.path.exists(getenv('APPDATA') + r'\Reihenfolge\res.db'):
            print('RE');
            with open(getenv('APPDATA') + r'\Reihenfolge\res.db', 'w') as f:
                f.write('');
                f.close();
    else:
        os.mkdir(getenv('APPDATA') + '\Reihenfolge');
        with open(getenv('APPDATA') + r'\Reihenfolge\res.db', 'w') as f:
                f.write('');
                f.close();
    
    db = sl.connect(getenv('APPDATA') + r'\Reihenfolge\res.db');
    data = [nickname, level, score, timeq];
    sql = "INSERT INTO PLAYERS values(?, ?, ?, ?)";
    while True:
        try:
            db.execute(sql, data);
            x = db.execute('SELECT * FROM PLAYERS');
            for i in x:
                print(i);
            db.commit();
            db.close();
            break;
        except:
            db.execute("""
                    CREATE TABLE PLAYERS (
                        nickname TEXT,
                        level INTEGER,
                        score INTEGER,
                        time TIME
                    );
                """);

    execv(executable, [executable] + argv);

root = Tk();
root.title('Reihenfolge');
geometry(root, 460, 180);

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
mode = 0;
ch = BooleanVar(value = mode);
speed = 0.5;
tflag = True;
re_a = ['a', 'b', 'c', 'd', 'e', 'f'];

Label(text = 'Reihenfolge', font = ('Arial',
    16, 'bold')).place(x = 170, y = 8);

ttk.Button(text = '⚙', width = 3, command = settings).place(x = 300, y = 12);
ttk.Button(text = '↻', width = 3, command = reset).place(x = 330, y = 12);
ttk.Button(text = '🏆', width = 3, command = results).place(x = 360, y = 12);

time = Label(text = '00:00:00', font = ('Arial', 12));
time.place(x = 240, y = 38);

lvl_name = Label(text = f'Level 1', font = ('Arial', 12));
lvl_name.place(x = 170, y = 38);

score_lbl = Label(text = f'Score: 0', font = ('Arial', 12));
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

th = Thread(target = game);
th.start();

root.protocol('WM_DELETE_WINDOW', lambda: _exit(1));
root.mainloop();