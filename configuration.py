import customtkinter;
import os;
import crc;

#
#   global variables
#
baudrate = 9600;
com_port = 0;
path_absolute = os.path.dirname(__file__);
path_stuff = os.path.join(path_absolute, 'stuff/piqs');
path_piq_port_update = os.path.join(path_stuff, 'port_updation.png');
window = customtkinter.CTk();
tx_buffer = [];
slave_device_address = 0x00;
slave_device_identificator = 0x67;


def crc_initialization():
    crc.Configuration(
        width = 0x10,
        polynomial = 0x1021,
        init_value = 0xFFFF,
        final_xor_value =0x00,
        reverse_input = False,
        reverse_output = False
    )

#customtkinter.set_default_color_theme("green");

