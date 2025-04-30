class Uye:
    def __init__(self, id, ad, soyad):
        self.id = id
        self.ad = ad
        self.soyad = soyad
        self.odunc_kitaplar = []
    
    def bilgileri_goster(self):
        return f"ID: {self.id} | Ad-Soyad: {self.ad} {self.soyad}"