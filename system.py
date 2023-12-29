import customtkinter;
import configuration;
import serial_connection;
from tkinter import *;



frame_system = customtkinter.CTkFrame(
    configuration.window,
    width = 300,
    height = 500
)

label_system_base = customtkinter.CTkLabel(frame_system);
label_version = customtkinter.CTkLabel(frame_system);
label_version_out = customtkinter.CTkLabel(frame_system);

def interface_system_initialization():
    frame_system.pack(expand = True, side = TOP);
    frame_system.grid_propagate(0);
    labels_initialization();
    #entries_initialization();

#
#   labels definition
#
def labels_initialization():
    label_system_base = customtkinter.CTkLabel(
        frame_system,
        text = "Системные параметры",
        font = ('Courier New', 18, 'bold'),
        width = 300,
        anchor = 'center',
        justify = 'center'
    )
    label_system_base.grid(row = 0, column = 0, columnspan = 2, sticky = 'ew');

    label_version = customtkinter.CTkLabel(
        frame_system,
        text = "Версия ПО",
        font = ('Courier New', 14),
        anchor = 'w',
        justify = 'left'
    )
    label_version.grid(padx = 10, row = 1, column = 0, sticky = 'w');

    label_version_out = customtkinter.CTkLabel(
        frame_system,
        text = configuration.device_version,
        font = ('Courier New', 14),
        anchor = 'e',
        justify = 'right',
    )
    label_version_out.grid(padx = 10, row = 1, column = 1, sticky = 'e');

def labels_deinitialization():
    label_system_base.destroy();
    label_version.destroy();
    label_version_out.destroy();


#
#   entries definition
#
def entries_initialization():
    entry_version = customtkinter.CTkEntry(
        frame_system
    )
    entry_version.grid(row = 2, column = 2);