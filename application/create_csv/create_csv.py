import pandas as pd
import random


def generate(length=2000):
    names_list = []
    surnames_list = []
    words_list = []
    domains_list = []

    with open('./application/create_csv/names.txt', 'r') as names:
        names_list = names.read().split('\n')

    with open('./application/create_csv/surnames.txt', 'r') as surnames:
        surnames_list = surnames.read().split('\n')

    with open('./application/create_csv/wordlist.10000.txt', 'r') as words:
        words_list = words.read().split('\n')

    with open('./application/create_csv/domains.txt', 'r') as domains:
        domains_list = domains.read().split('\n')

    random_fullnames = [f"{random.choice(surnames_list)} {random.choice(names_list)}" for _ in range(length)]
    random_timestamp = [random.randint(1710000000, 1723660000) for _ in range(length)]

    random_emails = []
    for _ in range(length):
        email = ""
        email_len = random.randint(1, 3)
        actions = {
            "W": lambda: random.choice(words_list),
            "D": lambda: random.randint(1000, 9999),
            "P": lambda: '.'
        }
        for i in range(email_len):
            action = random.choices(["W", "D", "P"], [0.8, 0.191, 0.01])[0]
            email += str(actions[action]())
            if i != email_len-1 and random.randint(0, 1) == 1:
                email += "."
        email += f"@{random.choice(domains_list)}"
        random_emails.append(email)

    df = pd.DataFrame({
        "name": random_fullnames,
        "email": random_emails,
        "signup_date": random_timestamp
    })

    df.to_csv("./generated.csv", index_label="user_id")
