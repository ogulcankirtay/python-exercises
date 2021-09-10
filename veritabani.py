import sqlite3
baglanti=sqlite3.connect("database.db")
imlec=baglanti.cursor()
'''
imlec.execute("CREATE TABLE IF NOT EXISTS ekip(isim TEXT,yaş INT,cinsiet TEXT)")
imlec.execute("INSERT INTO ekip VALUES('oğulcan',22,'erkek')")
imlec.execute("INSERT INTO ekip VALUES('eva',21,'kız')")
imlec.execute("INSERT INTO ekip VALUES('emir',19,'erkek')")
imlec.execute("INSERT INTO ekip VALUES('ecrin',23,'kız')")

'''

imlec.execute("SELECT * FROM ekip")
for veri in imlec.fetchall():
    print(veri)
imlec.execute("UPDATE ekip SET yaş=20 WHERE isim='ecrin'")
imlec.execute("DELETE FROM ekip WHERE isim='oğulcan'")
baglanti.commit()
baglanti.close()