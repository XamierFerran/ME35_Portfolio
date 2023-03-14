import matlab.engine
import paho.mqtt.client as mqtt #import the client1
import time

def whenCalled(client, userdata, message):
    print("received " ,str(message.payload.decode("utf-8")))
    print("from topic ",message.topic)

t1 = [-43.1633,-39.3492,-34.0730,-29.1270,-25.4186,-21.5189,-17.8753,-14.4901,-10.9556,-7.6256,-4.5035,-0.6528,0.6676,4.1273]
t2= [0,87.4807,108.5002,110.9248,104.5588,100.8438,96.5339,91.6246,87.7044,83.1333,77.8680,75.0342,63.1329,58.5350]

broker = '10.245.155.186'
topic_pub = "angles"
topic_sub = "angles"

client = mqtt.Client("fred") # use a unique name
client.on_message = whenCalled # callback
client.connect(broker)
print('Connected to %s MQTT broker' % broker)

client.loop_start() #start the loop
client.subscribe(topic_sub)

i = 0
for i in range(len(t1)):
    print("Publishing message to topic",topic_pub)
    word = "(" + str(t1[i]) + "," + str(t2[i]) + ")"
    client.publish(topic_pub,word)
    time.sleep(5) # wait for a little
    i+=1
client.loop_stop() #stop the loop
