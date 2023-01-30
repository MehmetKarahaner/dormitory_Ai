import sqlite3
conn = sqlite3.connect("yurtmu_evmi_database.db")
cursor = conn.cursor()

cursor.execute(""" CREATE TABLE ogrenciler(
kurallara_uyum INTEGER,
sorumluluk_sevme INTEGER,
ozel_alana_duskunluk INTEGER,
gelir INTEGER,
yurt_ev TEXT)
""")

cursor.execute(""" CREATE TABLE oranlar(
kural_uyum_oran REAL,
sorumluluk_sevme_oran REAL)
""")

cursor.execute(""" CREATE TABLE sebepler(
yurt_ev TEXT,
neden_digerinde_kalamiyor TEXT)
""")

cursor.execute(""" CREATE TABLE kullanicilar(
kullanici_adi TEXT,
sifre TEXT)
""")

cursor.execute("INSERT INTO kullanicilar VALUES ('guest','123')")

cursor.execute("INSERT INTO oranlar VALUES ('5','-5')")


conn.commit()
conn.close()
