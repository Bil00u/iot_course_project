import sqlite3
import paho.mqtt.client as mqtt

# my MQTT broker information
broker_address = "172.20.10.4"
broker_port = 1883
mqtt_topic = "sensor/light"

# SQLite database file path
db_file = "light_data.db"

# Callback function for receveing MQTT messages
def on_message(client, userdata, message):
    # Extracting the payload (light value) from the MQTT message
    light_value = float(message.payload.decode())
    
    # Storing the light value in the SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    # Creating the table if it doesn't exist
    cursor.execute("CREATE TABLE IF NOT EXISTS light_data (timestamp INTEGER, value REAL)")
    
    # Inserting the light value into the table along with the current timestamp
    cursor.execute("INSERT INTO light_data (timestamp, value) VALUES (strftime('%s','now'), ?)", (light_value,))
    
    # Committing the changes and closing the database connection
    conn.commit()
    conn.close()

# Creating an MQTT client and setting the message callback function
client = mqtt.Client()
client.on_message = on_message

# Connecting to the MQTT broker and subscribing to the topic
client.connect(broker_address, broker_port)
client.subscribe(mqtt_topic)

# Starting the MQTT loop to handle incoming messages
client.loop_start()

