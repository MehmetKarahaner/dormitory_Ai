from tkinter import *
from tkinter import messagebox
import sqlite3
import karar_algoritmasi

giris = Tk()
giris.title("Giriş Sayfası")
giris.geometry("400x400")


def giris_yap():
    connection = sqlite3.connect("yurtmu_evmi_database.db")
    my_cursor = connection.cursor()
    my_cursor.execute("SELECT kullanici_adi FROM kullanicilar")
    adi = my_cursor.fetchone()
    my_cursor.execute("SELECT sifre FROM kullanicilar")
    sifre = my_cursor.fetchone()

    connection.commit()
    connection.close()

    if kAdi_entry.get() == adi[0] and kSifre_entry.get() == sifre[0]:
        messagebox.showinfo("BAŞARILI", "Giriş başarılı")
        master = Tk()
        master.title("ANA SAYFA")
        master.geometry("400x400")
        giris.destroy()

        def tahmin_yap():
            tahmin = Tk()
            tahmin.title("Bilgi gir.")
            tahmin.geometry("400x400")

            def onayla():
                sonuc = karar_algoritmasi.karar_ver(int(entry1.get()), int(entry2.get()), int(entry4.get()))
                oda_arkadasi = str(karar_algoritmasi.kisiye_karar_ver(int(entry3.get()), int(entry4.get())))
                if sonuc:
                    messagebox.showinfo("SONUÇ", ("Yurtta kalmalısınız. Oda arkadaşı sayınız şu kadar olmalı: "
                                                  ""+oda_arkadasi))
                else:
                    messagebox.showinfo("SONUÇ", ("Evde kalmalısınız. Oda arkadaşı sayınız şu kadar olmalı: "
                                                  ""+oda_arkadasi))

            label1 = Label(tahmin, text="Kurallara uyum oranınızı yazınız (0/5 arası): ")
            label2 = Label(tahmin, text="Sorumluluk sevme oranınızı yazınız (0/5 arası): ")
            label3 = Label(tahmin, text="Özel alana duskunluk oranını yazınız (0/5 arası): ")
            label4 = Label(tahmin, text="Gelir miktarınızı yazınız (3200 gibi): ")
            entry1 = Entry(tahmin)
            entry2 = Entry(tahmin)
            entry3 = Entry(tahmin)
            entry4 = Entry(tahmin)
            onayla_buton = Button(tahmin, text="ONAYLA", command=onayla)

            label1.grid(row=0, column=0)
            entry1.grid(row=0, column=1)
            label2.grid(row=1, column=0)
            entry2.grid(row=1, column=1)
            label3.grid(row=2, column=0)
            entry3.grid(row=2, column=1)
            label4.grid(row=3, column=0)
            entry4.grid(row=3, column=1)
            onayla_buton.grid(row=4, column=1)

            tahmin.mainloop()

        def veri_gir():
            if messagebox.askokcancel("LÜTFEN OKUYUN.", "Kaldığınız yerde mutsuzsanız lütfen CANCEL'ı tıklayınız."):
                veri = Tk()
                veri.title("Bilgi gir.")
                veri.geometry("400x400")

                def onayla():

                    conn = sqlite3.connect("yurtmu_evmi_database.db")
                    cursor = conn.cursor()
                    cursor.execute("INSERT INTO ogrenciler (kurallara_uyum,sorumluluk_sevme,ozel_alana_duskunluk,"
                                   "gelir,yurt_ev) VALUES (?,?,?,?,?)", (int(entry1.get()),
                                                                         int(entry2.get()), int(entry3.get()),
                                                                         int(entry4.get()), entry5.get()))
                    sonuc = True
                    if entry5.get() == "ev":
                        sonuc = False

                    conn.commit()
                    conn.close()
                    karar_algoritmasi.karar_ver(int(entry1.get()), int(entry2.get()), int(entry4.get()), sonuc)
                    messagebox.showinfo("BAŞARILI.", "Bilgileriniz kaydedilmiştir. Teşekkürler.")
                    veri.destroy()

                label1 = Label(veri, text="Kurallara uyum oranınızı yazınız (0/5 arası): ")
                label2 = Label(veri, text="Sorumluluk sevme oranınızı yazınız (0/5 arası): ")
                label3 = Label(veri, text="Özel alana duskunluk oranını yazınız (0/5 arası): ")
                label4 = Label(veri, text="Gelir miktarınızı yazınız (3200 gibi): ")
                label5 = Label(veri, text="Kaldığınız yeri yazınız (yurt yada ev diye): ")
                entry1 = Entry(veri)
                entry2 = Entry(veri)
                entry3 = Entry(veri)
                entry4 = Entry(veri)
                entry5 = Entry(veri)
                onayla_buton = Button(veri, text="ONAYLA", command=onayla)

                label1.grid(row=0, column=0)
                entry1.grid(row=0, column=1)
                label2.grid(row=1, column=0)
                entry2.grid(row=1, column=1)
                label3.grid(row=2, column=0)
                entry3.grid(row=2, column=1)
                label4.grid(row=3, column=0)
                entry4.grid(row=3, column=1)
                label5.grid(row=4, column=0)
                entry5.grid(row=4, column=1)
                onayla_buton.grid(row=5, column=1)

                veri.mainloop()
            else:
                veri = Tk()
                veri.title("Bilgi gir.")
                veri.geometry("400x400")

                def onayla():
                    conn = sqlite3.connect("yurtmu_evmi_database.db")
                    cursor = conn.cursor()
                    cursor.execute("INSERT INTO sebepler (yurt_ev,neden_digerinde_kalamiyor) VALUES (?,?)",
                                   (entry2.get(), entry1.get()))
                    messagebox.showinfo("BAŞARILI.", "Bilgileriniz kaydedilmiştir. Teşekkürler.")
                    conn.commit()
                    conn.close()
                    veri.destroy()

                label1 = Label(veri, text="Neden sevmediğinizi yazınız.")
                label2 = Label(veri, text="Şu anda kaldığınız yeri yazınız.")
                entry1 = Entry(veri)
                entry2 = Entry(veri)
                onayla_buton = Button(veri, text="ONAYLA", command=onayla)

                label1.grid(row=0, column=0)
                entry1.grid(row=0, column=1)
                label2.grid(row=1, column=0)
                entry2.grid(row=1, column=1)
                onayla_buton.grid(row=2, column=1)

                veri.mainloop()

        giris_label = Label(master, text="HOŞGELDİNİZ", font=("Arial", 24))
        veri_gir_buton = Button(master, text="Yurtta veya öğrenci evinde kalıyorum.", command=veri_gir)
        tahmin_buton = Button(master, text="Nerde kalman gerektiğini öğren.", command=tahmin_yap)

        def bilgilendir():
            bilgi = Tk()
            bilgi.title("BİLGİ SAYFASI")
            bilgi.geometry("400x400")

            bilgi_baslik_label = Label(bilgi, text="BİLGİ SAYFASI", font=("Arial", 24), borderwidth=1)
            bilgi_label = Label(bilgi, text="Amaç: Bu program insanların karakteristik özelliklerine\n"
                                            "göre yurtta veya evde kalmalarını öneren programdır.   \n"
                                            "Ayrıca yurtta veya evde kalan insanların verilerini    \n"
                                            "girmeleriyle algoritma daha da iyi çalışır yani;       \n"
                                            "Program size daha iyi öneriler verir.                  \n\n\n"
                                            "Yapan: Mehmet Karahaner", font=("Arial", 12))

            bilgi_baslik_label.grid(row=0, padx=10)
            bilgi_label.grid(row=1, sticky=W)
            bilgi.mainloop()

        bilgi_menusu = Menu(master)
        master.config(menu=bilgi_menusu)
        bilgi_menu = Menu(bilgi_menusu)
        bilgi_menusu.add_cascade(label="Bilgilendir", menu=bilgi_menu)
        bilgi_menu.add_command(label="Bilgi sayfasını aç", command=bilgilendir)

        giris_label.grid(row=0, padx=75, pady=10, sticky=W)
        veri_gir_buton.grid(row=1, padx=80, pady=20, sticky=W)
        tahmin_buton.grid(row=2, padx=95, sticky=W)

        master.mainloop()

    else:
        messagebox.showerror("Başarısız.", "Giriş başarısız tekrar dene.")


karsilama_label = Label(giris, text="Lütfen giriş yapınız", font=("Arial", 16))
kAdi_label = Label(giris, text="Kullanıcı adını giriniz: ")
kSifre_label = Label(giris, text="Kullanıcı şifrenizi giriniz: ")
guest_label = Label(giris, text="MİSAFİRSENİZ: (kullanıcı adı:guest şifre: 123)")
giris_yap_buton = Button(giris, text="Giriş yap", command=giris_yap)

kAdi_entry = Entry(giris)
kSifre_entry = Entry(giris)

karsilama_label.grid(row=0, pady=10)
kAdi_label.grid(row=1, column=0, sticky=W)
kAdi_entry.grid(row=1, column=1, sticky=W)
kSifre_label.grid(row=2, column=0, sticky=W)
kSifre_entry.grid(row=2, column=1)
guest_label.grid(row=3, column=0, sticky=W)
giris_yap_buton.grid(row=3, column=1, sticky=E)

giris.mainloop()
