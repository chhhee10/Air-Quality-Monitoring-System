import serial
import csv
import re
from datetime import datetime

# configure serial
ser = serial.Serial('COM3', 115200)

file_name = "dataset/raw/master_log.csv"
print(f"Appending to {file_name}")

# open file for appending
with open(file_name, 'a', newline='') as f:
    writer = csv.writer(f)

    # write header only if file is empty
    if f.tell() == 0:
        writer.writerow(["timestamp", "mq135_raw", "temperature", "humidity", "aqi_category"])

    while True:
        try:
            line = ser.readline().decode().strip()
            print(line)

            match = re.search(r"MQ135:\s*(\d+).*Temp:\s*([\d.]+).*Hum:\s*([\d.]+).*=>\s*(\w+)", line)

            if match:
                timestamp = datetime.now()
                mq = match.group(1)
                temp = match.group(2)
                hum = match.group(3)
                aqi = match.group(4)

                writer.writerow([timestamp, mq, temp, hum, aqi])
                f.flush()

        except KeyboardInterrupt:
            print("Stopped.")
            break
