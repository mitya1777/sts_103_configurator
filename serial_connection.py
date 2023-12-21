import serial;
import serial.tools.list_ports;

baudrate = 9600;

available_ports = serial.tools.list_ports.comports();
list_of_ports = [];
for port in available_ports:
    list_of_ports.append(port.device);

device_version = "Данные отсутсвуют";

def port_setup_connection(com_port = list_of_ports[0], baudrate = baudrate):
    baudrate = baudrate;
