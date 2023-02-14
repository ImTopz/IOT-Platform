# coding = utf-8
import time
import sys
import random
import json
import paho.mqtt.client as mqtt
from Common import loadConfig


def on_connect(client, userdata, flags, rc):
    print("设备成功连接,状态码为" + str(rc))



    
def on_subscribe(client,userdata,mid,granted_qos):
    print("节点成功订阅")


def sendMsg(client):
    tempture = random.randint(-10,20)
    sensor_data = ' "time" : {} , "tempture" : {} '.format(str(time.time()),str(tempture))
    data = '{' + str(sensor_data) + '}'
    data = json.loads(data)
    client.publish(topic=f'tempture/device1',payload=str(data),qos=1)
    print("数据推送成功")
    time.sleep(5)


if __name__ == '__main__':

    client = mqtt.Client()
    client.username_pw_set(loadConfig()['user']['username'], loadConfig()['user']['password'])
    client.on_connect = on_connect
    client.on_subscribe = on_subscribe
    client.connect(host=loadConfig()['host']['ip'], port = loadConfig()['host']['port'], keepalive=60)  # 订阅频道
    time.sleep(1)

    i = 0

    while True:

        try:
            sendMsg(client)

        except KeyboardInterrupt:
            print("连接异常，断开连接")
            client.disconnect()
            sys.exit(0)
