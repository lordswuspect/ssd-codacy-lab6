import os
import sqlite3
import secrets   # Fix 3: using secrets instead of random

# Fix 1: Hardcoded password removed, using environment variable
DB_PASSWORD = os.environ.get('DB_PASSWORD')

def get_user(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Fix 2: SQL Injection vulnerability fixed with parameterized query
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    
    return cursor.fetchall()

def generate_token():
    # Fix 3: Insecure random replaced with secrets module
    return str(secrets.randbelow(900000) + 100000)

# Fix 4: Unused variable removed (completely deleted the line)
# (No unused_count = 42 present)

print(get_user('admin'))
print(generate_token())
