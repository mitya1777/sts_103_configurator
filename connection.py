import customtkinter;
import configuration;
from tkinter import *;
from tkinter import filedialog;
from pathlib import Path;


frame_connection = customtkinter.CTkFrame(
    configuration.window,
)

def interface_connetion_initialization():
    labels_connection_initialization();
    entries_initialization();
    buttons_initialization();



#
#   labels definition
#
def labels_connection_initialization():
    label_connection_base = customtkinter.CTkLabel(
        frame_connection,
        text = "Настройки подключения",
        anchor = 'center',
        font = ('Courier New', 18, 'bold')
    )
    label_connection_base.grid(row = 1, column = 2);

def labels_initialization():
    label_port_choice = customtkinter.CTkLabel(
        frame_connection,
        text = "Выбор\nCom-порта",
        font = ('Courier New', 14)
    )
    label_port_choice.grid(row = 10, column = 1, padx = 10, pady = 5);

    label_bitrate = customtkinter.CTkLabel(
        frame_connection,
        text = "Скорость обмена данными",
        font = ('Courier New', 14)
    )
    label_bitrate.grid(row = 10, column = 2, padx = 10, pady = 0);

    label_file_choice = customtkinter.CTkLabel(
        frame_connection,
        text = "Файл прошивки",
        font = ('Courier New', 14)
    )
    label_file_choice.grid(row = 10, column = 3, padx = 10, pady = 0);

#
#   entries definition
#
def entries_initialization():
    entry_bitrate = customtkinter.CTkEntry(
        frame_connection,
    )
    entry_bitrate.grid(row = 11, column = 2);
    bitrate = entry_bitrate.get();
    bitrate = bitrate_switch(bitrate);
    entry_bitrate.insert(0, bitrate);

    temp_variable_0 = StringVar(frame_connection);
    temp_variable_0.set("COM1");
    dropdown_port_choice = customtkinter.CTkOptionMenu(
        frame_connection,
        #temp_variable_0,
        values = ('COM1', 'COM2', 'COM3', 'COM4', 'COM5'),
        font = ('Courier New', 14, 'bold')
    )
    dropdown_port_choice.grid(row = 11, column = 1, padx = 10, pady = 0);

def browse_file_initialization():
    temporary_0 = filedialog.askopenfilename(
        initialdir = "C:/",
        title = "Выберете файл",
        filetypes = (
            ("Text files", "*.txt"),
            ("bin files", "*.bin"),
            ("hex files", "*.hex")
        )
    )

#
#   buttons definition
#
def buttons_initialization():
    button_file_browse = customtkinter.CTkButton(
        frame_connection,
        text = "Выбор файла прошивки",
        command = browse_file_initialization,
        font = ('Courier New', 14, 'bold')
    )
    button_file_browse.grid(row = 11, column = 3, pady = 10);

    button_launch = customtkinter.CTkButton(
        frame_connection,
        text = "Обновить ПО",
        font = ('Courier New', 14, 'bold')
    )
    button_launch.grid(row = 12, column = 3, pady = 10);

#
#   auxiliary functions 
#
def bitrate_switch(bitrate):
    if bitrate != 2400 | 4800:
        bitrate = 9600;
    return bitrate;
