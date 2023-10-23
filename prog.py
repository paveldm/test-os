import time
import paho.mqtt.client as mqtt
import json
import xml.etree.ElementTree as ET


# Функция обработки сообщения
def on_message(client, userdata, msg):
    print(f"Received message: {msg.topic} {msg.payload.decode()}")
    # Добавление полученных данных в список
    data.append((msg.topic, msg.payload.decode()))


# Создание клиента MQTT
client = mqtt.Client()

# Установка функции обратного вызова для обработки сообщений
client.on_message = on_message

# Подключение к брокеру MQTT (в данном случае, Wirenboard)
broker_address = "192.168.1.15"
broker_port = 1883
client.connect(broker_address, broker_port)

# Подписка на топики датчиков
topics = [
    "/devices/wb-m1w2_14/controls/External Sensor 1",
    "/devices/wb-msw-v3_21/controls/Sound Level",
    "/devices/wb-msw-v3_21/controls/CO2",
    "/devices/wb-msw-v3_21/controls/Air Quality (VOC)"
]

for topic in topics:
    client.subscribe(topic)

# Инициализация списка для хранения данных
data = []

# Основной цикл
while True:
    client.loop(0.0)
    time.sleep(1)
    # Проверка, прошло ли 5 секунд
    if len(data) >= 5:
        # Формирование данных в формате JSON
        json_data = {}
        for i, (topic, payload) in enumerate(data):
            json_data[f"Sensor {i + 1}"] = payload
        json_data["Time"] = time.strftime("%Y-%m-%d %H:%M:%S")
        json_data["Number"] = 16
        with open("data.json", "w") as json_file:
            json.dump(json_data, json_file)

        # Формирование данных в формате XML
        root = ET.Element("Data")
        for i, (topic, payload) in enumerate(data):
            sensor = ET.SubElement(root, f"Sensor{i + 1}")
            sensor.text = payload
        time_ = ET.SubElement(root, "Time")
        time_.text = time.strftime("%Y-%m-%d %H:%M:%S")
        number = ET.SubElement(root, "Number")
        number.text = "16"

        tree = ET.ElementTree(root)
        tree.write("data.xml")

        # Очистка списка данных
        data = []