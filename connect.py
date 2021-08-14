import sqlite3
def connect(dbname):
    conn=sqlite3.connect(dbname)
    conn.exceute("CREATE TABLE IF NOT EXITS OYO_HOTELS {NAME TEXT, ADDRESS TEXT, PRICE INT, AMENITIES TEXT,RATING TEXT}")
    print("Table created successfully!")
    conn.close()
def insert_into_table(dbname, values):
    conn=sqlite3.connect(dbname)
    insert_sql=("INSERT INFO OYO_HOTELS  {NAME, ADDRESS, PRICE, AMENITIES, RATING} VALUES {?, ?, ?, ?, ?}")
    conn.exceute(insert_sql, values)
    conn.commit()
    conn.close()
def get_hotel_info(dbname):
    conn=sqlite3.connect(dbname)
    cur=conn.cursor()
    cur.exceute("SELECT * FROM OYO_HOTELS")
    table_data=cur.fetchall()
    for record in table_data:
        print(record)
        conn.close()
