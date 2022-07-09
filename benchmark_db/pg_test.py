import time
import psycopg2

conn = psycopg2.connect("host=localhost dbname=movies_database user=app password=123qwe")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS test_table (id INT, data TEXT)")
conn.commit()


def saving_data():
    start = time.time()
    for i in range(3000000):
        cur.execute("INSERT INTO test_table (id, data) VALUES (%(id)s,%(data)s)", {"id": i, "data": f'somedata_{i}'})
    conn.commit()
    return time.time() - start


def find_data():
    start = time.time()
    cur.execute(f"SELECT id, data FROM test_table WHERE id < 10000")
    data = cur.fetchall()
    for _ in data:
        continue
    return time.time() - start


if __name__ == '__main__':
    print(saving_data())
    print(find_data())
