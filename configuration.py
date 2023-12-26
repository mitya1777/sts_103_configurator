import customtkinter;
import os;
import crc;
import array;
from crc import Crc16;

#
#   global variables
#
TX_BUFFER_SIZE = 0x20;
RX_BUFFER_SIZE = 0x100;

baudrate = 9600;
com_port = 0;
path_absolute = os.path.dirname(__file__);
path_stuff = os.path.join(path_absolute, 'stuff/piqs');
path_piq_port_update = os.path.join(path_stuff, 'port_updation.png');
window = customtkinter.CTk();
tx_buffer = array.array('B', [0x00] * TX_BUFFER_SIZE);
rx_buffer = array.array('B', [0x00] * RX_BUFFER_SIZE);

slave_device_address = 0x00;
slave_device_identificator = 0x67;
device_version = "Данные отсутсвуют";


def crc_initialization():
    crc_configuration = crc.Configuration(
        width = 0x10,
        polynomial = 0x1021,
        init_value = 0xFFFF,
        final_xor_value =0x00,
        reverse_input = False,
        reverse_output = False
    )
    crc_calculator = crc.Calculator(crc_configuration);
    return crc_calculator;
