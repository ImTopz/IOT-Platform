import time
import sys
import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))


    
def on_subscribe(client,userdata,mid,granted_qos):
    print("消息发送成功")
client = mqtt.Client(protocol=3)
client.username_pw_set("admin", "zd5201314..")
client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.connect(host="127.0.0.1", port = 1883, keepalive=60)  # 订阅频道
time.sleep(1)
i = 0
while True:
    try:
        # 发布MQTT信息
        sensor_data = "test" + str(i)
        client.publish(topic=f"mqtt/demo", payload=sensor_data, qos=0)
        time.sleep(5)
        i += 1
    except KeyboardInterrupt:
        print("EXIT")
        client.disconnect()
        sys.exit(0)
