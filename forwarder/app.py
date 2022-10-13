import os
import awsiot.greengrasscoreipc
import awsiot.greengrasscoreipc.client as client
import awsiot.greengrasscoreipc.model as model
import json
import paho.mqtt.client as mqtt

print(os.environ)

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("application/+/device/+/event/up")

def on_message(client, userdata, msg):
  # @TODO add DevEUI to topic
  topic = "{}/up".format(os.environ["AWS_IOT_THING_NAME"])
  data = json.loads(str(msg.payload.decode("utf-8")))
  print(data['object'])
  # print(payload['rxInfo']['gatewayId'])
  # print(payload['deviceInfo']['devEui'])
  payload = json.dumps({
    # "GatewayEui": payload['rxInfo']['gatewayId'],
    # "DevEui": payload['deviceInfo']['devEui'],
    "Payload": data['object']
  }).encode()

  ipc_client = awsiot.greengrasscoreipc.connect()

  publish_operation = ipc_client.new_publish_to_iot_core()

  print(payload)
  publish_operation.activate(
    request = model.PublishToIoTCoreRequest(
      topic_name = topic,
      qos = model.QOS.AT_MOST_ONCE,
      payload = payload
    )
  )
  print('pub success')

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mosquitto", 1883, 60)

client.loop_forever()