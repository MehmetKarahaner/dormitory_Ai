from math import pow  # Kural ve sorumluluk 5 üzerinden
import sqlite3

# Bu algoritmanın düzgün çalışması için veri eklenirken kişinini isteyerek kalması gerek


def karar_ver(kural, sorumluluk, gelir, sonuc=None):  # Yurtta kalıyor ise True evde kalıyor ise False gelicek.
    conn = sqlite3.connect("yurtmu_evmi_database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM oranlar")
    oranlar = cursor.fetchone()

    sorumluluk_orani = oranlar[0]
    kural_uyum_oran = oranlar[1]

    cursor.execute("SELECT COUNT(yurt_ev) FROM ogrenciler GROUP BY yurt_ev ORDER BY yurt_ev")
    kisi_sayilari = cursor.fetchall()
    try:
        yurt_secenler = 1 + (2 * kisi_sayilari[1][0])
        ev_secenler = 1 + (2 * kisi_sayilari[0][0])
    except:
        yurt_secenler = 1
        ev_secenler = 1

    veri_sayi_carpani = 0.5  # 0-1 arasında. Bu çarpanı az verirseniz her 1 verinin oranları değiştirme oranı artar.

    if sonuc is not None:

        kural_etkisi = (kural - 2.5) * 2
        sorumluluk_etkisi = (sorumluluk - 2.5) * 2

        if kural_etkisi < 0:
            kural_etkisi *= -1
        if sorumluluk_etkisi < 0:
            sorumluluk_etkisi *= -1

        if sonuc:
            if kural_etkisi > sorumluluk_etkisi:
                kural_uyum_oran += kural_etkisi * (1 / pow(yurt_secenler, veri_sayi_carpani))
            elif sorumluluk_etkisi > kural_etkisi:
                sorumluluk_orani += sorumluluk_etkisi * (1 / pow(yurt_secenler, veri_sayi_carpani))
            else:
                sorumluluk_orani += sorumluluk_etkisi * (1 / pow(yurt_secenler, veri_sayi_carpani))
                kural_uyum_oran += kural_etkisi * (1 / pow(yurt_secenler, veri_sayi_carpani))

            cursor.execute("UPDATE oranlar SET kural_uyum_oran = ? ,sorumluluk_sevme_oran = ? WHERE rowid = 1",
                           (kural_uyum_oran, sorumluluk_orani))

        else:
            if kural_etkisi > sorumluluk_etkisi:
                kural_uyum_oran -= kural_etkisi * (1 / pow(yurt_secenler, veri_sayi_carpani))
            elif sorumluluk_etkisi > kural_etkisi:
                sorumluluk_orani -= sorumluluk_etkisi * (1 / pow(yurt_secenler, veri_sayi_carpani))
            else:
                sorumluluk_orani -= sorumluluk_etkisi * (1 / pow(ev_secenler, veri_sayi_carpani))
                kural_uyum_oran -= kural_etkisi * (1 / pow(ev_secenler, veri_sayi_carpani))

            cursor.execute("UPDATE oranlar SET kural_uyum_oran = ? ,sorumluluk_sevme_oran = ? WHERE rowid = 1",
                           (kural_uyum_oran, sorumluluk_orani))
        conn.commit()
        conn.close()
    else:
        conn.commit()
        conn.close()
        # True = yurtta kal. False = Evde kal
        if gelir < 2000:
            return True
        else:
            return ((kural * kural_uyum_oran) + (sorumluluk * sorumluluk_orani)) > 0


def kisiye_karar_ver(ozel_alana_duskunluk, gelir):
    oda_arkadas_sayisi = 0
    tek_kisinin_kalabilecegi_minimum_gelir = 3000

    if ozel_alana_duskunluk < 2.5:
        oda_arkadas_sayisi += 1
        if ozel_alana_duskunluk < 1:
            oda_arkadas_sayisi += 1
    if gelir < tek_kisinin_kalabilecegi_minimum_gelir:
        oda_arkadas_sayisi += 1
        if gelir < tek_kisinin_kalabilecegi_minimum_gelir/2:
            oda_arkadas_sayisi += 1

    return oda_arkadas_sayisi
