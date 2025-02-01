import mysql.connector

# Database configuration
HOST = "localhost"
USER = "root"
PASSWORD = "20Eve,lyne#76"  # Change if you have a MySQL password

try:
    # Connect to MySQL server
    conn = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD
    )
    
    # Create a cursor object
    cursor = conn.cursor()
    
    # Create database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    
    print("Database 'alx_book_store' created successfully! ✅")

except mysql.connector.Error as err:
    print(f"Error: {err} ❌")

finally:
    # Close cursor and connection
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
