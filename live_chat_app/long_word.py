def kelime_sil(cümle):
    kelimeler = cümle.split()
    yeni_kelimeler = [kelime for kelime in kelimeler if len(kelime) <= 30]
    yeni_cümle = " ".join(yeni_kelimeler)
    return yeni_cümle
    