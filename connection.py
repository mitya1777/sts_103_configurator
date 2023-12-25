import customtkinter;
import configuration;
import serial_connection;
import PIL.Image;
import PIL.ImageTk;
import os;
from customtkinter import *;
from tkinter import *;


#
#   variables
#
piq_port_update = CTkImage(dark_image = PIL.Image.open(configuration.path_piq_port_update), size = (22, 22));
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
    configuration.crc_initialization();

#
#   labels definition
#
def labels_initialization():
    label_connection_base = customtkinter.CTkLabel(
        frame_connection,
        text = "Настройки подключения",
        font = ('Courier New', 18, 'bold'),
        width = 500
    )
    label_connection_base.grid(row = 0, column = 0, columnspan = 4);

    label_port_choice = customtkinter.CTkLabel(
        frame_connection,
        text = "Выбор\nCom-порта",
        font = ('Courier New', 14)
    )
    label_port_choice.grid(row = 1, column = 0, padx = 10, pady = 5);

    label_bitrate = customtkinter.CTkLabel(
        frame_connection,
        text = "Скорость обмена\nданными",
        font = ('Courier New', 14)
    )
    label_bitrate.grid(row = 1, column = 2, sticky = 's');

#
#   entries definition
#
def entries_initialization():
    entry_bitrate = customtkinter.CTkEntry(
        frame_connection
    )

    serial_connection.available_ports_updation();
    port_chosen =  StringVar(frame_connection);
    dropdown_port_choice = customtkinter.CTkOptionMenu(
        frame_connection,
        variable = port_chosen,
        values = serial_connection.list_of_ports,
        command = lambda port_chosen: com_port_update(port_chosen),
        font = ('Courier New', 14, 'bold'),
        anchor = 'center',
        dropdown_font= ('Courier New', 14, 'bold'),
        fg_color = '#078273',
        dropdown_fg_color = '#078273',
        button_color = '#045850',
        button_hover_color = '#045850',
        dropdown_hover_color = '#045850'
    )
    dropdown_port_choice.set(serial_connection.list_of_ports[0]);
    configuration.com_port = port_chosen.get();
    dropdown_port_choice.grid(row = 2, column = 0, padx = 5, pady = 0);
    x, y, width, grid_cell_size = frame_connection.bbox(2, 0);

    baudrate_list = ['2400', '4800', '9600', '19200', '57600', '115200'];
    baudrate_chosen = StringVar(frame_connection);
    dropdown_baudrate_choice = customtkinter.CTkOptionMenu(
        frame_connection,
        variable = baudrate_chosen,
        values = baudrate_list,
        command = lambda baudrate_chosen: baudrate_update(baudrate_chosen),
        font = ('Courier New', 14, 'bold'),
        anchor = 'center',
        dropdown_font= ('Courier New', 14, 'bold'),
        fg_color = '#078273',
        dropdown_fg_color = '#078273',
        button_color = '#045850',
        button_hover_color = '#045850',
        dropdown_hover_color = '#045850'
    )
    dropdown_baudrate_choice.set(baudrate_list[2]);
    configuration.baudrate = int(baudrate_chosen.get());
    dropdown_baudrate_choice.grid(row = 2, column = 2, padx = 5, pady = 0);

    
#
#   buttons definition
#
    button_port_update = customtkinter.CTkButton(
        frame_connection,
        command = entries_initialization,
        text = '',
        image = piq_port_update,
        width = 22,
        font = ('Courier New', 14, 'bold'),
        fg_color = '#078273',
        hover_color = '#045850'
    )
    button_port_update.grid(row = 2, column = 1, pady = 10);
    #button_port_update.grid.(row = 2, column = 1, pady = 10);

def buttons_initialization():
    button_launch = customtkinter.CTkButton(
        frame_connection,
        command = serial_connection.port_setup_connection,
        text = "Подключить",
        font = ('Courier New', 14, 'bold'),
        fg_color = '#078273',
        hover_color = '#045850'
    )
    button_launch.grid(row = 2, column = 3, padx = 5, pady = 10);

#
#   auxiliary calbacks
#
def baudrate_update(baudrate):
    configuration.baudrate = int(baudrate);

def com_port_update(port):
    configuration.com_port = port;
