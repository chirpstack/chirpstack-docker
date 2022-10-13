import os
# import awsiot.greengrasscoreipc
# import awsiot.greengrasscoreipc.client as client
# import awsiot.greengrasscoreipc.model as model
import json
import paho.mqtt.client as mqtt

# ipc_client = awsiot.greengrasscoreipc.connect()

print(os.environ)

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("application/+/device/+/event/up")

def on_message(client, userdata, msg):
  payload = json.loads(str(msg.payload.decode("utf-8")))
  print(payload['object'])
  message = {
    payload: payload['object']
  }
  print(message)
  # publish_operation = ipc_client.new_publish_to_iot_core()
  # publish_operation.activate(
  #   request = model.PublishToIoTCoreRequest(
  #     topic_name = 'MCT/PY/FD',
  #     qos = model.QOS.AT_MOST_ONCE,
  #     payload = json.dumps(message).encode()
  #   )
  # )

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mosquitto", 1883, 60)

client.loop_forever()