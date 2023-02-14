import random
from paho.mqtt import client as mqtt_client


# port = 1883
topic = "mqtt/demo"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)


    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(host='127.0.0.1', port=1883)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt() #生成一个client对象
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()

