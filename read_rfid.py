import serial

def read_rfid():
    try:
        ser = serial.Serial('COM3', 9600)  # Adjust COM port!
        print("Waiting for RFID...")
        rfid = ser.readline().decode().strip()
        ser.close()
        return rfid
    except Exception as e:
        print("Error:", e)
        return None

if __name__ == "__main__":
    rfid = read_rfid()
    if rfid:
        print("RFID Scanned:", rfid)
    else:
        print("No RFID detected.")
