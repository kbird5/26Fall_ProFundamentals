# sensor_app_template.py - runs ON THE PC (regular Python 3, e.g. VS Code or IDLE)
# Template: talks to the board over USB serial and prints the readings.
# Rename a copy of this file (e.g. sensor_app.py) and extend it for the assignment.
#
# Setup: pip install pyserial
# IMPORTANT: close Thonny before running this, only one program can use the port.

import time
import serial                      # from the pyserial package

PORT = "/dev/cu.usbmodem101"                     # <-- CHANGE to your board's port (see Device Manager)
BAUD = 115200


def ask_board(ser, command):
    """Send a one-letter command to the board and return the number it replies with."""
    ser.reset_input_buffer()                  # discard any stale data
    ser.write((command + "\n").encode())      # send command + newline
    # Read lines until one starts with DATA (ignores any boot messages)
    while True:
        line = ser.readline().decode(errors="ignore").strip()
        if line == "":
            raise TimeoutError("No reply from board")
        if line.startswith("DATA,"):
            return float(line.split(",")[2])


# TODO 1: write the DatabaseManager class here (sqlite3).
import sqlite3

class DatabaseManager:
    def __init__(self, db_name = "sensor_data.db"):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.create_table()
   
    def create_table(self):
        self.cur.execute("DROP TABLE IF EXISTS SensorData")
        self.cur.execute("""
            CREATE TABLE SensorData
            (id             INT          NOT NULL,
             timestamp      TEXT         NOT NULL,
             sensor_type    VARCHAR(20)  NOT NUll,
             senosr_reading TEXT         NOT NULL,
             PRIMARY KEY (id))
        """)
        self.conn.commit()
    print("the table is ready")        

   
# TODO 2: write the temperature function here (ask the board with "T",
#         display the value, and log it to the database).

# TODO 3: write the humidity function here (ask the board with "H",
#         display the value, and log it to the database).


def main():
    # Open the serial port; opening it may reset the board, so wait a moment
    ser = serial.Serial(PORT, BAUD, timeout=3)
    time.sleep(2)
    ser.reset_input_buffer()

    # Demo only: read both sensors once and print them.
    # TODO 4: replace this with the menu and the user-choice loop.
    temperature = ask_board(ser, "T")
    humidity = ask_board(ser, "H")
    print(f"Temperature: {temperature:.1f} C")
    print(f"Humidity: {humidity:.1f} %")

    ser.close()


if __name__ == "__main__":
    main()
