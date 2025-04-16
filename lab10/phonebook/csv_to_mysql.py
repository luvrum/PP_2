import psycopg2, tools
import pandas as pd
connection = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="root",
    port=5432
)


data = pd.read_csv(r"lab10/phonebook/data.csv")
df = pd.DataFrame(data)
# print(df)

cursor = connection.cursor()

for row in df.itertuples():
    print(row.phone_number," ", row.name)
    cursor.execute(
        """
        INSERT INTO phone_book (phone_number, name, surname)
        VALUES (%s, %s, %s)
        """,
        [row.phone_number,
        row.name,
        row.surname]
    )
connection.commit()
