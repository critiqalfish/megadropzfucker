import sqlite3

db = sqlite3.connect('database.db')
cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS links (
                ilink text,
                olink text
            )""")
db.commit()
cursor.execute("CREATE UNIQUE INDEX IF NOT EXISTS xlink ON links (olink)")
db.commit()

ilink = 'https://link-hub.net/156589/523488'

with db:
    cursor.execute("SELECT olink FROM links WHERE ilink=?", (ilink,))
    dlinks = cursor.fetchall()

if dlinks == []:
    print('empty')
else:
    for link in dlinks:
        print(link[0])

db.close()