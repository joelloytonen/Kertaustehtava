import json
import requests
import paho.mqtt.client as mqtt 
import time

if use_mqtt:
    broker_address="broker.hivemq.com"
    client = mqtt.Client("OmaYksikasitteinenTunnus") # luo uusi asiakas
    client.connect(broker_address) # avaa yhteys brokerille


#luetaan tiedosto
file = open("mobiledata.txt", "r")

for line in file:
    s = json.loads(line)
    if s['channel'] == 'solution':
        pos = s['position_lc1']

        positionData = {}
        positionData['time'] = s['time']
        positionData['x'] = pos[0]
        positionData['y'] = pos[1]
        positionData['z'] = pos[2]

        jsonm = json.dumps(positionData, indent = True)
        print(jsonm)
        # lähetetään HTTPllä
        if False: # omalle palvelinohjelmalle tai Thingspeakiin
            response = requests.post('http://localhost:5000/newmeasurement', data = jsonm)
            print(response)
        if use_mqtt:
            client.publish("my_topic", jsonm)
        time.sleep(1)