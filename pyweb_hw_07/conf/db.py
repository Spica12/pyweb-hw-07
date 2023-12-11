import configparser
import pathlib

import psycopg2
from psycopg2.errors import DuplicateDatabase
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


def create_database():
    con = None
    try:
        # Connect to PostgresSQL DBMS
        con = psycopg2.connect(host=domain, port=port, user=user, password=password)
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        # Obtain a DB Cursor
        cursor = con.cursor()

        # Check if database exists
        cursor.execute(f"SELECT datname FROM pg_database WHERE datname = '{db}'")
        result = cursor.fetchone()

        if not result:
            # If the database does not exists, create it.
            sql_create_database = f"CREATE DATABASE {db}"
            print(f"Database {db} created.")
        else:
            print(f"Database {db} already exists.")
        cursor.execute(sql_create_database)

    except UnboundLocalError:
        pass

    except Exception as err:
        print(err)

    finally:
        if con:
            con.close()


def drop_database():
    con = None
    try:
        # Connect to PostgresSQL DBMS
        con = psycopg2.connect(host=domain, port=port, user=user, password=password)
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        # Obtain a DB Cursor
        cursor = con.cursor()

        # Check if database exists
        cursor.execute(f"SELECT datname FROM pg_database WHERE datname = '{db}'")
        result = cursor.fetchone()

        if result:
            # If the database exists, drop it.
            sql_create_database = f"DROP DATABASE {db}"
            print(f"Database {db} dropped.")
        else:
            print(f"Database {db} does not exist.")
        cursor.execute(sql_create_database)

    except UnboundLocalError:
        pass

    except Exception as err:
        print(err)

    finally:
        if con:
            con.close()


print("--- Postgres DB ---")

file_config = (
    pathlib.Path(__file__)
    .parent.parent.parent.joinpath("config")
    .joinpath("config.ini")
)
print(f"Config: {file_config}")

config = configparser.ConfigParser()
config.read(file_config)

user = config.get(section="DEV_DB", option="USER")
password = config.get(section="DEV_DB", option="PASSWORD")
domain = config.get(section="DEV_DB", option="DOMAIN")
port = config.get(section="DEV_DB", option="PORT")
db = config.get(section="DEV_DB", option="DB_NAME")


URI = f"postgresql://{user}:{password}@{domain}:{port}/{db}"
print(URI)

engine = create_engine(URI, echo=False, pool_size=5, max_overflow=0)
DBSession = sessionmaker(bind=engine)

session = DBSession()


if __name__ == "__main__":
    # drop_database()
    pass
