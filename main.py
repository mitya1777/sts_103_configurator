import tkinter;
import config;
import labels;
import entries;
import buttons;
from tkinter import *;
from tkinter import messagebox;


config.window.title("Программа загрузчика STS-103");
config.window.geometry('540x230');

config.frame.pack(expand=True);
labels.labels_initialization();
entries.entries_initialization();
buttons.buttons_initialization();
config.window.mainloop();
