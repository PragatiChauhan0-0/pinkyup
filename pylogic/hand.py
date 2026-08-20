import serial
import time

arduino = serial.Serial('COM7', 9600) 
time.sleep(2)  # wait for the serial connection to initialize

previous = None  # Initialize previous to None to ensure the first count is sent

def send_finger_count(fingers):
    global previous 
    count = sum(fingers)  # Calculate the sum of the fingers list
    if count != previous:  # Only send if the count has changed
        arduino.write(str(count).encode())  # Send the count to Arduino as a string
        previous = count
        print(f"Sent {count} to Arduino")  # Print the sent value for debugging


def close_connection():
    arduino.close()  # Close the serial connection

