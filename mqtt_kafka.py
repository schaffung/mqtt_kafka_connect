#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 14:30:52 2019

@author: schaffung
"""

import json
import paho.mqtt.client as mqtt
from kafka import KafkaProducer
from connect_config_read import ConfigFileDetails

def on_connect(client, userdata, flag, result_code):
    """ This API is the callback used when the MQTT Client is connected to broker"""
    print("MQTT Client connected with Result Code : ", result_code)

def on_message(client, userdata, message):
    """ This API is the callback when a message arrives to the MQTT Client"""
    global PRODUCER, CONNECTION_INFORMATION
    mqtt_message = message.payload.decode()
    my_dict = json.loads(mqtt_message)
    #print(my_dict)
    try:
        PRODUCER.send(CONNECTION_INFORMATION[0]['KAFKA']['topic'], my_dict)
    except:
        print("Failure in print message.")

CONFIGHANDLE = ConfigFileDetails()
CONFIGHANDLE.extract_config_file_informations()
CONNECTION_INFORMATION = CONFIGHANDLE.send_connection_information()
print("Connection information : ", CONNECTION_INFORMATION)

# Defining the Kafka connection.
ADDRESS_VALUE = CONNECTION_INFORMATION[0]['KAFKA']['address']+":" \
                 +str(CONNECTION_INFORMATION[0]['KAFKA']['port'])
try:
    PRODUCER = KafkaProducer(bootstrap_servers=ADDRESS_VALUE,
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))
except:
    print("kafka Connection failed.")
    quit()

# Defining MQTT connection.

CLIENT = mqtt.Client()
CLIENT.on_connect = on_connect
CLIENT.on_message = on_message
try:
    CLIENT.connect(CONNECTION_INFORMATION[0]['MQTT']['address'],
                   CONNECTION_INFORMATION[0]['MQTT']['port'])
except:
    print("MQTT Connection Failed.")
    quit()

CLIENT.subscribe(CONNECTION_INFORMATION[0]['MQTT']['topic'], qos=1)

CLIENT.loop_forever()
