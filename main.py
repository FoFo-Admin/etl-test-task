from application import create_csv, etl, queries
import configparser
import psycopg2

config = configparser.ConfigParser()
config.read('./config.ini')

CSV = config.get("CSV", "csv_file")
HOST = config.get("DATABASE", "host")
DATABASE = config.get("DATABASE", "database")
USERNAME = config.get("DATABASE", "username")
PASSWORD = config.get("DATABASE", "password")
PORT = config.get("DATABASE", "port")


if __name__ == '__main__':
    with psycopg2.connect(
            host=HOST,
            dbname=DATABASE,
            user=USERNAME,
            password=PASSWORD,
            port=PORT
    ) as db:
        with db.cursor() as cursor:
            menu = '-1'
            while menu != '0':
                menu = input("Select an option\n1 - Generate csv\n2 - Transform and load csv into database\n3 - Perform sql queries\n>>>")
                if menu == "1":
                    create_csv.generate()
                elif menu == "2":
                    etl.transform_and_load(CSV, cursor, db)
                elif menu == "3":
                    queries.execute(cursor, db)
