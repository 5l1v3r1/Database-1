import sqlite3 ##Dahil Et

db =sqlite3.connect("test.am") ##Bağladık.

imlec = db.cursor()
imlec.execute("CREATE TABLE if not exists kitaplik (kitap,yazar,yayinevi,baskisayisi)")
imlec.execute("INSERT INTO 'kitaplik' VALUES ('İnce Mehmet','Yaşar Kemal','Ai Kitap Evi','10000')")
db.commit() ##Database işlemek için..

db.close()## Kapattık.
