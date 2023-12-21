import customtkinter;
import configuration;
import serial_connection;
from customtkinter import *;


frame_connection = customtkinter.CTkFrame(
    configuration.window,
    width = 700,
    height = 500,
    )

def interface_connetion_initialization():
    frame_connection.pack(expand = True, side = TOP);
    labels_initialization();
    entries_initialization();
    buttons_initialization();

#
#   labels definition
#
def labels_initialization():
    label_connection_base = customtkinter.CTkLabel(
        frame_connection,
        text = "Настройки подключения",
        font = ('Courier New', 18, 'bold'),
        width = 500
        #anchor = 'center',
    )
    label_connection_base.grid(row = 0, column = 0, columnspan = 3);

    label_port_choice = customtkinter.CTkLabel(
        frame_connection,
        text = "Выбор\nCom-порта",
        font = ('Courier New', 14)
    )
    label_port_choice.grid(row = 1, column = 0, padx = 10, pady = 5);

    label_bitrate = customtkinter.CTkLabel(
        frame_connection,
        text = "Скорость обмена данными",
        font = ('Courier New', 14)
    )
    label_bitrate.grid(row = 1, column = 1, sticky = 's');

#
#   entries definition
#
def entries_initialization():
    entry_bitrate = customtkinter.CTkEntry(
        frame_connection
    )

    baudrate_list = ['2400', '4800', '9600', '19200', '57600', '115200'];
    dropdown_baudrate_choice = customtkinter.CTkOptionMenu(
        frame_connection,
        values = baudrate_list,
        font = ('Courier New', 14, 'bold')
    )
    dropdown_baudrate_choice.grid(row = 2, column = 1, padx = 10, pady = 0);

    dropdown_port_choice = customtkinter.CTkOptionMenu(
        frame_connection,
        values = serial_connection.list_of_ports,
        font = ('Courier New', 14, 'bold')
    )
    dropdown_port_choice.grid(row = 2, column = 0, padx = 10, pady = 0);


#
#   buttons definition
#
def buttons_initialization():
    button_launch = customtkinter.CTkButton(
        frame_connection,
        text = "Подключить",
        font = ('Courier New', 14, 'bold'),
        command = serial_connection.port_setup_connection()
    )
    button_launch.grid(row = 2, column = 2, pady = 10);

#
#   auxiliary functions 
#
