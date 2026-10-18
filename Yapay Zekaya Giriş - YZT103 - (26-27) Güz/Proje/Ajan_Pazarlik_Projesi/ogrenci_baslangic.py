"""YAPAY ZEKÂYA GİRİŞ - DÖNEM PROJESİ
İki Ajan Arasında Pazarlık (Öğrenci başlangıç dosyası)

Kütüphane kurulumu gerekmiyor. Python 3.10+ yeterlidir.
TODO alanlarını proje yönergesindeki kurallara göre tamamlayın.
"""


def alici_teklif(tur, ajan):
    """Alıcının bu turda teklif edeceği fiyatı hesaplayın.

    ajan = {"ilk_teklif": 60, "sinir": 100, "artis": 10}
    İpucu: min() işlevini kullanabilirsiniz.
    """
    # TODO 1
    pass


def satici_teklif(tur, ajan):
    """Satıcının bu turda isteyeceği fiyatı hesaplayın.

    ajan = {"ilk_teklif": 130, "sinir": 85, "indirim": 10}
    İpucu: max() işlevini kullanabilirsiniz.
    """
    # TODO 2
    pass


def pazarlik(alici, satici, maksimum_tur=5):
    """Her tur için iki teklifi hesaplayın ve karşılaştırın.

    Anlaşma varsa sözlük döndürün:
      {"durum": "anlasma", "tur": ..., "fiyat": ..., "gecmis": [...]}

    Anlaşma yoksa:
      {"durum": "anlasma_yok", "tur": None, "fiyat": None, "gecmis": [...]}

    Her geçmiş kaydı:
      {"tur": 1, "alici": 60, "satici": 130}
    """
    gecmis = []
    # TODO 3: for ile 1'den maksimum_tur'a kadar dönün.
    # TODO 4: Her turda alıcı ve satıcı tekliflerini üretin.
    # TODO 5: Teklifleri ekrana yazdırın ve gecmis listesine ekleyin.
    # TODO 6: alıcı >= satıcı ise orta fiyatı hesaplayın, sonucu döndürün.
    # TODO 7: Tüm turlar biterse anlaşma olmadığını bildirin.
    pass


if __name__ == "__main__":
    alici = {"ilk_teklif": 60, "sinir": 100, "artis": 10}
    satici = {"ilk_teklif": 130, "sinir": 85, "indirim": 10}
    sonuc = pazarlik(alici, satici, maksimum_tur=5)
    print("Sonuç:", sonuc)

    # TODO 8: Yönergedeki B, C ve D senaryolarını da çalıştırın.
