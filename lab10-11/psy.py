import psycopg2
 
conn = psycopg2.connect(host="localhost", dbname="snake_game", user="postgres",
                        password="1234", port=5432)   
 
cur = conn.cursor()
 
conn.set_session(autocommit=True)

cur.execute("""CREATE TABLE if not exists snake(
            name VARCHAR(255),
            level INTEGER,
            score INTEGER
);
           """)
#conn.commit()