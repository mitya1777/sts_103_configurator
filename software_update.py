import customtkinter;
import configuration;
from customtkinter import filedialog;
from customtkinter import *;
from pathlib import Path;


frame_sw_updation = customtkinter.CTkFrame(
    configuration.window,
    width = 700,
    height = 100,
    )

def interface_sw_updation_initialization():
    frame_sw_updation.pack(expand = True, side = TOP);
    buttons_initialization();

#
#   buttons definition
#
def buttons_initialization():
    button_file_browse = customtkinter.CTkButton(
        frame_sw_updation,
        text = "Выбор файла прошивки",
        command = browse_file_initialization,
        font = ('Courier New', 14, 'bold')
    )
    button_file_browse.grid(row = 0, column = 0, padx = 10);

    button_launch = customtkinter.CTkButton(
        frame_sw_updation,
        text = "Обновить ПО",
        font = ('Courier New', 14, 'bold')
    )
    button_launch.grid(row = 0, column = 1, pady = 10);

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