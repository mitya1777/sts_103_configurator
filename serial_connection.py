import serial;
import serial.tools.list_ports;
import configuration;
import crc;
from crc import Crc16;
import system;


osi_transport_base =    {
    'RS485_CORRECT_PACKET': 0x00,
    'RS485_START_BYTE': 0xFD,
    'RS485_STOP_BYTE': 0xFE,
    'RS485_RECEIVING_COMPLETION': 0x01,
    'RS485_PACKET_IS_NOT_DETECTED': 0x03,
    'RS485_ERROR_IN_CRC': 0x04,
    'RS485_WRONG_ADDRESS': 0x05,
    'RS485_WRONG_DEVICE_TYPE': 0x06,
    'RS485_UNKNOWN_COMMAND': 0x07,
    'RS485_UNKNOWN_PARAMETER': 0x08,
    'RS485_WRONG_PARAMETER': 0x09,
    'RS485_INCORRECT_PACKET': 0x0A
}

osi_transport_commands =    {
    'COMMAND_DEVICE_STATE': 0x00,
    'COMMAND_PARAMETERS_GETTING': 0x01,
    'COMMAND_PARAMETERS_SETTING': 0x02,
    'COMMAND_PARAMETERS_DEFAULT': 0x03,
    'COMMAND_DEVICE_SEARCHING': 0x04,
    'COMMAND_BOOTLOADER_STARTING': 0x73
}

osi_application_parameters= {
    'PARAMETER_DEVICE_TYPE': 0x00,
    'PARAMETER_DEVICE_ADDRESS': 0x01,
    'PARAMETER_BITRATE': 0x02,
    'PARAMETER_LOW_VOLTAGE_THRESHOLD': 0x03,
    'PARAMETER_HIGH_VOLTAGE_THRESHOLD': 0x04,
    'PARAMETER_VOLTAGE_PERIOD_MEASUREMENT': 0x05,
    'PARAMETER_INDICATION_MODE': 0x06,
    'PARAMETER_ALERT_EXPIRE': 0x07,
    'PARAMETER_PYD1588_THRESCHOLD': 0x08,
    'PARAMETER_PYD1588_BLIND_TIME': 0x09,
    'PARAMETER_PYD1588_PULSE_COUNTER': 0x0A,
    'PARAMETER_PYD1588_WINDOW_TIME': 0x0B,
    'PARAMETER_PYD1588_SIGNAL_SOURCE': 0x0C,
    'PARAMETER_PYD1588_CUT_OFF_FREQUENCY': 0x0D,
    'PARAMETER_PYD1588_COUNTING_MODE': 0x0E,
    'PARAMETER_PYD1588_RAW_DATA': 0x0F,
    'PARAMETER_VOLTAGE_VALUE': 0x10,
    'PARAMETER_EVENTS_QUANTITY': 0x11,
    'PARAMETER_SERIAL_NUMBER': 0x12,
    'PARAMETER_DEVICE_VERSION': 0x13
}


#
#   variables
#
list_of_ports = [];

def available_ports_updation():
    list_of_ports.clear();
    available_ports = serial.tools.list_ports.comports();
    for port in available_ports:
        list_of_ports.append(port.device);

def port_setup_connection():
    global connection;
    port = configuration.com_port;
    baudrate = configuration.baudrate;
    connection = serial.Serial(port, baudrate, timeout = 100);

    tx_size = packet_forming(osi_transport_commands['COMMAND_PARAMETERS_GETTING'],
                             osi_application_parameters['PARAMETER_DEVICE_VERSION']);
    data_transmit_process(pacet_size = tx_size);
    data_receive_process();
    
    tx_size = packet_forming(osi_transport_commands['COMMAND_PARAMETERS_GETTING'],
                             osi_application_parameters['PARAMETER_DEVICE_ADDRESS']);
    data_transmit_process(pacet_size = tx_size);
    data_receive_process();

    if connection.is_open:
        connection.close();
   
def packet_forming(osi_transport_command, osi_application_parameter):
    crc_calculator = configuration.crc_initialization();
    configuration.tx_buffer[0x00] = osi_transport_base['RS485_START_BYTE'];
    configuration.tx_buffer[0x01] = configuration.slave_device_address;
    configuration.tx_buffer[0x02] = configuration.slave_device_identificator;
    configuration.tx_buffer[0x03] = osi_transport_command;
    configuration.tx_buffer[0x04] = 0x01;
    configuration.tx_buffer[0x05] = 0x00;
    configuration.tx_buffer[0x06] = osi_application_parameter;
    crc_calculated = crc_calculation(configuration.tx_buffer[0x01 : 0x07]);
    configuration.tx_buffer[0x07] = (crc_calculated & 0xFF00) >> 0x8;
    configuration.tx_buffer[0x08] = (crc_calculated & 0x00FF);
    configuration.tx_buffer[0x09] = osi_transport_base['RS485_STOP_BYTE'];
    tx_size = 0x0A;
    return tx_size;

def data_transmit_process(pacet_size):
    connection.write(configuration.tx_buffer[0x00 : pacet_size]);
    connection.reset_output_buffer();
    connection.timeout = 100e-3;

def data_receive_process():
    configuration.rx_buffer = connection.readline();
    for shift in range(len(configuration.rx_buffer)):
        try0 = configuration.rx_buffer[shift];
        if(configuration.rx_buffer[shift] == osi_transport_base['RS485_START_BYTE']):
            packet_start = shift;
        if(configuration.rx_buffer[shift] == osi_transport_base['RS485_STOP_BYTE']):
            rx_size = shift - packet_start + 0x01;
            if(rx_size >= 0x05):
                transport_packet_parsing(configuration.rx_buffer[0x03]),
            break;
    connection.reset_input_buffer();

def transport_packet_parsing(osi_transport_command):
    match(osi_transport_command ^ 0x80):
        case 0x01:
            application_packet_parsing(configuration.rx_buffer[0x06]);

def application_packet_parsing(osi_application_parameter):
    match(osi_application_parameter):
        #case 0x00:

        case 0x13:
            configuration.device_version = configuration.rx_buffer[0x07 : 0x0F];
            system.labels_initialization();

            #   add the device type, address fields.
'''        
    
    'PARAMETER_LOW_VOLTAGE_THRESHOLD': 0x03,
    'PARAMETER_HIGH_VOLTAGE_THRESHOLD': 0x04,
    'PARAMETER_VOLTAGE_PERIOD_MEASUREMENT': 0x05,
    'PARAMETER_INDICATION_MODE': 0x06,
    'PARAMETER_ALERT_EXPIRE': 0x07,
    'PARAMETER_PYD1588_THRESCHOLD': 0x08,
    'PARAMETER_PYD1588_BLIND_TIME': 0x09,
    'PARAMETER_PYD1588_PULSE_COUNTER': 0x0A,
    'PARAMETER_PYD1588_WINDOW_TIME': 0x0B,
    'PARAMETER_PYD1588_SIGNAL_SOURCE': 0x0C,
    'PARAMETER_PYD1588_CUT_OFF_FREQUENCY': 0x0D,
    'PARAMETER_PYD1588_COUNTING_MODE': 0x0E,
    'PARAMETER_PYD1588_RAW_DATA': 0x0F,
    'PARAMETER_VOLTAGE_VALUE': 0x10,
    'PARAMETER_EVENTS_QUANTITY': 0x11,
    'PARAMETER_SERIAL_NUMBER': 0x12,
'''

          

def crc_calculation(tx_buffer):
    crc_calculator = configuration.crc_initialization();
    crc_calculation = crc_calculator.checksum(bytes(tx_buffer));
    return crc_calculation;
