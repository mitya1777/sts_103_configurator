import tkinter;
import configuration;
import connection;
from tkinter import *;

configuration.window.title("Программа загрузчика STS-103");
configuration.window.geometry('600x730');

connection.frame_connection.pack(expand = True);
connection.interface_connetion_initialization();

configuration.window.mainloop();
