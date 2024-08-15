import pandas as pd
from email_validator import validate_email, EmailNotValidError
from datetime import date
from tqdm import tqdm


def check_email(email):
    try:
        validate_email(email, check_deliverability=False)
        return True
    except EmailNotValidError:
        return False


def transform_and_load(csv_path, cursor, db):
    df = pd.read_csv(csv_path)

    df["signup_date"] = df["signup_date"].apply(date.fromtimestamp)

    mask = df["email"].apply(check_email)
    df = df[mask]

    df["domain"] = df["email"].apply(lambda email: email.split("@")[-1])

    cursor.execute(open("./application/sql/create_table.sql", "r").read())
    cursor.execute("DELETE FROM users;")

    db.commit()

    insert_list = list(df.itertuples(index=False, name=None))
    for user in tqdm(insert_list):
        try:
            cursor.execute('INSERT INTO users (id, full_name, email, signup_date, domain) VALUES (%s, %s, %s, %s, %s)', user)
        except Exception as e:
            print(e)
        finally:
            db.commit()
