import os

import mariadb
from dotenv import load_dotenv


# Converting array to dictionary
def convert_array(keys, values):
    dictionary = {keys[i]: values[i] for i in range(len(keys))}
    return dictionary


# Create the required database
def create_database(db_engine):
    sql_statement = "CREATE DATABASE IF NOT EXISTS users_information"
    db_engine["db_cursor"].execute(sql_statement)
    print("DATABASE CREATED")


# Create the required table for registered_users
def create_registered_users_table(db_engine):
    sql_statement = ("CREATE TABLE IF NOT EXISTS registered_users "
                     "(id INT NOT NULL AUTO_INCREMENT, "
                     "username VARCHAR(100) NOT NULL,"
                     "hashed_password VARCHAR(100) NOT NULL,"
                     "enabled TINYINT NOT NULL,"
                     "PRIMARY KEY(id))")
    db_engine["db_cursor"].execute(sql_statement)
    print("REGISTERED USERS TABLE CREATED")


# Add new user into the registered_users table
def register_user(db_engine, username: str, hashed_password: str):
    sql_statement = (f"INSERT INTO registered_users (username, hashed_password, enabled) "
                     f"VALUES (%s,%s,%s)")
    db_engine["db_cursor"].execute(sql_statement, (username, hashed_password, 1))
    db_engine["db_connection"].commit()
    return_statement = username + " has been registered"
    return return_statement


# Get a specific user in the registered_users table
def get_registered_user(db_engine, username: str):
    sql_statement = (f"SELECT username, hashed_password, enabled "
                     f"from registered_users where username=%s")
    columns = ["username", "hashed_password", "enabled"]
    db_engine["db_cursor"].execute(sql_statement, (username, ))
    registered_user = db_engine["db_cursor"].fetchone()
    registered_user_dict = convert_array(columns, registered_user)
    return registered_user_dict


# Load the .env file
def configure():
    load_dotenv()


# Initialize the database
def init_db():
    configure()
    try:
        conn = mariadb.connect(
            user=os.environ.get("USER", "root"),
            password=os.environ.get("PASSWORD", "admin"),
            host=os.environ.get("HOST", "127.0.0.1"),
            database=os.environ.get("DATABASE", "users_information")
        )
        db_cursor = conn.cursor()
        db_engine = {"db_connection": conn, "db_cursor": db_cursor}
        return db_engine
    except mariadb.Error as e:
        print(f"Error: {e}")
