import os
import pandas as pd
from time import sleep
import psycopg2


def connection_db():
    for i in range(int(os.environ["MAX_RECONNECT_ITER"])):
        try:
            conn = psycopg2.connect(
                dbname=os.environ["POSTGRES_DB"],
                user=os.environ["POSTGRES_USER"],
                password=os.environ["POSTGRES_PASSWORD"],
                host="localhost",
                port=int(os.environ["POSTGRES_PORT"])
            )
            break
        except:
            sleep(float(os.environ["RECONNECT_SLEEP_TIME"]))
    else:
        raise TimeoutError("Couldn't connect to postgres database at this port!")
    return conn

def create_table(table, data):
    conn = connection_db()
    cur = conn.cursor()
    cur.execute(f'CREATE TABLE IF NOT EXISTS "{table}" ({data.columns[0]} VARCHAR(255), {data.columns[1]} FLOAT)')
    conn.commit()
    conn.close()

def insert(table, value_1, value_2):
    conn = connection_db()
    cur = conn.cursor()
    cur.execute(f"INSERT INTO {table} VALUES('%s','%s')" % (value_1, value_2))
    conn.commit()
    conn.close()

def check_fill(table):
    conn = connection_db()
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table}")
    rows = cur.fetchall()
    if rows:
        print('Database is filled')
    else:
        print('Databased is not filled')

def main():
    df = pd.read_csv(os.environ["DATA_PATH"])
    table_name = os.environ['TABLE_NAME']
    create_table(table_name, df)
    for _, row in df.iterrows():
        insert(table_name, row[df.columns[0]], row[df.columns[1]])
    check_fill(table_name)

if __name__ == "__main__":
    main()
