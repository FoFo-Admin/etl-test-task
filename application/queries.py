def execute(cursor, db):
    for i in range(1, 5):
        try:
            cursor.execute(open(f"./application/sql/query_{i}.sql", "r").read())
            print(f"Results for query {i}\n")
            for res in cursor.fetchall():
                print(f"{res}\n")
            print("----------------------------------------\n\n")
        except Exception as e:
            print("Table doesn't exists")
            db.commit()
            return None

    cursor.execute(open(f"./application/sql/query_5.sql", "r").read())
    db.commit()
    cursor.execute("SELECT * FROM users")
    print(f"Results for query 5\n")
    for res in cursor.fetchall():
        print(f"{res}\n")
    print("----------------------------------------\n\n")
