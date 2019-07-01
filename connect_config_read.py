"""The module is used for parsing the config file and obtaining information to be
put when connecting the MQTT with KAFKA."""

# REQUIRED MODULES
import configparser


class ConfigFileDetails():
    """This class is conerned with the configurations
    for the pipeline"""

    def __init__(self):
        """The Constructor"""
        self.config_handle = configparser.ConfigParser()
        self.sections_in_config = []
        self.connection_information = []

    def read_config_file(self, file_name):
        """This API is for reading a config file"""
        self.config_handle.read(file_name)

    def get_config_main_sections(self):
        """This API is used for getting the main sections"""
        self.sections_in_config = self.config_handle.sections()

    def extract_connection_properties(self):
        """This API is used for extracting the connection details"""
        try:
            localdict = {"MQTT" : {\
                                 "address" : self.config_handle['MQTT']['MQTTBrokerAddress'],\
                                 "port" : int(self.config_handle['MQTT']['MQTTBrokerPort']),\
                                 "topic" : self.config_handle['MQTT']['MQTTTopic']},\
                         "KAFKA" : {\
                                 "address" : self.config_handle['Kafka']['KafkaBrokerAddress'],\
                                 "port" : int(self.config_handle['Kafka']['KafkaBrokerPort']),\
                                 "topic" : self.config_handle['Kafka']['KafkaTopic']}\
                        }
            self.connection_information.append(localdict)
        except:
            print("Error in extracting connection properties")

    def extract_config_file_informations(self, file_name="connect_properties.ini"):
        """This API is the wrapper exposed to the outside world"""
        try:
            self.read_config_file(file_name)
            self.get_config_main_sections()
            self.extract_connection_properties()
        except:
            print("Error in extraction of Configuration file information")

    def send_connection_information(self):
        """API is used to pass the connection information"""
        return self.connection_information

    def print_config_main_sections(self):
        """This API is used for printing the sections list"""
        try:
            print("Main Sections in config file : ", self.sections_in_config)
        except:
            print("Invalid Config File.")

    def print_connection_information(self):
        """API is used for printing the connection information extracted from the config file"""
        try:
            print(self.connection_information)
        except:
            print("Error in displaying connection information.")

if __name__ == "__main__":
    CONFIGURATIONS = ConfigFileDetails()

    CONFIGURATIONS.read_config_file('connect_properties.ini')

    CONFIGURATIONS.get_config_main_sections()

    CONFIGURATIONS.print_config_main_sections()

    CONFIGURATIONS.extract_connection_properties()

    CONFIGURATIONS.print_connection_information()

    CVAL = CONFIGURATIONS.send_connection_information()

    print(CVAL[0])

    print(CVAL[0]['MQTT']['address'])
