import tkinter;
import config;
from tkinter import *;
from tkinter import messagebox;


def buttons_initialization():
    button_launch = Button(
        config.frame,
        text = "Обновить ПО"
    )
    button_launch.grid(row = 2, column = 3);
