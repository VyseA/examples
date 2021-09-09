import mysql.connector

# Connect to the database and set a cursor
try:
    mydb_server = mysql.connector.connect(
      host="localhost",
      user="sa",
      password="zqVH5^TXg*Ntore!Z8Xb#pYe89oFLFp#"
    )
    cursor = mydb_server.cursor(buffered=True, dictionary=True)
except:
    print("Failed to connect to server")
    exit(0)

# Check to see if the database is already present
# If database is not on local MySQL instance, then create it
cursor.execute("SHOW DATABASES")
db_isPresent = False
for item in cursor:
    if item['Database'] == "rowdyrumbles":
        db_isPresent = True

if db_isPresent:
    print("Database already present--skipping process")
else:
    cursor.execute("CREATE DATABASE rowdyrumbles")

# Try to create each of the tables
# If they already exist, then meh
try:
    cursor.execute("""
        CREATE TABLE rowdyrumbles.owners
        (   ownerID INTEGER PRIMARY KEY, fname TEXT, lname TEXT, addr1 TEXT, addr2 TEXT, city TEXT, state TEXT, zip TEXT,
            country TEXT, phone INTEGER, email TEXT, notes TEXT)
    """)
except:
    print("Table 'owners' failed to create.  Either it already exists, or there was an error.")
try:
    cursor.execute("""
        CREATE TABLE rowdyrumbles.animals
        (   animalID INTEGER PRIMARY KEY, speciesID INTEGER, speciesSubID INTEGER, callName TEXT, 
            registryID INTEGER, weight INTEGER, weightDate Date, registeredName TEXT, notes TEXT)
    """)
except:
    print("Table 'animals' failed to create.  Either it already exists, or there was an error.")
try:
    cursor.execute("""
        CREATE TABLE rowdyrumbles.owner_animals
        (   ownerID INTEGER, animalID INTEGER, primaryOwner INTEGER,
                FOREIGN KEY(ownerID) REFERENCES owners(ownerID),FOREIGN KEY(animalID) REFERENCES animals(animalID))
    """)
except:
    print("Table 'owner_animals' failed to create.  Either it already exists, or there was an error.")
try:
    cursor.execute("""
        CREATE TABLE procedures
        (   typeProc INTEGER, animalID INTEGER , addr2 TEXT, city TEXT, state TEXT, zip TEXT, country TEXT, notes TEXT,
                FOREIGN KEY(dogID) REFERENCES dogs(dogID))
    """)
except:
    print("Table 'procedures' failed to create.  Either it already exists, or there was an error.")
try:
    cursor.execute("""
        CREATE TABLE rowdyrumbles.semen
        (   semenID INTEGER PRIMARY KEY, dogID Integer, quality1 INTEGER, quality2 INTEGER, abnormality1_present INTEGER,
            abnormality2_present INTEGER, abnormality3_present INTEGER, abnormality4_present INTEGER, notes TEXT,
                FOREIGN KEY(dogID) REFERENCES dogs(dogID))
    """)
except:
    print("Table 'semen' failed to create.  Either it already exists, or there was an error.")
try:
    cursor.execute("""
        CREATE TABLE rowdyrumbles.shipments
        (   shipmentID INTEGER PRIMARY KEY, semenID INTEGER, shipAddr1 TEXT, shipAddr2 TEXT, shipCity TEXT, shipState TEXT,
            shipZip TEXT, shipCountry TEXT, notes TEXT)
    """)
except:
    print("Table 'shipments' failed to create.  Either it already exists, or there was an error.")
mydb_server.commit()

cursor.close()
mydb_server.close()