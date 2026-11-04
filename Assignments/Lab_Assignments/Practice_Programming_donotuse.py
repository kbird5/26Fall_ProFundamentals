#1) When the program starts, display this menu on the Serial Monitor: Please choose from the following options: T - Temperature H- Humidity O- Both V - View Log History


#2) setting up the database sensor_data.db that includes ID, timestamp, senosr type and sensor reading value
import sqlite3
conn = sqlite3.connect("sensor_data.db")
cur = conn.cursor()

#removing old table so things can rerun
cur.execute("DROP TABLE IF EXISTS SensorData")
#creating the table
cur.execute("""
    CREATE TABLE SensorData
    (id             INT          NOT NULL,
     timestamp      TEXT         NOT NULL,
     sensor_type    VARCHAR(20)  NOT NUll,
     senosr_reading TEXT         NOT NULL,
     PRIMARY KEY (id))
""")
conn.commit()
print("the table is ready")

data = [
    (1, "11:03am", 'temperature', 67),
    (2, "11:03am", 'humidity', 15),
    (3, "11:05am", 'temperature', 73),
    (4, "11:05am", 'humidity', 12),
    (5, "11:10am", 'temperature', 75),
    (6, "11:10am", 'humidity', 20),
]
cur.executemany("INSERT INTO SensorData VALUES (?, ?, ?, ?)", data)
conn.commit()
print ("6 data values added")
