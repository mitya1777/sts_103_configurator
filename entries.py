import tkinter;
import config;
from tkinter import *;
from tkinter import messagebox;


def entries_initialization():
    entry_bitrate = Entry(
        config.frame,
    )
    entry_bitrate.grid(row = 2, column = 2);
    temp_variable_0 = StringVar(config.frame);
    temp_variable_0.set("COM1");
    dropdown_port_choice = OptionMenu(
        config.frame,
        temp_variable_0,   
        'COM1', 'COM2', 'COM3', 'COM4', 'COM5'
    )
    dropdown_port_choice.grid(row = 2, column = 1, padx = 10, pady = 0);
