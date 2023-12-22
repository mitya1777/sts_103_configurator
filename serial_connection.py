import serial;
import serial.tools.list_ports;
import configuration;

device_version = "Данные отсутсвуют";

available_ports = serial.tools.list_ports.comports();
list_of_ports = [];
for port in available_ports:
    list_of_ports.append(port.device);


def port_setup_connection():
    baudrate = configuration.baudrate;
    port = configuration.com_port;
