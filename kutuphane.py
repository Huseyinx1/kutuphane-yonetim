from odunc import Odunc
class Kutuphane:
    def __init__(self):
        self.kitaplar = {}
        self.uyeler = {}
        self.odunc_islem = Odunc()
    
    def kitap_ekle(self, kitap):
        if kitap.id in self.kitaplar:
            return False
        self.kitaplar[kitap.id] = kitap
        return True
    
    def uye_ekle(self, uye):
        if uye.id in self.uyeler:
            return False
        self.uyeler[uye.id] = uye
        return True
    
    def rapor_al(self):
        print(f"\nToplam Kitap: {len(self.kitaplar)}")
        print(f"Toplam Üye: {len(self.uyeler)}")
        print(f"Ödünçteki Kitaplar: {len(self.odunc_islem.odunc_kayitlari)}")