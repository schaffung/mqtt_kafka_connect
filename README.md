# mqtt_kafka_connect
A medium for linking mqtt to kafka


The usual problem while working with the IOT is that we don't have a robust open source connector between MQTT and Kafka which is at the same time simple to execute. 

So, in this case, we have a MQTT-KAFKA connector created in Python. 

Before jumping into the Connector part, I assume that you already have installed some MQTT Broker and a Kafka Broker, so I won't be guiding you in the installation of these two. 

But following are some of the modules which would be required before running the connect code.

sudo pip3 install kafka-python
sudo pip3 install paho-mqtt

Now once these have been installed,the next step would be to populate the configuration file according to your needs. At present there are three properties in two sections,

[MQTT]
MQTTBrokerAddress = "mention the ip or the url of the Broker"
MQTTBrokerPort = "port number of the broker"
MQTTTopic = "the topic in which the data is published and from which you want to pull and push it into kafka"

[Kafka]
KafkaBrokerAddress = "mention the ip or the url of the Broker"
KafkaBrokerPort = "port number of the broker"
KafkaTopic = "the topic in which you want to produce towards Kafka side"


Then, execute...
python3 mqtt_kafka.py

It will start the connection. 

First, it will define the subscriptions for MQTT using the configuration you provided and hence the callbacks would be created. Once that is done, whenever the message arrives, the message is produced into the corresponding Kafka topic.
