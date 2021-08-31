import sqlite3
connection = sqlite3.connect("projects.db")
cursor = connection.cursor()
cursor.execute("""
    CREATE TABLE owners
    (   ownerID INTEGER PRIMARY KEY, fname TEXT, lname TEXT, addr1 TEXT, addr2 TEXT, city TEXT, state TEXT, zip TEXT, 
        country TEXT, notes TEXT)
""")
cursor.execute("""
    CREATE TABLE dogs
    (   dogID INTEGER PRIMARY KEY, callName TEXT, registeredName TEXT, notes TEXT)
""")
cursor.execute("""
    CREATE TABLE owner_dogs
    (   ownerID INTEGER, dogID INTEGER, primaryOwner INTEGER,
            FOREIGN KEY(ownerID) REFERENCES owners(ownerID),FOREIGN KEY(dogID) REFERENCES dogs(dogID))
""")
cursor.execute("""
    CREATE TABLE procedures
    (   typeProc INTEGER, dogID INTEGER , addr2 TEXT, city TEXT, state TEXT, zip TEXT, country TEXT, notes TEXT,
            FOREIGN KEY(dogID) REFERENCES dogs(dogID))
""")
cursor.execute("""
    CREATE TABLE semen
    (   semenID INTEGER PRIMARY KEY, dogID Integer, quality1 INTEGER, quality2 INTEGER, abnormality1_present INTEGER,
        abnormality2_present INTEGER, abnormality3_present INTEGER, abnormality4_present INTEGER, notes TEXT,
            FOREIGN KEY(dogID) REFERENCES dogs(dogID))
""")
cursor.execute("""
    CREATE TABLE shipments
    (   shipmentID INTEGER PRIMARY KEY, semenID INTEGER, shipAddr1 TEXT, shipAddr2 TEXT, shipCity TEXT, shipState TEXT, 
        shipZip TEXT, shipCountry TEXT, notes TEXT)
""")
cursor.execute("""INSERT INTO projects VALUES 
    ('giraffes.io', 'Uber, but with giraffes', 1900),
    ('dronesweaters.com', 'Clothes for cold drones', 3000),
    ('hummingpro.io', 'Online humming courses', 120000)
""")
connection.commit()