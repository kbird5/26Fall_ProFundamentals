# sensor_app_template.py - runs ON THE PC (regular Python 3, e.g. VS Code or IDLE)
# Template: talks to the board over USB serial and prints the readings.
# Rename a copy of this file (e.g. sensor_app.py) and extend it for the assignment.
#
# Setup: pip install pyserial
# IMPORTANT: close Thonny before running this, only one program can use the port.

import sqlite3
import time
from datetime import datetime

import serial

PORT = "/dev/cu.usbmodem101"
BAUD = 115200


def ask_board(ser, command):
    """Send a one-letter command to the board and return the number it replies with."""
    ser.reset_input_buffer()
    ser.write((command + "\n").encode())
    while True:
        line = ser.readline().decode(errors="ignore").strip()
        if line == "":
            raise TimeoutError("No reply from board")
        if line.startswith("DATA,"):
            return float(line.split(",")[2])


class DatabaseManager:
    """Create and manage a simple SQLite database for sensor readings."""

    def __init__(self, db_name="sensor_data.db"):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("DROP TABLE IF EXISTS SensorData")
        self.cur.execute(
            """
            CREATE TABLE SensorData (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                sensor_type TEXT NOT NULL,
                sensor_reading REAL NOT NULL
            )
            """
        )
        self.conn.commit()

    def log_reading(self, sensor_type, value):
        """Save one reading with the PC's current local date and time."""
        timestamp = datetime.now().isoformat(sep=" ", timespec="seconds")
        self.cur.execute(
            """INSERT INTO SensorData (timestamp, sensor_type, sensor_reading)
               VALUES (?, ?, ?)""",
            (timestamp, sensor_type, value),
        )
        self.conn.commit()

    def view_history(self):
        """Query and display every saved reading, oldest first."""
        records = self.cur.execute(
            """SELECT id, timestamp, sensor_type, sensor_reading
               FROM SensorData
               ORDER BY id"""
        ).fetchall()

        if not records:
            print("No readings have been logged yet.")
            return

        print("\nID | Timestamp | Sensor type | Reading")
        for record in records:
            record_id, timestamp, sensor_type, reading_value = record
            unit = "C" if sensor_type == "Temperature" else "%"
            print(f"{record_id} | {timestamp} | {sensor_type} | {reading_value:.1f} {unit}")

    def close(self):
        """Close the database connection."""
        self.conn.close()


def read_temperature(ser, database):
    """Request, display, and log temperature only when called."""
    temperature = ask_board(ser, "T")
    print(f"Temperature: {temperature:.1f} C")
    database.log_reading("Temperature", temperature)


def read_humidity(ser, database):
    """Request, display, and log humidity only when called."""
    humidity = ask_board(ser, "H")
    print(f"Humidity: {humidity:.1f} %")
    database.log_reading("Humidity", humidity)


def main():
    ser = serial.Serial(PORT, BAUD, timeout=3)
    time.sleep(2)
    ser.reset_input_buffer()
    database = DatabaseManager()

    print("Please choose from the following options:")
    print("T - Temperature")
    print("H - Humidity")
    print("0 - Both")
    print("V - View Log History")
    print("Q - Quit")

    try:
        while True:
            choice = input("\nEnter T, H, 0, V, or Q: ").strip().upper()
            if choice not in ("T", "H", "0", "V", "Q"):
                print("Invalid choice, please try again.")
                continue

            if choice == "T":
                read_temperature(ser, database)
            elif choice == "H":
                read_humidity(ser, database)
            elif choice == "0":
                read_temperature(ser, database)
                read_humidity(ser, database)
            elif choice == "V":
                database.view_history()
            elif choice == "Q":
                print("Program ended.")
                break
    except KeyboardInterrupt:
        print("\nProgram ended.")
    finally:
        database.close()
        ser.close()


if __name__ == "__main__":
    main()
