import tkinter;
import config;
from tkinter import *;
from tkinter import messagebox;


def labels_initialization():
    label_port_choice = Label(
        config.frame,
        text = "Выбор\nCom-порта"
    )
    label_port_choice.grid(row = 1, column = 1, padx = 10, pady = 5);

    label_bitrate = Label(
        config.frame,
        text = "Скорость обмена данными"
    )
    label_bitrate.grid(row = 1, column = 2, padx = 10, pady = 0);

    label_file_choice = Label(
        config.frame,
        text = "Файл прошивки"
    )
    label_file_choice.grid(row = 1, column = 3, padx = 10, pady = 0);


