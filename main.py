import tkinter;
import customtkinter;
import configuration;
import connection;
import system;
import software_update;


configuration.window.title("Программа загрузчика STS-103");
configuration.window.geometry('520x730');

connection.interface_connetion_initialization();
system.interface_system_initialization();
software_update.interface_sw_updation_initialization();

configuration.window.mainloop();
