from dotenv import load_dotenv, dotenv_values
import os
import mariadb


def create_database(db_cursor):
    sql_statement = "CREATE DATABASE IF NOT EXISTS users_information"
    db_cursor.execute(sql_statement)
    print("DATABASE CREATED")


def create_registered_users_table(db_cursor):
    sql_statement = ("CREATE TABLE IF NOT EXISTS registered_users "
                     "(id INT NOT NULL AUTO_INCREMENT, "
                     "username VARCHAR(100) NOT NULL,"
                     "hashed_password VARCHAR(100) NOT NULL,"
                     "enabled TINYINT NOT NULL,"
                     "PRIMARY KEY(id))")
    db_cursor.execute(sql_statement)
    print("REGISTERED USERS TABLE CREATED")


def register_user(db_cursor, username: str, hashed_password: str):
    sql_statement = (f"INSERT INTO registered_users (username, hashed_password, enabled) "
                     f"VALUES ('{username}', '{hashed_password}', '{1}')")
    db_cursor.execute(sql_statement)


def get_registered_user(db_cursor, username: str):
    sql_statement = (f"SELECT username, hashed_password, enabled "
                     f"from registered_users where username={username}")
    return db_cursor.execute(sql_statement)


def configure():
    load_dotenv()


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
        return db_cursor
    except mariadb.Error as e:
        print(f"Error: {e}")


#cursor = init_db()
#register_user(cursor, "admin", "$2b$12$NKg.483CpDHY1mis.tyKRe.bxTfUvrBea1SEFHeQAjDr7wcufSDYa")
#register_user(cursor, "user", "pass")
