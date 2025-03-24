import psutil
import serial
import time

# Настройте COM-порт в зависимости от вашей системы
arduino = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)  # Даем время на установку соединения

while True:
    battery = psutil.sensors_battery()
    if battery:
        percent = int(battery.percent)
        arduino.write(f"{percent}\n".encode())
        print(f"Отправлено: {percent}%")
    else:
        arduino.write("0\n".encode())
        print("Батарея не обнаружена")
    
    time.sleep(1)  # Обновляем каждую секунду