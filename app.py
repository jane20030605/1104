import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM customer")
data = cursor.fetchall()
for rec in data:
    print(f"ID：{rec[0]}, Name：{rec[1]}, Tel：{rec[2]}, Addr：{rec[3]}")

cursor.execute("INSERT INTO customer(cid, cname, ctel, cadd) VALUES (?, ?, ?, ?)", ('c004', 'Cathy', '0937-543889', 'Tainan City daye road'))
conn.commit()

cursor.close()
conn.close()