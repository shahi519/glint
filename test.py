import pyodbc
# print(pyodbc.drivers())

# Replace with your connection details
server = '192.168.1.54'  # IP address of your SQL Server
database = 'jewelsam'  # Name of your database
username = 'krish'  # SQL Server username
password = 'krish123'  # SQL Server password
port = 1433  # Default port for SQL Server; change if needed

# Connection string
connection_string = (
    f'DRIVER={{ODBC Driver 18 for SQL Server}};'
    f'SERVER={server},{port};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password}'
)

try:
    # Establish connection
    connection = pyodbc.connect(connection_string)
    print("Connection to SQL Server successful!")

    # Create a cursor object using the connection
    cursor = connection.cursor()

    # Test query to check if we can fetch data
    cursor.execute("SELECT TOP 1 * FROM YourTableName")  # Replace 'YourTableName' with an actual table name
    row = cursor.fetchone()
    print("Sample Data:", row)

    # Close the connection
    connection.close()

except Exception as e:
    print("Error connecting to SQL Server:", e)
