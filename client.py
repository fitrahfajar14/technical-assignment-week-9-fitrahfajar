import paho.mqtt.client as mqtt
from ult_sensor import distance
from time import sleep



# define static variable
# broker = "localhost" # for local connection
broker = "broker.hivemq.com"  # for online version
port = 1883
timeout = 60

username = 'fitrahfajar14'
password = 'qlue'

topic = "man1ponorogo/fajar"
# topic_feedback = "man1ponorogo/nama/greetings"
 
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(topic)
 
# The callback for when a PUBLISH message is received from the server.
def on_publish(client, userdata, msg):
    print("Data di Publish")


# Create an MQTT client and attach our routines to it.
client = mqtt.Client("fajar")
client.username_pw_set(username=username,password=password)
client.on_connect = on_connect
client.on_message = on_publish
 
client.connect(broker, port, timeout)


while True:
	sensor = distance()
	message = sensor
	ret = client1.publish(topic,payload=message)
