import tkinter;
import config;
import entries;
from tkinter import *;
from tkinter import messagebox;
from entries import browse_file_initialization;


def buttons_initialization():
    button_file_browse = Button(
        config.frame,
        text = "Выбор файла прошивки",
        command = browse_file_initialization,
    )
    button_file_browse.grid(row = 2, column = 3, pady = 10);

    button_launch = Button(
        config.frame,
        text = "Обновить ПО",
    )
    button_launch.grid(row = 3, column = 3, pady = 10);
