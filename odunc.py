class Odunc:
    def __init__(self):
        self.odunc_kayitlari = {}
    
    def odunc_ver(self, kitap, uye):
        if kitap.durum == "Mevcut":
            kitap.durum = "Ödünçte"
            self.odunc_kayitlari[kitap.id] = uye.id
            uye.odunc_kitaplar.append(kitap.id)
            return True
        return False
    
    def iade_al(self, kitap, uye):
        if kitap.id in self.odunc_kayitlari and self.odunc_kayitlari[kitap.id] == uye.id:
            kitap.durum = "Mevcut"
            del self.odunc_kayitlari[kitap.id]
            uye.odunc_kitaplar.remove(kitap.id)
            return True
        return False