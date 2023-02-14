# coding=utf-8
import random
from paho.mqtt import client as mqtt_client
from Common import loadConfig


TOPIC = "tempture/device1"


client_id = f'python-mqtt-{random.randint(0, 100)}'



def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(host=loadConfig()['host']['ip'], port=loadConfig()['host']['port'])
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"接收到传感器的温度数据`{msg.payload.decode()}` 来自 `{msg.topic}` 主题")

    client.subscribe(TOPIC)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()

